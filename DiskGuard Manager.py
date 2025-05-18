import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk, UnidentifiedImageError
import psutil
import subprocess
import os

def show_splash(root, image_path, duration=2000):
    root.withdraw()
    try:
        img = Image.open(image_path)
    except (FileNotFoundError, UnidentifiedImageError):
        root.deiconify()
        return
    splash = tk.Toplevel(root)
    splash.overrideredirect(True)
    max_w, max_h = 400, 300
    img.thumbnail((max_w, max_h), Image.LANCZOS)
    splash_img = ImageTk.PhotoImage(img)
    splash.label = tk.Label(splash, image=splash_img, bd=0)
    splash.label.image = splash_img
    splash.label.pack()
    width, height = img.size
    x = (splash.winfo_screenwidth() - width) // 2
    y = (splash.winfo_screenheight() - height) // 2
    splash.geometry(f"{width}x{height}+{x}+{y}")
    root.after(duration, lambda: (splash.destroy(), root.deiconify()))

class PartitionManagerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestionnaire de Périphériques Externes")
        self.geometry("400x300")
        self.resizable(False, False)
        if os.path.exists('favicon.ico'):
            self.iconbitmap('favicon.ico')

        # Charger icônes
        self.icons = {}
        icons_files = {'scan': 'icons/scan.png', 'format': 'icons/format.png', 'exit': 'icons/exit.png'}
        for name, path in icons_files.items():
            if os.path.exists(path):
                img = Image.open(path).resize((16,16), Image.LANCZOS)
                self.icons[name] = ImageTk.PhotoImage(img)

        # Thème Vista
        style = ttk.Style()
        style.theme_use('vista')
        # Boutons arrondis via relief and padding
        style.configure('Rounded.TButton', font=("Segoe UI", 9), padding=6, relief='raised', borderwidth=1)
        style.map('Rounded.TButton', background=[('active', '#e6e6e6'), ('!active', '#ffffff')])
        # Combobox arrondie
        style.configure('Rounded.TCombobox', relief='groove', borderwidth=1, padding=3)

        self.configure(bg='#ffffff')
        # Grille principale
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        # Zone de commandes
        ctrl = ttk.Frame(self, padding=10)
        ctrl.grid(row=0, column=0, sticky='ew')
        ctrl.grid_columnconfigure(0, weight=1)

        # Bouton Scanner (plus petit, arrondi)
        self.scan_button = ttk.Button(ctrl, text="Scanner", image=self.icons.get('scan'), compound='left', style='Rounded.TButton', width=10, command=self.scan_devices)
        self.scan_button.grid(row=0, column=0, sticky='w')

        # Menu déroulant arrondi
        self.device_var = tk.StringVar()
        self.device_menu = ttk.Combobox(ctrl, textvariable=self.device_var, style='Rounded.TCombobox', state='readonly', width=15)
        self.device_menu.grid(row=1, column=0, pady=5, sticky='w')
        self.device_menu['values'] = ["Aucun détecté"]
        self.device_menu.current(0)

        # Zone de résultat
        self.result_frame = ttk.Frame(self, relief='solid', borderwidth=1, padding=5)
        self.result_frame.grid(row=1, column=0, padx=10, pady=5, sticky='nsew')
        self.result_text = tk.Text(self.result_frame, font=("Segoe UI", 9), relief='flat', bg='#ffffff')
        self.result_text.pack(fill='both', expand=True)

        # Bouton Formater en bas à droite
        self.format_button = ttk.Button(self, text="Formater", image=self.icons.get('format'), compound='left', style='Rounded.TButton', command=self.format_device)
        self.format_button.grid(row=2, column=0, sticky='e', padx=10, pady=10)

        # Quitter
        self.quit_button = ttk.Button(self, text="Quitter", image=self.icons.get('exit'), compound='left', style='Rounded.TButton', command=self.quit)
        self.quit_button.grid(row=2, column=0, sticky='w', padx=10, pady=10)

    def scan_devices(self):
        self.result_text.delete(1.0, tk.END)
        partitions = psutil.disk_partitions()
        external = []
        for p in partitions:
            try:
                usage = psutil.disk_usage(p.mountpoint)
                if usage.total < 500 * 1024**3:
                    external.append(f"{p.device} ({p.mountpoint})")
            except Exception:
                continue
        if external:
            self.result_text.insert(tk.END, "Périphériques :\n" + "\n".join(external))
            self.device_menu['values'] = external
            self.device_menu.current(0)
        else:
            self.result_text.insert(tk.END, "Aucun périphérique externe détecté.")
            self.device_menu['values'] = ["Aucun détecté"]
            self.device_menu.current(0)

    def format_device(self):
        sel = self.device_var.get().split()[0]
        if sel == "Aucun" or not sel:
            messagebox.showerror("Erreur", "Aucun périphérique sélectionné.")
            return
        if messagebox.askyesno("Confirmation", f"Formater {sel} ? Tous les fichiers seront perdus."):
            script = (
                f"select volume {sel}\n"
                "attributes disk clear readonly\n"
                "clean\n"
                "create partition primary\n"
                "format fs=ntfs quick\n"
                "assign\n"
                "exit\n"
            )
            with open("format_script.txt", "w") as f:
                f.write(script)
            res = subprocess.run("diskpart /s format_script.txt", shell=True, capture_output=True, text=True)
            if res.returncode == 0:
                messagebox.showinfo("Succès", f"{sel} formaté avec succès.")
            else:
                messagebox.showerror("Erreur", res.stderr)

if __name__ == "__main__":
    app = PartitionManagerApp()
    if os.path.exists('splash.png'):
        show_splash(app, 'splash.png')
    app.mainloop()

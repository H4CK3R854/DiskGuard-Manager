# Ce readme n'est pas a jour

# 📦 Gestionnaire de Périphériques Externes

Bienvenue dans **Gestionnaire de Périphériques Externes** ! Une application Python/Tkinter stylée Windows Vista/11 pour scanner, formater et gérer vos clés USB et cartes SD en toute simplicité. 🎉

---

## 🚀 Fonctionnalités

* 🔍 **Scan Instantané** : détecte automatiquement les périphériques externes (<500 Go).
* 🔄 **Splash Screen** : écran de démarrage animé (400×300) pour un look pro.
* 🎨 **Interface Windows-Like** : boutons arrondis, combobox stylée, barre de progression.
* 💾 **Formater** : efface et re-partitionne vos périphériques (force sans écriture protégée).
* 🔧 **Fallback Robust** : gestion des erreurs de ressource (splash, icônes, favicon).

---

## 🎨 Esthétique & Thème

* Thème **Vista** via `ttk.Style` pour un rendu natif Windows.
* Polices **Segoe UI** et couleurs épurées (#ffffff, #e6e6e6).
* Icônes personnalisées pour scanner, formater et quitter.

---

## 🛠️ Installation

1. Clonez le dépôt :

   ```bash
   git clone https://github.com/H4CK3R854/DiskGuard-Manager/](https://github.com/H4CK3R854/DiskGuard-Manager.git
   ```
2. Créez et activez un environnement virtuel (optionnel) :

   ```bash
   python -m venv venv
   source venv/Scripts/activate  # Windows
   ```
3. Installez les dépendances :

   ```bash
   pip install -r requirements.txt
   ```
4. Placez dans le dossier :

   * `favicon.ico` (icône de la fenêtre)
   * `splash.png` (image de démarrage)
   * Dossier `icons/` contenant `scan.png` et `format.png`

---

## ▶️ Utilisation

```bash
python main.py
```

1. **Splash Screen** apparaît pendant 2 s.
2. Fenêtre principale 400×300 responsive s’ouvre.
3. Cliquez sur **Scanner** pour détecter les périphériques externes.
4. Sélectionnez votre clé USB/carte SD et cliquez sur **Formater**. 🔥

---

## 📦 Générer un exécutable (.exe)

Utilisez \[auto-py-to-exe]:

```bash
pip install auto-py-to-exe
auto-py-to-exe
```

* Sélectionnez `main.py`, cochez `Onefile` et `Windowed`.
* Ajoutez `favicon.ico`, `splash.png`, dossier `icons/` dans "Additional Files".
* Lancez la conversion et récupérez votre `main.exe` dans `output/dist/`.

---

## ❤️ Contribuer

Toute contribution est la bienvenue ! Forkez, créez une branche, et ouvrez une **Pull Request**. 🤝

---

## 📜 Licence

CIKA © Othman Assim

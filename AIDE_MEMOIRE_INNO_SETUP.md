# AIDE-MÉMOIRE INNO SETUP
## Pour applications Python

---

## 🚀 WORKFLOW RAPIDE

```
1. Coder ton app Python
2. Compiler avec PyInstaller
3. Remplir le template .iss
4. Compiler avec Inno Setup
5. ✅ Installateur prêt !
```

---

## 📦 COMMANDE PYINSTALLER

```bash
# Application avec interface (sans console noire)
pyinstaller --onedir --windowed --name MonApp mon_script.py

# Application console
pyinstaller --onedir --name MonApp mon_script.py

# Avec une icône
pyinstaller --onedir --windowed --icon=icon.ico --name MonApp mon_script.py
```

**Résultat :** Dossier `dist/MonApp/` contenant ton .exe et ses dépendances

---

## 📝 SECTIONS INNO SETUP

| Section | Contenu | Obligatoire |
|---------|---------|-------------|
| `[Setup]` | Nom, version, dossiers | ✅ |
| `[Files]` | Fichiers à copier | ✅ |
| `[Icons]` | Raccourcis | ❌ |
| `[Run]` | Lancer après install | ❌ |
| `[Languages]` | Langues | ❌ |
| `[Tasks]` | Options utilisateur | ❌ |
| `[Registry]` | Registre Windows | ❌ |

---

## 📂 VARIABLES UTILES

| Variable | Chemin |
|----------|--------|
| `{app}` | Dossier d'installation |
| `{autopf}` | Program Files |
| `{autodesktop}` | Bureau |
| `{group}` | Menu Démarrer |
| `{userappdata}` | AppData\Roaming |
| `{tmp}` | Dossier temporaire |
| `{uninstallexe}` | Désinstallateur |

---

## 🔧 FLAGS COURANTS [Files]

| Flag | Effet |
|------|-------|
| `ignoreversion` | Remplacer même si plus récent |
| `recursesubdirs` | Inclure sous-dossiers |
| `createallsubdirs` | Créer dossiers vides |
| `isreadme` | Afficher après install |

---

## ✅ CHECKLIST AVANT COMPILATION

- [ ] PyInstaller exécuté → dossier `dist/` créé
- [ ] Tester le .exe manuellement
- [ ] Vérifier le chemin `Source:` dans [Files]
- [ ] Vérifier le nom .exe dans [Icons] et [Run]
- [ ] Icône présente si spécifiée

---

## 🐛 ERREURS COURANTES

| Erreur | Solution |
|--------|----------|
| `Source file not found` | Vérifier le chemin dans [Files] |
| `Compression invalid` | Utiliser `zip` ou `lzma` |
| `#define invalid` | Supprimer les #define, mettre valeurs directes |
| `.exe ne se lance pas` | Tester d'abord le .exe dans dist/ |

---

## 📁 STRUCTURE PROJET RECOMMANDÉE

```
MonProjet/
├── mon_script.py          # Code source
├── requirements.txt       # Dépendances pip
├── assets/
│   └── icon.ico          # Icône (optionnel)
├── dist/
│   └── MonApp/           # Généré par PyInstaller
│       ├── MonApp.exe
│       └── ...
├── installer.iss          # Script Inno Setup
└── installer_output/      # Installateur généré
    └── MonApp_Setup.exe
```

---

Créé par Claude pour Uriel - 2024

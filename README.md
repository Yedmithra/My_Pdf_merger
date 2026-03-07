# PDF Merger - Fusionneur de PDFs

Application Python pour fusionner des PDFs avec un contrôle précis du positionnement des pages.

## ✨ Fonctionnalités

- ✅ Ajouter des PDFs à la fin du document
- ✅ Ajouter des PDFs au début du document
- ✅ Insérer des PDFs à une position spécifique
- ✅ Réorganiser l'ordre des PDFs avant fusion
- ✅ Interface en ligne de commande (CLI)
- ✅ Interface graphique intuitive (GUI)
- ✅ Prévisualisation du nombre de pages
- ✅ Support de plusieurs PDFs en une seule opération

## 📋 Prérequis

- Python 3.7 ou supérieur
- pip (gestionnaire de paquets Python)

## 🔧 Installation

1. **Cloner ou télécharger les fichiers**

2. **Installer les dépendances**

```bash
pip install pypdf
```

Ou utiliser le fichier requirements.txt :

```bash
pip install -r requirements.txt
```

## 🚀 Utilisation

### Version Interface Graphique (Recommandé)

```bash
python pdf_merger_gui.py
```

**Fonctionnalités de l'interface :**

1. **Ajouter à la fin** : Ajoute des PDFs à la fin de la liste
2. **Ajouter au début** : Insère des PDFs au début de la liste
3. **Insérer à la position** : Insère des PDFs à une position spécifique
4. **Supprimer** : Retire le PDF sélectionné de la liste
5. **Monter/Descendre** : Réorganise l'ordre des PDFs
6. **Fusionner** : Crée le PDF final avec tous les documents

### Version Ligne de Commande

```bash
python pdf_merger.py
```

**Menu interactif :**

```
Options:
1. Ajouter un PDF à la fin
2. Ajouter un PDF au début
3. Ajouter un PDF à une position spécifique
4. Sauvegarder et quitter
5. Quitter sans sauvegarder
```

## 📝 Exemples d'utilisation

### Exemple 1 : Fusion simple (ajouter à la suite)

```
1. Lancer l'application GUI
2. Cliquer sur "Ajouter à la fin"
3. Sélectionner document1.pdf
4. Cliquer à nouveau sur "Ajouter à la fin"
5. Sélectionner document2.pdf
6. Cliquer sur "Fusionner les PDFs"
```

Résultat : document1.pdf suivi de document2.pdf

### Exemple 2 : Insérer au début

```
1. Ajouter document1.pdf (à la fin)
2. Ajouter document2.pdf (à la fin)
3. Cliquer sur "Ajouter au début"
4. Sélectionner intro.pdf
5. Fusionner
```

Résultat : intro.pdf, document1.pdf, document2.pdf

### Exemple 3 : Insérer à une position précise

```
1. Ajouter chapitre1.pdf
2. Ajouter chapitre3.pdf
3. Cliquer sur "Insérer à la position"
4. Choisir position 2
5. Sélectionner chapitre2.pdf
6. Fusionner
```

Résultat : chapitre1.pdf, chapitre2.pdf, chapitre3.pdf

### Exemple 4 : Réorganisation avant fusion

```
1. Ajouter plusieurs PDFs
2. Utiliser les boutons "Monter" et "Descendre"
3. Réorganiser dans l'ordre souhaité
4. Fusionner
```

## 🎯 Cas d'usage typiques

### 📚 Assemblage de rapport

```
1. Page de garde (début)
2. Sommaire (début)
3. Chapitres (à la suite)
4. Annexes (à la fin)
5. Dernière de couverture (à la fin)
```

### 📄 Fusion de documents administratifs

```
1. Formulaire principal
2. Pièces justificatives (insérées à des positions précises)
3. Documents complémentaires
```

### 📖 Création de livre ou manuel

```
1. Couverture
2. Préface
3. Chapitres (dans l'ordre)
4. Index
5. Quatrième de couverture
```

## 🔍 Détails techniques

### Bibliothèque utilisée

- **pypdf** : Bibliothèque moderne pour manipuler des PDFs en Python
  - Fork maintenu de PyPDF2
  - Meilleure performance
  - Support actif

### Structure du code

```
pdf_merger.py          # Version CLI avec menu interactif
pdf_merger_gui.py      # Version GUI avec Tkinter
requirements.txt       # Dépendances Python
README.md             # Ce fichier
```

### Classe PDFMerger

```python
PDFMerger()
├── add_pdf_at_end(pdf_path)          # Ajoute à la fin
├── add_pdf_at_beginning(pdf_path)    # Ajoute au début
├── add_pdf_at_position(pdf_path, pos) # Insère à une position
├── save(output_path)                 # Sauvegarde le résultat
└── get_page_count()                  # Compte les pages
```

## ⚠️ Limitations et notes

- Les PDFs doivent être valides et non corrompus
- Les PDFs protégés par mot de passe ne sont pas supportés
- La fusion préserve la structure des pages mais pas nécessairement tous les métadonnées
- Pour des PDFs très volumineux, l'opération peut prendre du temps

## 🐛 Dépannage

### Erreur "pypdf not found"

```bash
pip install --upgrade pypdf
```

### Erreur "Permission denied" lors de la sauvegarde

- Vérifiez que vous avez les droits d'écriture dans le dossier
- Fermez le PDF de sortie s'il est ouvert dans un lecteur

### PDF corrompu en sortie

- Vérifiez que tous les PDFs source sont valides
- Essayez de les ouvrir individuellement avant la fusion

## 💡 Améliorations futures possibles

- [ ] Support du glisser-déposer dans l'interface GUI
- [ ] Prévisualisation des pages avant fusion
- [ ] Extraction de pages spécifiques
- [ ] Rotation de pages
- [ ] Ajout de marque-pages (bookmarks)
- [ ] Ajout de numérotation de pages
- [ ] Support des PDFs protégés
- [ ] Mode batch via ligne de commande
- [ ] Export des métadonnées

## 📄 Licence

Code libre d'utilisation pour vos projets personnels et professionnels.

## 🤝 Contribution

Les suggestions et améliorations sont les bienvenues !

## 📞 Support

Pour toute question ou problème :
1. Vérifiez la section Dépannage
2. Vérifiez que pypdf est bien installé
3. Testez avec des PDFs simples d'abord

---

**Bon travail avec vos PDFs ! 📄✨**

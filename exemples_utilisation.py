#!/usr/bin/env python3
"""
Exemple d'utilisation programmatique du PDFMerger
Montre comment intégrer la fusion de PDFs dans vos propres scripts
"""

import sys
sys.path.insert(0, '.')  # Pour importer pdf_merger

from pdf_merger import PDFMerger


def exemple_simple():
    """Exemple 1 : Fusion simple de plusieurs PDFs à la suite"""
    print("=" * 60)
    print("Exemple 1 : Fusion simple")
    print("=" * 60)
    
    merger = PDFMerger()
    
    # Ajouter des PDFs à la suite
    merger.add_pdf_at_end("document1.pdf")
    merger.add_pdf_at_end("document2.pdf")
    merger.add_pdf_at_end("document3.pdf")
    
    # Sauvegarder
    merger.save("fusion_simple.pdf")
    print()


def exemple_avec_ordre_specifique():
    """Exemple 2 : Fusion avec un ordre spécifique"""
    print("=" * 60)
    print("Exemple 2 : Fusion avec ordre spécifique")
    print("=" * 60)
    
    merger = PDFMerger()
    
    # Ajouter les chapitres
    merger.add_pdf_at_end("chapitre1.pdf")
    merger.add_pdf_at_end("chapitre2.pdf")
    merger.add_pdf_at_end("chapitre3.pdf")
    
    # Ajouter la page de garde au début
    merger.add_pdf_at_beginning("page_garde.pdf")
    
    # Ajouter les annexes à la fin
    merger.add_pdf_at_end("annexes.pdf")
    
    # Insérer le sommaire après la page de garde (position 2)
    merger.add_pdf_at_position("sommaire.pdf", 2)
    
    merger.save("rapport_complet.pdf")
    print()


def exemple_assemblage_rapport():
    """Exemple 3 : Assemblage d'un rapport structuré"""
    print("=" * 60)
    print("Exemple 3 : Assemblage de rapport structuré")
    print("=" * 60)
    
    merger = PDFMerger()
    
    # Structure d'un rapport
    structure = [
        ("couverture.pdf", "début"),
        ("sommaire.pdf", "début"),
        ("introduction.pdf", "fin"),
        ("analyse.pdf", "fin"),
        ("conclusion.pdf", "fin"),
        ("references.pdf", "fin"),
        ("annexe_a.pdf", "fin"),
        ("annexe_b.pdf", "fin"),
    ]
    
    for fichier, position in structure:
        if position == "début":
            merger.add_pdf_at_beginning(fichier)
        else:
            merger.add_pdf_at_end(fichier)
    
    merger.save("rapport_final.pdf")
    print()


def exemple_insertion_precise():
    """Exemple 4 : Insertion à des positions précises"""
    print("=" * 60)
    print("Exemple 4 : Insertion à des positions précises")
    print("=" * 60)
    
    merger = PDFMerger()
    
    # Commencer avec le contenu principal
    merger.add_pdf_at_end("partie1.pdf")
    merger.add_pdf_at_end("partie3.pdf")
    merger.add_pdf_at_end("partie5.pdf")
    
    print(f"Pages après ajout initial: {merger.get_page_count()}")
    
    # Insérer les parties manquantes
    merger.add_pdf_at_position("partie2.pdf", 2)  # Entre partie1 et partie3
    merger.add_pdf_at_position("partie4.pdf", 4)  # Entre partie3 et partie5
    
    print(f"Pages après insertion: {merger.get_page_count()}")
    
    merger.save("document_complet.pdf")
    print()


def exemple_avec_verification():
    """Exemple 5 : Fusion avec vérifications"""
    print("=" * 60)
    print("Exemple 5 : Fusion avec vérifications")
    print("=" * 60)
    
    import os
    
    merger = PDFMerger()
    
    # Liste des fichiers à fusionner
    fichiers = [
        "rapport_Q1.pdf",
        "rapport_Q2.pdf",
        "rapport_Q3.pdf",
        "rapport_Q4.pdf",
    ]
    
    # Vérifier l'existence et ajouter
    for fichier in fichiers:
        if os.path.exists(fichier):
            merger.add_pdf_at_end(fichier)
        else:
            print(f"⚠️  Fichier introuvable: {fichier}")
    
    # Vérifier qu'il y a des pages avant de sauvegarder
    if merger.get_page_count() > 0:
        merger.save("rapport_annuel.pdf")
    else:
        print("❌ Aucun PDF à fusionner")
    print()


def exemple_batch_processing():
    """Exemple 6 : Traitement par lot de plusieurs dossiers"""
    print("=" * 60)
    print("Exemple 6 : Traitement par lot")
    print("=" * 60)
    
    import os
    from pathlib import Path
    
    # Traiter tous les PDFs d'un dossier
    dossier = "documents_a_fusionner"
    
    if os.path.exists(dossier):
        merger = PDFMerger()
        
        # Trier les fichiers par nom pour un ordre prévisible
        fichiers = sorted(Path(dossier).glob("*.pdf"))
        
        for fichier in fichiers:
            print(f"Ajout de {fichier.name}...")
            merger.add_pdf_at_end(str(fichier))
        
        if merger.get_page_count() > 0:
            merger.save(f"{dossier}_fusion.pdf")
        else:
            print("❌ Aucun PDF trouvé dans le dossier")
    else:
        print(f"⚠️  Dossier introuvable: {dossier}")
    print()


def exemple_integration_api():
    """Exemple 7 : Intégration dans une fonction/API"""
    print("=" * 60)
    print("Exemple 7 : Fonction réutilisable")
    print("=" * 60)
    
    def fusionner_pdfs(fichiers, sortie, ordre="sequentiel"):
        """
        Fusionne plusieurs PDFs
        
        Args:
            fichiers: Liste de chemins de fichiers PDF
            sortie: Chemin du fichier de sortie
            ordre: 'sequentiel', 'inverse', ou liste de positions
        
        Returns:
            bool: True si succès, False sinon
        """
        merger = PDFMerger()
        
        try:
            if ordre == "inverse":
                for fichier in reversed(fichiers):
                    merger.add_pdf_at_end(fichier)
            elif isinstance(ordre, list):
                # Ordre personnalisé basé sur les indices
                for idx in ordre:
                    if 0 <= idx < len(fichiers):
                        merger.add_pdf_at_end(fichiers[idx])
            else:  # sequentiel
                for fichier in fichiers:
                    merger.add_pdf_at_end(fichier)
            
            return merger.save(sortie)
        
        except Exception as e:
            print(f"❌ Erreur: {e}")
            return False
    
    # Utilisation
    mes_fichiers = ["doc1.pdf", "doc2.pdf", "doc3.pdf"]
    
    # Ordre normal
    fusionner_pdfs(mes_fichiers, "fusion_normale.pdf")
    
    # Ordre inverse
    fusionner_pdfs(mes_fichiers, "fusion_inverse.pdf", ordre="inverse")
    
    # Ordre personnalisé: [2, 0, 1] = doc3, doc1, doc2
    fusionner_pdfs(mes_fichiers, "fusion_custom.pdf", ordre=[2, 0, 1])
    print()


def menu_exemples():
    """Menu pour choisir quel exemple exécuter"""
    exemples = {
        '1': ("Fusion simple", exemple_simple),
        '2': ("Ordre spécifique", exemple_avec_ordre_specifique),
        '3': ("Assemblage de rapport", exemple_assemblage_rapport),
        '4': ("Insertions précises", exemple_insertion_precise),
        '5': ("Avec vérifications", exemple_avec_verification),
        '6': ("Traitement par lot", exemple_batch_processing),
        '7': ("Fonction réutilisable", exemple_integration_api),
        '8': ("Tous les exemples", None),
    }
    
    print("\n" + "=" * 60)
    print("EXEMPLES D'UTILISATION DU PDF MERGER")
    print("=" * 60)
    print("\nChoisissez un exemple à exécuter:\n")
    
    for key, (desc, _) in exemples.items():
        print(f"{key}. {desc}")
    
    choix = input("\nVotre choix (1-8): ").strip()
    
    if choix in exemples:
        if choix == '8':
            # Exécuter tous les exemples
            for key in sorted(exemples.keys()):
                if key != '8':
                    _, fonction = exemples[key]
                    fonction()
                    input("\nAppuyez sur Entrée pour continuer...")
        else:
            _, fonction = exemples[choix]
            fonction()
    else:
        print("❌ Choix invalide")


if __name__ == "__main__":
    print("""
╔══════════════════════════════════════════════════════════╗
║         EXEMPLES D'UTILISATION - PDF MERGER             ║
╚══════════════════════════════════════════════════════════╝

Ce script montre différentes façons d'utiliser la classe
PDFMerger dans vos propres projets Python.

NOTES IMPORTANTES:
- Ces exemples utilisent des noms de fichiers fictifs
- Adaptez les noms de fichiers à vos besoins réels
- Vérifiez toujours que les fichiers existent avant fusion
    """)
    
    menu_exemples()
    
    print("\n✨ Pour plus d'informations, consultez le README.md")

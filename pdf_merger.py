#!/usr/bin/env python3
"""
PDF Merger - Fusion de PDFs avec positionnement flexible
Permet d'insérer des pages PDF à différentes positions
"""

import os
import sys
from pathlib import Path
try:
    from pypdf import PdfReader, PdfWriter
except ImportError:
    print("Installation de pypdf requise: pip install pypdf")
    sys.exit(1)


class PDFMerger:
    """Classe pour fusionner des PDFs avec positionnement flexible"""
    
    def __init__(self):
        self.writer = PdfWriter()
        self.total_pages = 0
    
    def add_pdf_at_end(self, pdf_path):
        """Ajoute un PDF à la fin"""
        try:
            reader = PdfReader(pdf_path)
            for page in reader.pages:
                self.writer.add_page(page)
            pages_added = len(reader.pages)
            self.total_pages += pages_added
            print(f"✓ Ajouté '{os.path.basename(pdf_path)}' à la fin ({pages_added} page(s))")
            return True
        except Exception as e:
            print(f"✗ Erreur avec '{pdf_path}': {e}")
            return False
    
    def add_pdf_at_beginning(self, pdf_path):
        """Ajoute un PDF au début"""
        try:
            reader = PdfReader(pdf_path)
            # Créer un nouveau writer temporaire
            new_writer = PdfWriter()
            
            # Ajouter d'abord les nouvelles pages
            for page in reader.pages:
                new_writer.add_page(page)
            
            # Puis ajouter les pages existantes
            for page in self.writer.pages:
                new_writer.add_page(page)
            
            pages_added = len(reader.pages)
            self.writer = new_writer
            self.total_pages += pages_added
            print(f"✓ Ajouté '{os.path.basename(pdf_path)}' au début ({pages_added} page(s))")
            return True
        except Exception as e:
            print(f"✗ Erreur avec '{pdf_path}': {e}")
            return False
    
    def add_pdf_at_position(self, pdf_path, position):
        """
        Ajoute un PDF à une position spécifique (1-indexed)
        Position 1 = début, position > total = fin
        """
        try:
            reader = PdfReader(pdf_path)
            new_writer = PdfWriter()
            
            # Ajuster la position (convertir en 0-indexed)
            insert_pos = max(0, min(position - 1, self.total_pages))
            
            # Ajouter les pages avant la position
            for i in range(insert_pos):
                if i < len(self.writer.pages):
                    new_writer.add_page(self.writer.pages[i])
            
            # Ajouter les nouvelles pages
            for page in reader.pages:
                new_writer.add_page(page)
            
            # Ajouter les pages après la position
            for i in range(insert_pos, len(self.writer.pages)):
                new_writer.add_page(self.writer.pages[i])
            
            pages_added = len(reader.pages)
            self.writer = new_writer
            self.total_pages += pages_added
            print(f"✓ Ajouté '{os.path.basename(pdf_path)}' à la position {position} ({pages_added} page(s))")
            return True
        except Exception as e:
            print(f"✗ Erreur avec '{pdf_path}': {e}")
            return False
    
    def save(self, output_path):
        """Sauvegarde le PDF fusionné"""
        try:
            with open(output_path, 'wb') as output_file:
                self.writer.write(output_file)
            print(f"\n✓ PDF créé avec succès: {output_path}")
            print(f"  Total de pages: {self.total_pages}")
            return True
        except Exception as e:
            print(f"\n✗ Erreur lors de la sauvegarde: {e}")
            return False
    
    def get_page_count(self):
        """Retourne le nombre total de pages actuel"""
        return self.total_pages


def menu_interactif():
    """Menu interactif pour fusionner des PDFs"""
    print("=" * 60)
    print("PDF MERGER - Fusion de PDFs avec positionnement")
    print("=" * 60)
    
    merger = PDFMerger()
    
    while True:
        print(f"\nPages actuelles dans le document: {merger.get_page_count()}")
        print("\nOptions:")
        print("1. Ajouter un PDF à la fin")
        print("2. Ajouter un PDF au début")
        print("3. Ajouter un PDF à une position spécifique")
        print("4. Sauvegarder et quitter")
        print("5. Quitter sans sauvegarder")
        
        choix = input("\nVotre choix (1-5): ").strip()
        
        if choix == '1':
            pdf_path = input("Chemin du PDF à ajouter: ").strip()
            if os.path.exists(pdf_path):
                merger.add_pdf_at_end(pdf_path)
            else:
                print(f"✗ Fichier introuvable: {pdf_path}")
        
        elif choix == '2':
            pdf_path = input("Chemin du PDF à ajouter: ").strip()
            if os.path.exists(pdf_path):
                merger.add_pdf_at_beginning(pdf_path)
            else:
                print(f"✗ Fichier introuvable: {pdf_path}")
        
        elif choix == '3':
            pdf_path = input("Chemin du PDF à ajouter: ").strip()
            if not os.path.exists(pdf_path):
                print(f"✗ Fichier introuvable: {pdf_path}")
                continue
            
            try:
                position = int(input(f"Position d'insertion (1-{merger.get_page_count() + 1}): "))
                merger.add_pdf_at_position(pdf_path, position)
            except ValueError:
                print("✗ Position invalide")
        
        elif choix == '4':
            if merger.get_page_count() == 0:
                print("\n✗ Aucune page à sauvegarder")
                continue
            
            output = input("Nom du fichier de sortie (ex: resultat.pdf): ").strip()
            if not output.endswith('.pdf'):
                output += '.pdf'
            
            if merger.save(output):
                break
        
        elif choix == '5':
            print("\nAnnulé.")
            break
        
        else:
            print("✗ Choix invalide")


def mode_ligne_commande():
    """Mode ligne de commande pour usage avancé"""
    print("Usage: python pdf_merger.py <pdf1> [position1] <pdf2> [position2] ... -o <output>")
    print("\nPositions:")
    print("  'start' ou 's' = début")
    print("  'end' ou 'e' = fin (défaut)")
    print("  nombre (1, 2, 3...) = position spécifique")
    print("\nExemples:")
    print("  python pdf_merger.py doc1.pdf doc2.pdf -o resultat.pdf")
    print("  python pdf_merger.py doc1.pdf s doc2.pdf e doc3.pdf 2 -o resultat.pdf")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] in ['-h', '--help']:
        mode_ligne_commande()
    elif len(sys.argv) > 1:
        # Mode ligne de commande (à implémenter si besoin)
        print("Mode ligne de commande en développement...")
        print("Utilisation du mode interactif:\n")
        menu_interactif()
    else:
        # Mode interactif par défaut
        menu_interactif()

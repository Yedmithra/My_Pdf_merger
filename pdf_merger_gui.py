#!/usr/bin/env python3
"""
PDF Merger GUI - Interface graphique pour fusionner des PDFs
"""

import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from pathlib import Path

try:
    from pypdf import PdfReader, PdfWriter
except ImportError:
    print("Installation requise: pip install pypdf")
    import sys
    sys.exit(1)


class PDFMergerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Merger - Fusion de PDFs")
        self.root.geometry("800x600")
        self.root.resizable(True, True)
        
        # Liste des PDFs à fusionner
        self.pdf_list = []
        
        self.setup_ui()
    
    def setup_ui(self):
        """Configuration de l'interface utilisateur"""
        
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configuration du grid
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(1, weight=1)
        
        # Titre
        title_label = ttk.Label(
            main_frame, 
            text="Fusionneur de PDFs", 
            font=('Arial', 16, 'bold')
        )
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 10))
        
        # Frame pour la liste des PDFs
        list_frame = ttk.LabelFrame(main_frame, text="PDFs à fusionner", padding="5")
        list_frame.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)
        list_frame.columnconfigure(0, weight=1)
        list_frame.rowconfigure(0, weight=1)
        
        # Treeview pour afficher les PDFs
        columns = ('Position', 'Fichier', 'Pages')
        self.tree = ttk.Treeview(list_frame, columns=columns, show='headings', height=10)
        
        self.tree.heading('Position', text='Position')
        self.tree.heading('Fichier', text='Nom du fichier')
        self.tree.heading('Pages', text='Pages')
        
        self.tree.column('Position', width=80, anchor='center')
        self.tree.column('Fichier', width=400)
        self.tree.column('Pages', width=80, anchor='center')
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        self.tree.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        
        # Frame pour les boutons d'action
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=2, column=0, columnspan=3, pady=10)
        
        ttk.Button(
            button_frame, 
            text="➕ Ajouter à la fin", 
            command=self.add_pdf_end
        ).grid(row=0, column=0, padx=5)
        
        ttk.Button(
            button_frame, 
            text="⬆️ Ajouter au début", 
            command=self.add_pdf_start
        ).grid(row=0, column=1, padx=5)
        
        ttk.Button(
            button_frame, 
            text="📍 Insérer à la position...", 
            command=self.add_pdf_position
        ).grid(row=0, column=2, padx=5)
        
        ttk.Button(
            button_frame, 
            text="❌ Supprimer", 
            command=self.remove_selected
        ).grid(row=0, column=3, padx=5)
        
        ttk.Button(
            button_frame, 
            text="⬆️ Monter", 
            command=self.move_up
        ).grid(row=0, column=4, padx=5)
        
        ttk.Button(
            button_frame, 
            text="⬇️ Descendre", 
            command=self.move_down
        ).grid(row=0, column=5, padx=5)
        
        # Frame pour la sortie
        output_frame = ttk.LabelFrame(main_frame, text="Fichier de sortie", padding="5")
        output_frame.grid(row=3, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=5)
        output_frame.columnconfigure(1, weight=1)
        
        ttk.Label(output_frame, text="Nom:").grid(row=0, column=0, padx=5)
        
        self.output_entry = ttk.Entry(output_frame)
        self.output_entry.insert(0, "pdf_managed.pdf")
        self.output_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=5)
        
        ttk.Button(
            output_frame, 
            text="📁 Parcourir", 
            command=self.browse_output
        ).grid(row=0, column=2, padx=5)
        
        # Frame pour les actions finales
        action_frame = ttk.Frame(main_frame)
        action_frame.grid(row=4, column=0, columnspan=3, pady=10)
        
        ttk.Button(
            action_frame, 
            text="✅ Fusionner les PDFs", 
            command=self.merge_pdfs,
            style='Accent.TButton'
        ).grid(row=0, column=0, padx=5)
        
        ttk.Button(
            action_frame, 
            text="🗑️ Tout effacer", 
            command=self.clear_all
        ).grid(row=0, column=1, padx=5)
        
        # Label de statut
        self.status_label = ttk.Label(main_frame, text="Prêt", relief=tk.SUNKEN, anchor=tk.W)
        self.status_label.grid(row=5, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(5, 0))
    
    def update_status(self, message):
        """Met à jour le statut"""
        self.status_label.config(text=message)
        self.root.update_idletasks()
    
    def get_pdf_info(self, pdf_path):
        """Récupère les informations d'un PDF"""
        try:
            reader = PdfReader(pdf_path)
            return len(reader.pages)
        except Exception as e:
            messagebox.showerror("Erreur", f"Impossible de lire le PDF:\n{e}")
            return None
    
    def refresh_tree(self):
        """Rafraîchit l'affichage de la liste"""
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        total_pages = 0
        for idx, (path, pages) in enumerate(self.pdf_list, 1):
            filename = os.path.basename(path)
            self.tree.insert('', tk.END, values=(idx, filename, pages))
            total_pages += pages
        
        self.update_status(f"{len(self.pdf_list)} PDF(s) - Total: {total_pages} page(s)")
    
    def add_pdf_end(self):
        """Ajoute un PDF à la fin"""
        files = filedialog.askopenfilenames(
            title="Sélectionner des PDFs",
            filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")]
        )
        
        for file in files:
            pages = self.get_pdf_info(file)
            if pages:
                self.pdf_list.append((file, pages))
        
        self.refresh_tree()
    
    def add_pdf_start(self):
        """Ajoute un PDF au début"""
        files = filedialog.askopenfilenames(
            title="Sélectionner des PDFs",
            filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")]
        )
        
        for file in reversed(files):
            pages = self.get_pdf_info(file)
            if pages:
                self.pdf_list.insert(0, (file, pages))
        
        self.refresh_tree()
    
    def add_pdf_position(self):
        """Ajoute un PDF à une position spécifique"""
        if not self.pdf_list:
            messagebox.showinfo("Info", "Ajoutez d'abord un PDF à la liste")
            return
        
        # Dialogue pour choisir la position
        dialog = tk.Toplevel(self.root)
        dialog.title("Choisir la position")
        dialog.geometry("300x150")
        dialog.transient(self.root)
        dialog.grab_set()
        
        ttk.Label(dialog, text="Insérer à la position:").pack(pady=10)
        
        position_var = tk.IntVar(value=len(self.pdf_list) + 1)
        spinbox = ttk.Spinbox(
            dialog, 
            from_=1, 
            to=len(self.pdf_list) + 1, 
            textvariable=position_var,
            width=10
        )
        spinbox.pack(pady=5)
        
        result = {'position': None}
        
        def ok():
            result['position'] = position_var.get()
            dialog.destroy()
        
        def cancel():
            dialog.destroy()
        
        btn_frame = ttk.Frame(dialog)
        btn_frame.pack(pady=10)
        
        ttk.Button(btn_frame, text="OK", command=ok).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Annuler", command=cancel).pack(side=tk.LEFT, padx=5)
        
        dialog.wait_window()
        
        if result['position']:
            files = filedialog.askopenfilenames(
                title="Sélectionner des PDFs",
                filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")]
            )
            
            pos = result['position'] - 1
            for file in files:
                pages = self.get_pdf_info(file)
                if pages:
                    self.pdf_list.insert(pos, (file, pages))
                    pos += 1
            
            self.refresh_tree()
    
    def remove_selected(self):
        """Supprime le PDF sélectionné"""
        selection = self.tree.selection()
        if not selection:
            messagebox.showinfo("Info", "Sélectionnez un PDF à supprimer")
            return
        
        item = selection[0]
        index = self.tree.index(item)
        del self.pdf_list[index]
        self.refresh_tree()
    
    def move_up(self):
        """Déplace le PDF sélectionné vers le haut"""
        selection = self.tree.selection()
        if not selection:
            return
        
        item = selection[0]
        index = self.tree.index(item)
        
        if index > 0:
            self.pdf_list[index], self.pdf_list[index - 1] = \
                self.pdf_list[index - 1], self.pdf_list[index]
            self.refresh_tree()
            # Resélectionner l'item
            new_item = self.tree.get_children()[index - 1]
            self.tree.selection_set(new_item)
    
    def move_down(self):
        """Déplace le PDF sélectionné vers le bas"""
        selection = self.tree.selection()
        if not selection:
            return
        
        item = selection[0]
        index = self.tree.index(item)
        
        if index < len(self.pdf_list) - 1:
            self.pdf_list[index], self.pdf_list[index + 1] = \
                self.pdf_list[index + 1], self.pdf_list[index]
            self.refresh_tree()
            # Resélectionner l'item
            new_item = self.tree.get_children()[index + 1]
            self.tree.selection_set(new_item)
    
    def browse_output(self):
        """Choisir le fichier de sortie"""
        filename = filedialog.asksaveasfilename(
            title="Enregistrer sous",
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")]
        )
        
        if filename:
            self.output_entry.delete(0, tk.END)
            self.output_entry.insert(0, filename)
    
    def clear_all(self):
        """Efface tous les PDFs de la liste"""
        if self.pdf_list and messagebox.askyesno(
            "Confirmation", 
            "Voulez-vous vraiment tout effacer ?"
        ):
            self.pdf_list.clear()
            self.refresh_tree()
    
    def merge_pdfs(self):
        """Fusionne tous les PDFs"""
        if not self.pdf_list:
            messagebox.showwarning("Attention", "Aucun PDF à fusionner")
            return
        
        output_path = self.output_entry.get()
        if not output_path:
            messagebox.showwarning("Attention", "Spécifiez un nom de fichier de sortie")
            return
        
        if not output_path.endswith('.pdf'):
            output_path += '.pdf'
        
        try:
            self.update_status("Fusion en cours...")
            writer = PdfWriter()
            
            for pdf_path, _ in self.pdf_list:
                reader = PdfReader(pdf_path)
                for page in reader.pages:
                    writer.add_page(page)
            
            with open(output_path, 'wb') as output_file:
                writer.write(output_file)
            
            total_pages = sum(pages for _, pages in self.pdf_list)
            self.update_status(f"✓ Fusion réussie: {output_path}")
            
            messagebox.showinfo(
                "Succès", 
                f"PDF créé avec succès!\n\n"
                f"Fichier: {output_path}\n"
                f"Pages: {total_pages}\n"
                f"PDFs fusionnés: {len(self.pdf_list)}"
            )
            
        except Exception as e:
            self.update_status("✗ Erreur lors de la fusion")
            messagebox.showerror("Erreur", f"Erreur lors de la fusion:\n{e}")


def main():
    root = tk.Tk()
    app = PDFMergerGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()

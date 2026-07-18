import tkinter as tk # la bibliothèque d'afficharge des interfaces graphiques
from tkinter import ttk, messagebox # (messagebox)--> afficharge des messages
from operator import itemgetter #pour ranger les etudiants par moyenne

# Définition des données de base

etudiants = [
    {'id': 1, 'nom': 'OFIE', 'prenom': 'K. Frédéric'},
    {'id': 2, 'nom': 'NOUDOFININ', 'prenom': 'L.B. Priscillia'},
    {'id': 3, 'nom': 'NINI', 'prenom': 'P. Ulrich'},
    {'id': 4, 'nom': 'OUBETTO', 'prenom': 'K.Jean'},
    {'id': 5, 'nom': 'OKE', 'prenom': 'M.Geoffroy'}

]
# Dictionnaire des notes (clé: ID étudiant)
matieres = ["Mathématiques", "Physique", "Chimie", "Informatique"]
evaluations = ["E1", "E2", "D1", "D2"]
#Dictionnare des notes pour chaque étudiant
notes = {
    1: {
        "Mathématiques": {"E1": 14, "E2": 15, "D1": 13, "D2": 16},
        "Physique": {"E1": 12, "E2": 14, "D1": 11, "D2": 13},
        "Chimie": {"E1": 13, "E2": 13, "D1": 12, "D2": 14},
        "Informatique": {"E1": 15, "E2": 16, "D1": 14, "D2": 15}
    },
    2: {
        "Mathématiques": {"E1": 10, "E2": 12, "D1": 11, "D2": 13},
        "Physique": {"E1": 19, "E2": 10, "D1": 18, "D2": 11},
        "Chimie": {"E1": 11, "E2": 12, "D1": 10, "D2": 13},
        "Informatique": {"E1": 14, "E2": 13, "D1": 15, "D2": 16}
    },
    3: {
        "Mathématiques": {"E1": 18, "E2": 17, "D1": 19, "D2": 18},
        "Physique": {"E1": 17, "E2": 18, "D1": 14, "D2": 17},
        "Chimie": {"E1": 10, "E2": 17, "D1": 15, "D2": 16},
        "Informatique": {"E1": 19, "E2": 10, "D1": 18, "D2": 9}
    },
    4: {
        "Mathématiques": {"E1": 10, "E2": 12, "D1": 11, "D2": 13},
        "Physique": {"E1": 9, "E2": 10, "D1": 8, "D2": 11},
        "Chimie": {"E1": 11, "E2": 12, "D1": 14, "D2": 13},
        "Informatique": {"E1": 17, "E2": 15, "D1": 15, "D2": 17}
    },
    5: {
        "Mathématiques": {"E1": 10, "E2": 12, "D1": 11, "D2": 13},
        "Physique": {"E1": 9, "E2": 10, "D1": 18, "D2": 11},
        "Chimie": {"E1": 11, "E2": 9, "D1": 10, "D2": 13},
        "Informatique": {"E1": 14, "E2": 17, "D1": 15, "D2": 17}
    }

}
# Fonction pour générer une structure de notes vide
def initialiser_notes():
    return {matiere: {eval: None for eval in evaluations} for matiere in matieres} # retourne d'un dictionnaire de dictionnaire
# ------- Interface graphique  --------

# Fenêtre pour ajouter un étudiant
def ajouter_etudiant_gui(nom, prenom, fenetre):
    if not nom or not prenom:
        messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")
        return
    id_etudiant = len(etudiants) + 1  #genere le matricule de l'etudiant
    etudiants.append({'id': id_etudiant, 'nom': nom, 'prenom': prenom}) # ajouter un autre étudiant 
    notes[id_etudiant] = initialiser_notes()
    messagebox.showinfo("L'étudiant", f"ID {id_etudiant} a été ajouté avec succès ")
    fenetre.destroy()

def interface_ajouter_etudiant():
    fen = tk.Toplevel(root)
    fen.title("Ajouter un étudiant")
    fen.geometry("400x200")
    tk.Label(fen, text="Nom").pack()
    entry_nom = tk.Entry(fen)
    entry_nom.pack()
    tk.Label(fen, text="Prénom").pack()
    entry_prenom = tk.Entry(fen)
    entry_prenom.pack()
    tk.Button(fen, text="Ajouter", command=lambda: ajouter_etudiant_gui(entry_nom.get(), entry_prenom.get(), fen)).pack(pady=10)

def interface_saisir_notes():
    if not etudiants:
        messagebox.showwarning("Attention !", "Aucun étudiant enregistré.")
        return

    fen = tk.Toplevel(root)
    fen.title("Saisir les notes")
    fen.geometry("500x400")

    tk.Label(fen, text="Choisissez l'étudiant :").pack()
    student_var = tk.StringVar()
    student_choices = [f"{e['id']} - {e['prenom']} {e['nom']}" for e in etudiants]
    student_menu = ttk.Combobox(fen, textvariable=student_var, values=student_choices, state='readonly')
    student_menu.pack()

    tk.Label(fen, text="Choisissez la matière :").pack()
    matiere_var = tk.StringVar()
    matiere_menu = ttk.Combobox(fen, textvariable=matiere_var, values=matieres, state='readonly')
    matiere_menu.pack()

    note_vars = {}
    for eval in evaluations:
        tk.Label(fen, text=f"Note {eval} (0-20)").pack()
        var = tk.StringVar()
        note_vars[eval] = var
        tk.Entry(fen, textvariable=var).pack()

    def enregistrer_notes():
        try:
            id_etudiant = int(student_var.get().split(" - ")[0])
            matiere = matiere_var.get()
            for eval in evaluations:
                val = note_vars[eval].get().strip()
                if val:
                    val = float(val)
                    if 0 <= val <= 20:
                        notes[id_etudiant][matiere][eval] = val
                    else:
                        raise ValueError("Note hors limites")
            messagebox.showinfo("Enregistrées", "avec succès")
            fen.destroy()
        except Exception as e:
            messagebox.showerror("Ooh !", f"Erreur lors de la saisie : {e}")

    tk.Button(fen, text="Enregistrer", command=enregistrer_notes).pack(pady=10)
# Fonctions de calcul de moyennes 
    # Moyenne pour une matière
def calculer_moyenne_matiere(id_etudiant, matiere):
    notes_matiere = notes[id_etudiant][matiere]
    total = 0
    poids_total = 0
    if notes_matiere['E1'] is not None:
        total += notes_matiere['E1'] * 0.3
        poids_total += 0.3
    if notes_matiere['E2'] is not None:
        total += notes_matiere['E2'] * 0.3
        poids_total += 0.3
    if notes_matiere['D1'] is not None:
        total += notes_matiere['D1'] * 0.2
        poids_total += 0.2
    if notes_matiere['D2'] is not None:
        total += notes_matiere['D2'] * 0.2
        poids_total += 0.2
    return round(total / poids_total, 2) if poids_total else None

# Moyenne générale de l'étudiant
def calculer_moyenne_generale(id_etudiant):
    moyennes = [calculer_moyenne_matiere(id_etudiant, m) for m in matieres]
    moyennes = [m for m in moyennes if m is not None]
    return round(sum(moyennes) / len(moyennes), 2) if moyennes else None

# Afficharge du bulletin
def interface_afficher_bulletin():
    if not etudiants:
        messagebox.showwarning("Attention !", "Aucun étudiant enregistré.")
        return

    fen = tk.Toplevel(root)
    fen.title("Bulletin d'un étudiant")
    fen.geometry("600x400")

    tk.Label(fen, text="Sélectionnez un étudiant :").pack()
    var = tk.StringVar()
    choix = [f"{e['id']} - {e['prenom']} {e['nom']}" for e in etudiants]
    menu = ttk.Combobox(fen, textvariable=var, values=choix, state='readonly')
    menu.pack()

    text = tk.Text(fen, height=20, width=70)
    text.pack()

    def afficher():
        try:
            id_etudiant = int(var.get().split(" - ")[0])
            e = next(e for e in etudiants if e['id'] == id_etudiant)
            text.delete("1.0", tk.END)
            text.insert(tk.END, f"Bulletin de {e['prenom']} {e['nom']}\n\n")
            for matiere in matieres:
                text.insert(tk.END, f"{matiere}:\n")
                for eval in evaluations:
                    note = notes[id_etudiant][matiere][eval]
                    note_str = f"{note}/20" if note is not None else "Pas de note"
                    text.insert(tk.END, f"  {eval}: {note_str}\n")
                moyenne = calculer_moyenne_matiere(id_etudiant, matiere)
                text.insert(tk.END, f"  Moyenne: {moyenne if moyenne is not None else 'Pas de note'}\n\n")
            gen = calculer_moyenne_generale(id_etudiant)
            text.insert(tk.END, f"Moyenne générale: {gen if gen is not None else 'Pas de note'}\n")
        except:
            messagebox.showerror("Ooh !", "Sélection invalide.")

    tk.Button(fen, text="Afficher", command=afficher).pack(pady=5)
# Interface pour voir le classement
def interface_afficher_classement():
    fen = tk.Toplevel(root)
    fen.title("Classement")
    fen.geometry("600x400")

    tree = ttk.Treeview(fen, columns=("nom", "moyenne"), show="headings")
    tree.heading("nom", text="Étudiant")
    tree.heading("moyenne", text="Moyenne")
    tree.pack(fill="both", expand=True)

    classement = []
    for e in etudiants:
        m = calculer_moyenne_generale(e['id'])
        if m is not None:
            classement.append((f"{e['prenom']} {e['nom']}", m))

    for i, (nom, moy) in enumerate(sorted(classement, key=lambda x: x[1], reverse=True), 1):
        tree.insert("", "end", values=(nom, f"{moy:.2f}"))
# Interface d'ajout de moyenne 
def interface_afficher_moyennes():
    fen = tk.Toplevel(root)
    fen.title("Moyennes par matière")
    fen.geometry("400x300")
    text = tk.Text(fen)
    text.pack(fill="both", expand=True)

    for mat in matieres:
        toutes = [calculer_moyenne_matiere(e['id'], mat) for e in etudiants]
        toutes = [m for m in toutes if m is not None]
        if toutes:
            moyenne = sum(toutes) / len(toutes)
            text.insert(tk.END, f"{mat}: {moyenne:.2f} sur {len(toutes)} étudiants\n")
        else:
            text.insert(tk.END, f"{mat}:Pas de note \n")

#Afficher menu et retourner choix utilisateur
def menu_principal():
    frame = tk.Frame(root, bg="#091821")
    frame.pack(fill="both", expand=True, pady=50)
    tk.Label(frame, text="Système de gestion de notes", font=("Arial", 24), bg="#091821", fg="white").pack(pady=20)
    boutons = [
        ("Ajouter un étudiant", interface_ajouter_etudiant),
        ("Saisir les notes", interface_saisir_notes),
        ("Afficher bulletin", interface_afficher_bulletin),
        ("Classement général", interface_afficher_classement),
        ("Moyennes par matière", interface_afficher_moyennes),
        ("Quitter", root.quit)
    ]
    for txt, cmd in boutons:
        tk.Button(frame, text=txt, command=cmd, width=30, font=("Arial", 12)).pack(pady=5)

# Création de menu principal 
root = tk.Tk()
root.title("Gestion des Notes")
root.geometry("800x600")
root.configure(bg="#091821")
menu_principal()
root.mainloop()
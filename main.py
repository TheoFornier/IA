import random
import matplotlib.pyplot as plt
import numpy as np

# Dimensions de l'échiquier
echiquier_lignes = 8
echiquier_colonnes = 8

# Liste des types de pièces
types_pieces = ['Roi', 'Reine', 'Tour', 'Fou', 'Cavalier', 'Pion']

# Formes pour chaque type de pièce
formes_pieces = {
    'Roi': '♚',
    'Reine': '♛',
    'Tour': '♜',
    'Fou': '♝',
    'Cavalier': '♞',
    'Pion': '♟',
}

# Couleur d'arrière-plan des cases
couleur_case_blanche = '#FFEEDD'  # Jaune pâle
couleur_case_noire = '#B5915F'    # Brun clair

# Équipes
equipe_blanc = 'Blanc'
equipe_noir = 'Noir'

# Fonction pour créer une disposition aléatoire des pièces avec des équipes
def generer_disposition_aleatoire():
    disposition = [['' for _ in range(echiquier_colonnes)] for _ in range(echiquier_lignes)]
    equipe = [['' for _ in range(echiquier_colonnes)] for _ in range(echiquier_lignes)]
    pieces_placees = 0

    while pieces_placees < 10:
        i, j = random.randint(0, echiquier_lignes - 1), random.randint(0, echiquier_colonnes - 1)

        if disposition[i][j] == '':
            piece = random.choice(types_pieces)
            disposition[i][j] = piece

            # Définir la couleur de l'équipe en fonction de la couleur de la case
            equipe[i][j] = equipe_blanc if (i + j) % 2 != 0 else equipe_noir

            pieces_placees += 1

    return disposition, equipe

# Fonction pour afficher l'échiquier avec matplotlib
def afficher_echiquier(disposition, equipe):
    # Vérifier s'il y a des pièces sur l'échiquier
    if not any(piece for ligne in disposition for piece in ligne):
        print("Il n'y a pas de pièces d'échecs à afficher.")
        return

    fig, ax = plt.subplots()
    ax.set_aspect('equal')

    for i in range(echiquier_lignes):
        for j in range(echiquier_colonnes):
            couleur_case = couleur_case_blanche if (i + j) % 2 == 0 else couleur_case_noire
            ax.add_patch(plt.Rectangle((j, i), 1, 1, color=couleur_case))

            piece = disposition[i][j]
            if piece:
                couleur_piece = 'black' if equipe[i][j] == equipe_noir else 'white'
                ax.text(j + 0.5, i + 0.5, formes_pieces[piece], color=couleur_piece,
                        fontsize=20, fontweight='bold', ha='center', va='center')

    ax.set_xlim(0, echiquier_colonnes)
    ax.set_ylim(0, echiquier_lignes)
    ax.set_xticks(np.arange(0.5, echiquier_colonnes, 1))
    ax.set_yticks(np.arange(0.5, echiquier_lignes, 1))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    plt.grid(False)  # Désactiver les lignes de la grille

    # Fonction appelée lors d'un clic de souris
    def on_click(event):
        if event.inaxes is not None:
            i, j = int(event.ydata), int(event.xdata)
            piece = disposition[i][j]

            # Vérifier si la case cliquée contient une pièce
            if piece:
                equipe_piece = equipe[i][j]
                print(f"Vous avez cliqué sur la case ({i}, {j}) contenant la pièce : {piece} de l'équipe : {equipe_piece}")
            else:
                print(f"La case ({i}, {j}) ne contient aucune pièce.")

    # Attacher la fonction on_click à l'événement de clic de la souris
    plt.gcf().canvas.mpl_connect('button_press_event', on_click)

    plt.show()

# Générer une disposition aléatoire des pièces avec des équipes et un maximum de 10 pièces
disposition_aleatoire, equipe_aleatoire = generer_disposition_aleatoire()

# Afficher l'échiquier avec matplotlib
afficher_echiquier(disposition_aleatoire, equipe_aleatoire)

"""import random
import matplotlib.pyplot as plt
import numpy as np
from transformers import BertTokenizer, BertForSequenceClassification
import torch

# Dimensions de l'échiquier
echiquier_lignes = 8
echiquier_colonnes = 8

# Liste des types de pièces
types_pieces = ['Roi', 'Reine', 'Tour', 'Fou', 'Cavalier', 'Pion']

# Formes pour chaque type de pièce
formes_pieces = {
    'Roi': '♚',
    'Reine': '♛',
    'Tour': '♜',
    'Fou': '♝',
    'Cavalier': '♞',
    'Pion': '♟',
}

# Couleur d'arrière-plan des cases
couleur_case_blanche = '#FFEEDD'  # Jaune pâle
couleur_case_noire = '#B5915F'    # Brun clair

# Équipes
equipe_blanc = 'Blanc'
equipe_noir = 'Noir'

# Fonction pour créer une disposition aléatoire des pièces avec des équipes
def generer_disposition_aleatoire():
    disposition = [['' for _ in range(echiquier_colonnes)] for _ in range(echiquier_lignes)]
    equipe = [['' for _ in range(echiquier_colonnes)] for _ in range(echiquier_lignes)]
    pieces_placees = 0

    while pieces_placees < 10:
        i, j = random.randint(0, echiquier_lignes - 1), random.randint(0, echiquier_colonnes - 1)

        if disposition[i][j] == '':
            piece = random.choice(types_pieces)
            disposition[i][j] = piece

            # Définir la couleur de l'équipe en fonction de la couleur de la case
            equipe[i][j] = equipe_blanc if (i + j) % 2 != 0 else equipe_noir

            pieces_placees += 1

    return disposition, equipe

# Fonction pour afficher l'échiquier avec matplotlib
def afficher_echiquier(disposition, equipe):
    # Vérifier s'il y a des pièces sur l'échiquier
    if not any(piece for ligne in disposition for piece in ligne):
        print("Il n'y a pas de pièces d'échecs à afficher.")
        return

    fig, ax = plt.subplots()
    ax.set_aspect('equal')

    for i in range(echiquier_lignes):
        for j in range(echiquier_colonnes):
            couleur_case = couleur_case_blanche if (i + j) % 2 == 0 else couleur_case_noire
            ax.add_patch(plt.Rectangle((j, i), 1, 1, color=couleur_case))

            piece = disposition[i][j]
            if piece:
                couleur_piece = 'black' if equipe[i][j] == equipe_noir else 'white'
                ax.text(j + 0.5, i + 0.5, formes_pieces[piece], color=couleur_piece,
                        fontsize=20, fontweight='bold', ha='center', va='center')

    ax.set_xlim(0, echiquier_colonnes)
    ax.set_ylim(0, echiquier_lignes)
    ax.set_xticks(np.arange(0.5, echiquier_colonnes, 1))
    ax.set_yticks(np.arange(0.5, echiquier_lignes, 1))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    plt.grid(False)  # Désactiver les lignes de la grille

    # Fonction appelée lors d'un clic de souris
    def on_click(event):
        if event.inaxes is not None:
            i, j = int(event.ydata), int(event.xdata)
            piece = disposition[i][j]

            # Vérifier si la case cliquée contient une pièce
            if piece:
                equipe_piece = equipe[i][j]
                print(f"Vous avez cliqué sur la case ({i}, {j}) contenant la pièce : {piece} de l'équipe : {equipe_piece}")
            else:
                print(f"La case ({i}, {j}) ne contient aucune pièce.")

    # Charger le modèle BERT pré-entraîné et le tokenizer
    model = BertForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=len(types_pieces))
    tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

    # Fonction pour effectuer la classification de texte avec BERT
    def classifier_piece(description):
        inputs = tokenizer(description, return_tensors="pt")
        outputs = model(**inputs)
        logits = outputs.logits
        predicted_label = torch.argmax(logits, dim=1).item()
        return types_pieces[predicted_label]

    # Fonction appelée lors d'un clic de souris
    def on_click(event):
        if event.inaxes is not None:
            i, j = int(event.ydata), int(event.xdata)
            piece = disposition[i][j]

            # Vérifier si la case cliquée contient une pièce
            if piece:
                equipe_piece = equipe[i][j]
                print(
                    f"Vous avez cliqué sur la case ({i}, {j}) contenant la pièce : {piece} de l'équipe : {equipe_piece}")

                # Utiliser le modèle BERT pour classifier une description factice de la pièce
                description_factice = f"C'est une pièce d'échecs de type {piece}."
                predicted_type = classifier_piece(description_factice)
                print(f"Le modèle prédit que la pièce est de type : {predicted_type}")

            else:
                print(f"La case ({i}, {j}) ne contient aucune pièce.")

    # ... (le reste du code reste inchangé)

    # Générer une disposition aléatoire des pièces avec des équipes et un maximum de 10 pièces
    disposition_aleatoire, equipe_aleatoire = generer_disposition_aleatoire()

    # Afficher l'échiquier avec matplotlib
    afficher_echiquier(disposition_aleatoire, equipe_aleatoire)"""
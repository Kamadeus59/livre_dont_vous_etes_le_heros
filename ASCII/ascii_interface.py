
import re

def creer_encadre(texte, largeur):
    '''
    Crée un encadré ASCII autour du texte donné avec la largeur spécifiée.
    '''
    texte_visible = re.sub(r'\033\[[0-9;]*m', '', texte)
    espaces = largeur - 2 - len(texte_visible)

    gauche = espaces // 2
    droite = espaces - gauche

    haut = "╭" + "─" * (largeur - 2) + "╮"
    milieu = "│" + " " * gauche + texte + " " * droite + "│"
    bas = "╰" + "─" * (largeur - 2) + "╯"

    return [haut, milieu, bas]


def afficher_menu():
    '''
    Affiche le menu principal du jeu.
    '''

    map_box = creer_encadre("\033[36mMAP ( M )\033[0m", 18)
    action_possible_box = creer_encadre("\033[32mACTION POSSIBLE ( A )\033[0m", 54)
    deplacement_box = creer_encadre("\033[31mSE DEPLACER ( D )\033[0m", 54)
    inventaire_box = creer_encadre(" \033[38;5;94mINVENTAIRE ( I )\033[0m", 24)

    # Affiche ACTION POSSIBLE au-dessus des autres encadrés.
    for i in range(3):
        print(" " * 22 + action_possible_box[i])

    # Affiche les trois autres encadrés côte à côte.
    for i in range(3):
        print(
            map_box[i] + "    " +
            deplacement_box[i] + "    " +
            inventaire_box[i]
        )

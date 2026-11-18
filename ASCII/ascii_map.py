import os
import sys

VERSION_SIMPLE = "="
def couleurs_disponibles() -> bool:
    """True si le terminal sait afficher les couleurs ANSI."""
    res = False
    if not os.environ.get("NO_COLOR") and sys.stdout.isatty():
        if os.name == "nt":
            os.system("")   # active les couleurs ANSI dans la console Windows
        res = True
    return res

def couleurs():
    '''
    Retourne un dictionnaire associant les couleurs aux codes ANSI correspondants.
    '''
    dictionnaire_couleur = { 
        1 : "\033[41m  \033[0m",
        2 : "\033[42m  \033[0m",
        3 : "\033[44m  \033[0m",
        4 : "\033[43m  \033[0m",
        5 : "\033[48;5;94m  \033[0m",
        6 : "\033[45m  \033[0m",
        7 : "\033[46m  \033[0m",
        8 : "\033[38;5;208m✖ \033[0m"
    }
    return dictionnaire_couleur

def afficher_map(carte):
    '''
    Affiche la carte du jeu.
    '''
    for ligne in carte:
        for case in ligne:
            print(couleurs().get(case, "  "), end="")
        print()

def ascii_map(position) -> None:
    """
    Affiche la map complete si le PC le permet, une version simplifié sinon
    """
    carte = [
    [3,3,3,3,3,3,3,3,3,3,3,3,3,3],
    [3,3,3,4,4,4,4,4,4,4,4,3,3,3],
    [3,3,4,2,2,2,2,2,2,2,2,4,3,3],
    [3,4,2,2,2,5,5,5,2,2,2,2,4,3],
    [3,4,2,2,5,5,5,5,5,2,2,2,4,3],
    [3,4,2,2,5,5,6,5,5,5,2,2,2,3],
    [3,4,2,2,2,5,6,6,5,2,2,7,2,3],
    [3,4,2,2,2,2,5,6,5,2,7,7,2,3],
    [3,4,2,2,2,2,2,5,2,2,2,7,2,3],
    [3,3,4,2,2,1,1,2,2,2,2,2,4,3],
    [3,3,4,2,1,1,1,1,2,2,2,4,3,3],
    [3,3,3,4,2,2,1,2,2,4,4,3,3,3],
    [3,3,3,3,4,4,4,4,4,4,3,3,3,3],
    [3,3,3,3,3,3,3,3,3,3,3,3,3,3]
    ]
    terrain_case = 3
    for i in range(len(carte)):
        for j in range(len(carte[i])):
            if j == 8: 
                if (i,j) == position:
                    print("Vous êtes toujours au meme endroit")
                    carte[i][j] == terrain_case 
                
    terrain_case = carte[position[0]][position[1]]
    carte[position[0]][position[1]] = 8
    if couleurs_disponibles():
        print()
        afficher_map(carte)
        print()
    else:
        print(VERSION_SIMPLE)


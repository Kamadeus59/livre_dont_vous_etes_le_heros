import os
import sys
from histoire_A12 import menu

gameState = menu.menu()

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
    [3,3,4,2,2,8,1,2,2,2,2,2,4,3],
    [3,3,4,2,1,1,1,1,2,2,2,4,3,3],
    [3,3,3,4,2,2,1,2,2,4,4,3,3,3],
    [3,3,3,3,4,4,4,4,4,4,3,3,3,3],
    [3,3,3,3,3,3,3,3,3,3,3,3,3,3]
]

case = 1
verif = 0
position = gameState["position"]
for i in range(len(carte)):
    for j in range(len(carte[i])):
        if j == 8:
            if (i,j) == position:
                print("Vous êtes toujours au meme endroit")
                carte[i,j] == case 
                
case = carte[position[0]][position[1]]
carte[position[0]][position[1]] = 8






VERSION_SIMPLE = "="

ROUGE  = "\033[41m  \033[0m"
VERT   = "\033[42m  \033[0m"
BLEU   = "\033[44m  \033[0m"
JAUNE  = "\033[43m  \033[0m"
MARRON = "\033[48;5;94m  \033[0m"
VIOLET = "\033[45m  \033[0m"
CYAN   = "\033[46m  \033[0m"
ORANGE = "\033[48;5;208m  \033[0m"

def couleurs_disponibles() -> bool:
    """True si le terminal sait afficher les couleurs ANSI."""
    res = False
    if not os.environ.get("NO_COLOR") and sys.stdout.isatty():
        if os.name == "nt":
            os.system("")   # active les couleurs ANSI dans la console Windows
        res = True
    return res

COULEURS = {
    1: ROUGE,
    2: VERT,
    3: BLEU,
    4: JAUNE,
    5: MARRON,
    6: VIOLET,
    7: CYAN,
    8: ORANGE 
}

def afficher_map():
    for ligne in carte:
        for case in ligne:
            print(COULEURS.get(case, "  "), end="")
        print()

def ascii_map() -> None:
    """Affiche la map complete si le PC le permet, une version simplifié sinon"""
    if couleurs_disponibles():
        print(2)
        afficher_map()
        print()
    else:
        print(VERSION_SIMPLE)


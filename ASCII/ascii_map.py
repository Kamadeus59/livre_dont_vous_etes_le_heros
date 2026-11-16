import os
import sys
from histoire_A12 import menu

carte = [1,1,2,1,3,1,1,3,3,2,3]

VERSION_SIMPLE = "="

ROUGE = "\033[41m  \033[0m"
VERT = "\033[42m  \033[0m"
BLEU = "\033[44m  \033[0m"

def couleurs_disponibles() -> bool:
    """True si le terminal sait afficher les couleurs ANSI."""
    res = False
    if not os.environ.get("NO_COLOR") and sys.stdout.isatty():
        if os.name == "nt":
            os.system("")   # active les couleurs ANSI dans la console Windows
        res = True
    return res

def afficher_map():
    for case in carte:
        if case == 1:
            print(ROUGE, end="")
        elif case == 2:
            print(VERT, end="")
        elif case == 3:
            print(BLEU, end="")

def ascii_map() -> None:
    """Affiche la map complete si le PC le permet, une version simplifié sinon"""
    if couleurs_disponibles():
        print()
        afficher_map()
        print()
    else:
        print(VERSION_SIMPLE)
    return 2


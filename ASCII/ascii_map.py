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
        1: "\033[41m  \033[0m",       # Lave ( Rouge ) 
        2: "\033[48;5;22m  \033[0m",  # Forêt ( Vert foncé )
        3: "\033[48;5;40m  \033[0m",  # Plaine ( Vert clair )
        4: "\033[43m  \033[0m",       # Désert ( Jaune )
        5: "\033[48;5;94m  \033[0m",  # Cratère / Pont ( Marron )
        6: "\033[48;5;208m  \033[0m", # Village ( Orange )
        7: "\033[46m  \033[0m",       # Rivière ( Cyan )
        8: "\033[38;5;208m✖ \033[0m", # Joueur ( Croix )
        9: "\033[47m  \033[0m",       # Neige ( Blanc )
        10: "\033[48;5;240m  \033[0m", # Roche ( Gris foncé )
        11: "\033[44m  \033[0m", # Lac gelé ( Bleu )
        12: "\033[40m  \033[0m", # Lac gelé ( Bleu )
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
    '''carte = [
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 9, 9, 9],
    [2, 2, 2, 2, 2, 2, 2, 9, 9, 9, 9, 9],
    [2, 2, 2, 2, 10, 10, 10, 9, 9, 9, 9, 9],
    [2, 2, 2, 10, 5, 5, 5, 10, 9, 9, 9, 9],
    [2, 2, 10, 5, 5, 5, 5, 5, 10, 4, 4, 4],
    [2, 2, 10, 5, 5, 5, 5, 5, 10, 4, 4, 4],
    [2, 2, 2, 10, 5, 5, 5, 10, 4, 4, 4, 4],
    [2, 2, 2, 2, 10, 10, 10, 4, 4, 4, 4,4],
    [2, 2, 2, 2, 2, 3, 3, 4, 1, 4, 1, 4],
    [2, 2, 2, 2, 3, 3, 3, 4, 1, 1, 1, 4],
    [2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 4],
    ]'''

    carte = [
        [12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12],
        [12, 2, 2, 2, 9, 9, 11, 11, 9, 9, 3, 3, 3, 12],
        [12, 2, 2, 2, 9, 9, 11, 11, 9, 9, 3, 3, 3, 12],
        [12, 6, 6, 2, 9, 9, 9, 9, 9, 3, 3, 3, 3, 12],
        [12, 6, 6, 2, 2, 9, 9, 9, 6, 6, 3, 3, 3, 12],
        [12, 6, 2, 2, 2, 10, 10, 10, 6, 6, 6, 3, 3, 12],
        [12, 2, 2, 2, 10, 5, 5, 5, 10, 6, 6, 3, 3, 12],
        [12, 2, 7, 7, 10, 5, 5, 5, 10, 4, 4, 4, 4, 12],
        [12, 7, 7, 3, 3, 10, 10, 10, 4, 4, 4, 4, 4, 12],
        [12, 3, 3, 3, 3, 3, 7, 7, 4, 4, 4, 4, 1, 12],
        [12, 6, 6, 3, 3, 5, 5, 5, 4, 4, 4, 1, 1, 12],
        [12, 6, 6, 6, 3, 3, 7, 4, 4, 4, 1, 1, 1, 12],
        [12, 6, 6, 6, 3, 7, 7, 4, 4, 4, 4, 1, 1, 12],
        [12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12]
        ]

    
    terrain_case : int = 3
    for i in range(len(carte)):
        for j in range(len(carte[i])):
            if j == 8: 
                if (i,j) == position:
                    print("Vous êtes toujours au meme endroit")
                    carte[i][j] == terrain_case 
                
    terrain_case = carte[position[1]][position[0]]
    carte[position[1]][position[0]] = 8
    if couleurs_disponibles():
        print()
        afficher_map(carte)
        print()
    else:
        print(VERSION_SIMPLE)
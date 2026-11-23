import os
import sys

VERSION_SIMPLE = "PAS DE CARTE"


def couleurs_disponibles() -> bool:
    '''
    Vérifie si le terminal permet d'afficher les couleurs ANSI.
    Retourne True si les couleurs sont disponibles, False sinon.
    '''
    res = False

    # Vérifie que les couleurs ne sont pas désactivées et que la sortie est un terminal.
    if not os.environ.get("NO_COLOR") and sys.stdout.isatty():

        # Sous Windows, active la prise en charge des couleurs ANSI.
        if os.name == "nt":
            os.system("")

        res = True

    return res


def couleurs():
    '''
    Retourne un dictionnaire associant chaque type de terrain
    à son code ANSI permettant de l'afficher avec une couleur.
    Chaque nombre correspond à un type de terrain précis.
    '''
    dictionnaire_couleur = {
        1: "\033[41m  \033[0m",        # Lave (Rouge)
        2: "\033[48;5;22m  \033[0m",   # Forêt (Vert foncé)
        3: "\033[48;5;40m  \033[0m",   # Plaine (Vert clair)
        4: "\033[43m  \033[0m",        # Désert (Jaune)
        5: "\033[48;5;94m  \033[0m",   # Cratère / Pont (Marron)
        6: "\033[48;5;208m  \033[0m",  # Village (Orange)
        7: "\033[46m  \033[0m",        # Rivière (Cyan)
        8: "\033[38;5;208m✖ \033[0m",  # Joueur (Croix)
        9: "\033[47m  \033[0m",        # Neige (Blanc)
        10: "\033[48;5;240m  \033[0m", # Roche (Gris foncé)
        11: "\033[44m  \033[0m",       # Lac gelé (Bleu)
        12: "\033[40m  \033[0m",       # Bordure (Noir)
    }

    return dictionnaire_couleur


def legende_map():
    '''
    Affiche une carte représentant les différents types de terrains
    ainsi qu'une légende associant chaque couleur à sa signification.
    '''

    # Création d'une carte composée de nombres correspondant aux terrains.
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

    # Liste des descriptions associées aux différentes couleurs.
    legende = [
        "\033[41m  \033[0m : Rouge = Lave (zone dangereuse).",
        "\033[48;5;22m  \033[0m : Vert foncé = Forêt.",
        "\033[48;5;40m  \033[0m : Vert clair = Plaine.",
        "\033[43m  \033[0m : Jaune = Désert.",
        "\033[48;5;94m  \033[0m : Marron = Cratère ou pont.",
        "\033[48;5;208m  \033[0m : Orange = Village.",
        "\033[46m  \033[0m : Cyan = Rivière.",
        "\033[38;5;208m✖ \033[0m : Croix violette = Votre position.",
        "\033[47m  \033[0m : Blanc = Neige.",
        "\033[48;5;240m  \033[0m : Gris foncé = Roche.",
        "\033[44m  \033[0m : Bleu = Lac gelé."
    ]

    print()

    # Parcourt les lignes de la carte sans afficher les bordures extérieures.
    for i in range(1, len(carte)-1):

        # Affiche la carte et sa légende côte à côte.
        if i <= len(legende):

            # Affiche chaque case de la ligne avec sa couleur correspondante.
            for case in carte[i]:
                print(couleurs().get(case, "  "), end="")

            # Ajoute des espaces pour séparer la carte de la légende.
            for j in range(50):
                print(" ", end="")

            # Affiche la description correspondant à la ligne actuelle.
            print(legende[i-1])

        else:
            # Affiche uniquement la carte si aucune légende ne correspond.
            for case in carte[i]:
                print(couleurs().get(case, "  "), end="")

    print()
    print()


def afficher_map(carte):
    '''
    Affiche la carte du jeu dans le terminal.

    Parcourt chaque ligne et chaque case de la carte afin de
    représenter les différents terrains avec leurs couleurs ANSI.
    '''

    # Parcourt toutes les lignes de la carte.
    for ligne in carte:

        # Parcourt chaque case de la ligne et affiche sa couleur.
        for case in ligne:
            print(couleurs().get(case, "  "), end="")

        # Passe à la ligne suivante après avoir affiché toute la ligne.
        print()


def ascii_map(position) -> None:
    '''
    Affiche la carte complète du jeu en couleurs ANSI si le terminal
    le permet. Sinon, affiche une version simplifiée.

    La position du joueur est utilisée pour placer une croix sur
    la carte à l'endroit où se trouve actuellement le joueur.
    '''

    # Création de la carte avec les différents types de terrains.
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

    # Définit le type de terrain sur lequel se trouve initialement le joueur.
    case_sur_laquelle_est_le_joueur: int = 3

    # Enregistre le terrain sous le joueur avant de placer son symbole.
    carte[position[1]][position[0]] = case_sur_laquelle_est_le_joueur

    # Récupère le terrain sur lequel se trouve le joueur.
    terrain_case = carte[position[1]][position[0]]

    # Remplace temporairement le terrain par le symbole du joueur.
    carte[position[1]][position[0]] = 8

    # Vérifie si le terminal permet l'affichage des couleurs ANSI.
    if couleurs_disponibles():

        # Affiche la carte complète en couleurs.
        print()
        afficher_map(carte)
        print()

    else:
        # Affiche une version simplifiée si les couleurs ne sont pas disponibles.
        print(VERSION_SIMPLE)
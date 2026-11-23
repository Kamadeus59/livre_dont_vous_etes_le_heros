'''
Version finale de la page 1, à mettre lorsqu'on rend le projet
'''


from OUTILS import map
from OUTILS import couleurs_disponibles
from OUTILS import affichage_texte
from OUTILS.interface import interface
import os


def page1(gameState: dict) -> int:
    """
    Affiche la présentation du jeu.
    """
    os.system("cls")
    couleurs_disponibles.couleurs_disponibles()
    texte = [
        "Mes hommages cher voyageur ! Que me vaut le plaisir de votre visite ?",
         "Vous cherchez quelque chose qui remplirait votre soif d'aventure ?",
         "Dans ce cas là vous êtes au bon endroit"
         ""
        ]
    affichage_texte.affichage_texte(texte)
    nom: str = input("Quel est votre nom ? ")
    gameState["nom"] = nom
    texte1 = [
        f"Bienvenue, \033[31m{nom}\033[0m. Vous entrez dans le monde merveilleux de Freldia !",
        "Êtes-vous prêt pour l'aventure ?",
        "Car c'est parti !",
        "Dans un premier temps, voici la carte du monde de Freldia.",
        ]
    affichage_texte.affichage_texte(texte1)
    map.afficher_map_legend(gameState),
    texte2 = [
        "Vous êtes actuellement sur la case \033[35mreprésenté par une croix\033[0m, qui est votre point de départ.",
        "Chaque case correspond à une zone que vous pouvez explorer.",
        "Déplacez-vous pour découvrir les différentes régions de la carte !",
        "",
        "Voici l'interface",
        ""
        ]
    affichage_texte.affichage_texte(texte2)
    interface()
    texte3 = [
        "Elle vous permet de vous déplacez ainsi que d'ouvrir votre inventaire ou bien la map du monde :",
        "Ainsi vous pouvez ouvrir votre \033[36mmap\033[0m en appuyant sur la touche \033[31mM\033[0m",
        "Vous pouvez ouvrir votre \033[31mmenu de déplacement\033[0m en appuyant sur la touche \033[31mD\033[0m",
        "Et enfin vous pouvez ouvrir votre \033[38;5;94minventaire\033[0m en appuyant sur la touche \033[31mI\033[0m",
        "Votre introduction à ce monde merveilleux est maintenant terminé",
        "Pour commencer votre aventure, veuillez appuyer sur la touche entrée de votre clavier"
    ]
    affichage_texte.affichage_texte(texte3)
    input("")
        
    res = 1001

    return res

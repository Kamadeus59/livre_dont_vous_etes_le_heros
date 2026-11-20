from OUTILS import map
from OUTILS import couleurs_disponibles
from OUTILS import affichage_texte


def page1(gameState: dict) -> int:
    """
    Affiche la présentation du jeu.
    """
    couleurs_disponibles.couleurs_disponibles()
    map.afficher_map(gameState)
    nom: str = input("Quel est votre nom ? ")
    texte1 = [
        f"Bienvenue, \033[31m{nom}\033[0m. Vous entrez dans le monde merveilleux de Freldia !",
        "Êtes-vous prêt pour l'aventure ?",
        "Car c'est parti !",
        "Dans un premier temps, voici la carte du monde de Freldia.",
        ]
    affichage_texte.affichage_texte(texte1)
    map.afficher_map(gameState),
    texte2 = [
        "Vous êtes actuellement sur la case \033[31mreprésenté par une croix\033[0m, qui est votre point de départ."
        ]
    affichage_texte.affichage_texte(texte2)
    

        
    res = 1001

    return res

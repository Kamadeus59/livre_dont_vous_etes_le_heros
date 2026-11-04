"""
Fonctions annexes pour les combats.

Ces fonctions ne décident JAMAIS de la page suivante : elles retournent
une information (ici True / False) et c'est la page qui choisit la suite.

Pour les utiliser dans une page :
    from OUTILS.combat import combat_dragon
"""


def combat(gameState: dict, monstre: dict) -> bool:
    """
    Combat générique entre le héros et un monstre.

    gameState : le dictionnaire du jeu (contient "vie" et "force" du héros)
    monstre   : un dictionnaire avec les clés "nom", "vie" et "force"

    Retourne True si le héros gagne, False s'il perd.
    Les points de vie du héros perdus pendant le combat sont retirés
    de gameState["vie"].
    """
    res: bool = False

    # A IMPLEMENTER

    return res


def combat_dragon(gameState: dict) -> bool:
    """Combat contre un dragon. Retourne True si le héros gagne."""
    monstre: dict = {"nom": "dragon", "vie": 20, "force": 4}
    res: bool = combat(gameState, monstre)
    return res


def combat_orc(gameState: dict) -> bool:
    """Combat contre un orc. Retourne True si le héros gagne."""
    monstre: dict = {"nom": "orc", "vie": 8, "force": 2}
    res: bool = combat(gameState, monstre)
    return res

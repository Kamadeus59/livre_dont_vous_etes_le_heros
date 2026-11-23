'''
Version de la page 1 pour les tests
'''


def page1(gameState: dict) -> int:
    """
    Affiche la présentation du jeu.
    """
    nom: str = input("Quel est votre nom ? ")
    gameState["nom"] = nom
    
    res = 1001

    return res

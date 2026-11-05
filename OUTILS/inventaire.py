def ouvrir_inventaire(gameState : dict) -> dict:
    """
    Ouvre l'inventaire du héros et permet de l'utiliser.

    gameState : le dictionnaire du jeu (contient "inventaire" et "vie" du héros)

    Retourne le dictionnaire gameState mis à jour.
    """
    res: list = gameState["inventaire"]
    return res

    # A IMPLEMENTER
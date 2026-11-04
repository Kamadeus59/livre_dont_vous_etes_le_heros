def page1(gameState: dict) -> int:
    res: int = -2                     # par défaut : cas non prévu

    print(f"{gameState['nom']}, vous êtes à l'entrée d'une grotte.")
    print("Une épée rouillée traîne au sol.")
    print("1 - Prendre l'épée   2 - Entrer directement")
    choix: str = input("> ")

    if choix == "1":
        gameState["inventaire"].append("épée")
        gameState["force"] = gameState["force"] + 3
        print(f"Votre force passe à {gameState['force']}.")
        res = 2
    elif choix == "2":
        res = 2
    else:
        print("Choix invalide.")
        res = 1                  # on reste sur cette page

    return res

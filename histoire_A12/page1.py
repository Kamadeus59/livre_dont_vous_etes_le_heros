def page1(gameState: dict) -> int:
    res: int = -2                     # par défaut : cas non prévu

    print(f"{gameState['nom']}, vous êtes à l'entrée d'une grotte.")
    print("Quel type d'arme choisis tu")
    print("1 - Une épée rouillée \n2 - Un arc avec une ficelle lache \n3 - Une lance a moitié brisée   ")
    choix: str = input("> ")

    if choix == "i":   
        for i in gameState: 
            print (i, ":", gameState[i])
        res = 1   

    if choix == "1":
        gameState["inventaire"].append("épée rouillée")
        gameState["force"] = gameState["force"] + 3
        print(f"Votre force passe à {gameState['force']}.")
        res = 2
    elif choix == "2":
        gameState["inventaire"].append("arc en bois")
        gameState["force"] = gameState["force"] + 1
        gameState["portée"] = gameState["portée"] + 3
        print(f"Votre force passe à {gameState['force']}.")
        print(f"Votre force passe à {gameState['portée']}.")
        res = 2
    elif choix == "3":
        gameState["inventaire"].append("lance a moitié brisée")
        gameState["force"] = gameState["force"] + 3
        gameState["portée"] = gameState["portée"] + 1
        print(f"Votre force passe à {gameState['force']}.")
        print(f"Votre force passe à {gameState['portée']}.")
        res = 2
    
    else:
        print("Choix invalide.")
        res = 1                  # on reste sur cette page

    return res

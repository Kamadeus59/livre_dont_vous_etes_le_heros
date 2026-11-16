from OUTILS import map

def page1(gameState: dict) -> int:
    res = -2
    print("test 1")
    a = int(input("Que voulez vous fare ?"))
    print("test 2")
    print("Tu as choisi :", a)
    if a == 1:
        print("0")
        map.afficher_map(gameState)
    b = int(input("Nouvelle position X ?"))
    c = int(input("Nouvelle position Y ?"))
    gameState["position"] = (b,c)
    map.afficher_map(gameState)

    res = 1

        
    return res
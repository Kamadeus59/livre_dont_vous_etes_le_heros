
from ASCII import ascii_map 


def afficher_map(gameState : dict) -> dict:
    '''
    Affiche la map du jeu.
    '''
    ascii_map.ascii_map(gameState["position"])

    res: list = gameState["inventaire"]
    return res

def move(gameState : dict,originalTile) -> list:
    '''
    Permet de déplacer le joueur sur la map.
    '''
    validAnswer = False
    Xdeplacement = 0
    Ydeplacement = 0
    print("Nord : N   Sud : S")
    print("Est : E    Ouest : O")
    while not validAnswer:
        
        direction = input("Par où allez vous ?")
        validAnswer = True
        if direction == "N" or direction=="n":
            Ydeplacement = -1
        elif direction == "S" or direction=="s":
            Ydeplacement = 1
        elif direction == "E" or direction=="e":
            Xdeplacement = 1
        elif direction == "O" or direction=="o":
            Xdeplacement = -1
        else:
            validAnswer = False

    res : int = -2
    position : tuple= gameState["position"]
    map : list= gameState["map"]
    newPosition : tuple= (position[0]+Xdeplacement, position[1]+Ydeplacement)
    Id : int = map[newPosition[1]][newPosition[0]]
    if Id == -1:
        res = originalTile
        print("Vous ne pouvez pas aller par là !")
    else:
        res = int(Id)
    print(position, newPosition)
    return res
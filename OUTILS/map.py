from OUTILS import affichage_texte
from ASCII import ascii_map 


def afficher_map(gameState : dict) -> dict:
    '''
    Affiche la map du jeu.
    '''
    ascii_map.ascii_map(gameState["position"])

    res: list = gameState["inventaire"]
    return res

def afficher_map_legend(gameState: dict):
    '''
    Affiche la map du jeu avec sa légende.
    '''
    ascii_map.legende_map()

def move(gameState : dict ,originalTile) -> list:
    gameState["ancienne position"] = gameState["position"]
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
        deplacement_reussi = False
        res = int(originalTile)
        print("Vous ne pouvez pas aller par là !")
    else:
        deplacement_reussi = True
        gameState["ID_map"] = Id
        gameState["position"]= newPosition
        res = int(Id)
    return res, deplacement_reussi

def narrateur(gameState):
    map_de_biomes = [
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
    noms_de_biomes_sortant = {
        2 : "une forêt",
        9 : "une région glaciale avec de la neige partout partout",
        11: "un lac gelé. Vous manquez de vous tauler",
        3: "une plaine",
        6 : "une ville",
        4 : "un désert",
        1 : "un lac de lave mais tu meurt pas parce quon la pas codé",
        5 : "un pont ou un cratère",
        7 : "une rivière"

    }
    noms_de_biomes_entrant = {
        2 : "la forêt",
        9 : "la région glaciale avec de la neige partout partout",
        11: "le lac gelé. Vous manquez de vous tauler",
        3: "la plaine",
        6 : "la ville",
        4 : "le désert",
        1 : "le lac de lave mais tu meurt pas parce quon la pas codé",
        5 : "le pont ou le cratère",
        7 : "la rivière"
    }


    print(gameState["ancienne position"])
    ancien_biome = noms_de_biomes_entrant[map_de_biomes[gameState["ancienne position"][1]][gameState["ancienne position"][0]]]
    nouveau_biome = noms_de_biomes_sortant[map_de_biomes[gameState["position"][1]][gameState["position"][0]]]

    print(f"Vous quittez {ancien_biome} et arrivez dans {nouveau_biome}")
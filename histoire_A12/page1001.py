from OUTILS.map import move
from OUTILS import interface
import os

def page1001(gameState: dict) -> int:
    res = -2

    os.system("cls") #permet de faire une séparation entre l'introduction et le début de la partie
    print("Bienvenue")
    interface.interface()
    action : str = ""
    while action != "D" and action != "d":
        action = str(input(""))
        if action == "I" or action == "i":
            interface.ouvrir_inventaire(gameState)
        elif action =="M" or action =="m":
            interface.ouvrir_map(gameState)
        elif action != "D" or action != "d":
            print("Appuyer sur une touche valable")
    
    res = move(gameState,gameState["ID_map"])
    return res
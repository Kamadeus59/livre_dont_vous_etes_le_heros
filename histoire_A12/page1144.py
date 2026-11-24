
from OUTILS.map import *
from OUTILS import interface
import os

def page1144(gameState: dict) -> int:
    res = -2

    os.system("cls") #permet de faire une séparation entre l'introduction et le début de la partie
    interface.interface()
    action : str = ""

    narrateur(gameState)


    interface_fonctionne = True
    while interface_fonctionne:
        action = str(input(""))
        if action == "I" or action == "i":
            interface.ouvrir_inventaire(gameState)
        elif action =="M" or action =="m":
            interface.ouvrir_map(gameState)
        elif action == "D" or action == "d":
            res, deplacement_reussi = move(gameState,gameState["ID_map"])
            if deplacement_reussi:
                interface_fonctionne = False
        else:
            print("Appuyer sur une touche valable")
    
    return res

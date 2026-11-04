from ASCII.ascii_dragon import ascii_dragon
from OUTILS.combat import combat_dragon


def page2(gameState: dict) -> int:
    res: int = -2                     # par défaut : cas non prévu

    ascii_dragon()
    print("Un dragon surgit et vous barre la route !")

    if "épée" in gameState["inventaire"]:
        res=0
    else:
        print("Vous ne faites pas le poids... Le dragon l'emporte.")
        res = -1

    return res

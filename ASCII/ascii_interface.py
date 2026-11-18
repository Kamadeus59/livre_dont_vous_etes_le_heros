def creer_encadre(texte, largeur):
    haut = "╭" + "─" * (largeur - 2) + "╮"
    milieu = "│" + texte.center(largeur - 2) + "│"
    bas = "╰" + "─" * (largeur - 2) + "╯"

    return [haut, milieu, bas]


def afficher_menu():
    map_box = creer_encadre("MAP", 18)
    deplacement_box = creer_encadre("SE DEPLACER", 54)
    inventaire_box = creer_encadre("INV", 22)
    for i in range(3):
        print(
            map_box[i] + "    " +
            deplacement_box[i] + "    " +
            inventaire_box[i]
        )


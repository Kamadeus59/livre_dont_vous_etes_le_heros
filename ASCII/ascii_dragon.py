"""
Exemple de dessin ASCII simple.

Pour créer votre propre dessin :
  1. copiez ce fichier dans le dossier ASCII sous le nom ascii_quelquechose.py ;
  2. renommez la fonction ascii_quelquechose (même nom que le fichier) et
     gardez le typage : def ascii_quelquechose() -> None ;
  3. collez votre dessin entre les triple guillemets.

Le r placé juste avant les triple guillemets du print est important :
sans lui, Python interprète mal les barres obliques inversées du dessin.

Pour l'utiliser dans une page :
    from ASCII.ascii_dragon import ascii_dragon
    ascii_dragon()
"""


def ascii_dragon() -> None:
    print(r"""
                             /\   /\
                            /  \_/  \_______
               /\          |   (o)          \__
              /  \         |           ______  >
             / /\ \        |          / vvvvv /    ~~~~~~
            / /  \ \____    \        |       <   ~~~~~~~~~~
           / /    \     \____\        \ ^^^^^ \    ~~~~~~
          /_/  /\  \          \        \_______\
              /  \  \          \          |
             /    \  \__________\         |
            /______\         /   \         \
                            /     \_________\
                           /__/\__\     /__/\__\
""")


if __name__ == "__main__":
    ascii_dragon()   # pour tester le dessin seul : python ASCII/ascii_dragon.py

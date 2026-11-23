import time

def affichage_texte(texte: str) -> None:
    """
    Affiche le texte caractère par caractère avec un délai.
    """
    for phrase in texte:
        for mot in phrase.split():
            for caractere in mot:
                print(caractere, end="", flush=True)
                time.sleep(0)
            print(" ", end="", flush=True)
            if mot[-1] in [".", "!", "?"]:
                time.sleep(0)
            time.sleep(0)
        print()
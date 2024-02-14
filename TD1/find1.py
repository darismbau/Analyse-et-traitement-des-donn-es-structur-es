import os.path
import sys

def start_find1():
    """

    :return:
    """
    if len(sys.argv) <= 1:
        print(f"Il n'y a pas assez d'argument dans le programme {sys.argv[0]}")
    else:
        if not os.path.exists(sys.argv[1]):
           aide()
        else:
            affiche(sys.argv[1])


def affiche(d):
    """

    :param d:
    :return:
    """
    for elt in os.listdir(d):
        print(elt)

def aide():
    print("Le dossier n'existe pas dans le dossier courant")
    print("Erreur d'utilisation du script find1.py")
    #print(help(start_find1))
    print('Vous devez ajouter un nom de repertoire par exemple : find1.py C:\ temp ')

if __name__ == '__main__':
    start_find1()
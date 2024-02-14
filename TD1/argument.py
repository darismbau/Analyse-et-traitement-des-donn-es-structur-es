import sys


if __name__ == '__main__':
    if len(sys.argv) == 1 :
        print(f"Pas assez d'argument pour le script {sys.argv[0]}")
    else:
        for elt in sys.argv:
            print(elt)
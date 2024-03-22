from Rectangle import *
from Carree import *
if __name__ == '__main__':
    rect = Rectangle(10, 5)
    print(rect.get_area())
    rect.height = 3
    print(rect.get_perimeter())
    print(rect)
    print(rect.get_picture())

    sq = Carree(9)
    print(sq.get_area())
    sq.side = 4
    print(sq.get_diagonal())
    print(sq)
    print(sq.get_picture())
    rect.height = 8
    rect.width = 16

#le nom qu'on donne au fivhier, c'est le nom de la classe, le mieux est d'avoir chaque classe par fichier,
#Init est le constructeur, permet de créer des instances.
#argument , sachant que les arguments peuvent avoir des valeurs par defaut
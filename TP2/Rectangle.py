class Rectangle:
    def __init__(self, width, height):  #Ici, j'initialise la rectangle créée avec les attributs width & height.
       self.__width = width                      #Je crée l'objet rectangle avec une largeur de ...
       self.__height = height

    def set_width(self, width):
        if width < 0:
            print("La valeur doit être positive")
    def set_height(self, height):
        if height < 0:
            print("La valeur doit être positive")
    def get_area (self):
        area = self.__width*self.__height
        print("The area is :", area)
    def get_perimeter(self):
        perimeter = (self.__width+self.__height+self.__width+self.__height)
        print("The perimeter is : ", perimeter)
    def get_diagonal(self):
        diagonal = ((self.__width**2+self.__height**2)**5)
        print("The Diagonal is :", diagonal)
    def get_picture(self):
        pic =""
        for i in range(self.__height):                                        #\n : permet de faire un retour à la ligne.
            print(self.__width * '*')
    #def get_amount_inside(self):



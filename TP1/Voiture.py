class Voiture:
    def __str__(self, m1,m2,c,p=10): # Ici on a attribué la valeur par defaut à P
        self.__marque = m1
        self.__modele = m2
        self.__puissance_fiscale = p
        self.__couleur = c

    def get_marque(self):
        return self.__marque

    def set_marque(self,v):
        self.__marque =v

from Rectangle import *

class Carree(Rectangle):
    def __init__(self, side = 1):
        super().__init__(side, side)                                                 # pour construire un carree, il faut juste passer 2 fois l'argument.
    def set_side(self,RT):
        super().set_width(RT)
        super().set_height(RT)
    def get_side(self,):
        return super().get_longueur()
    side = property (fget=get_side,fset=set_side)



import pygame
from Class_imagen import Imagen
class Plataforma(Imagen):
    def __init__(self,x,y,largo,ancho,path_imagen=-1):
        if type(path_imagen) == str:
            tamaño = largo,ancho
            origen = (x,y)
            super().__init__(tamaño,path_imagen)
            self.rectangulo.center = origen 
        else:
            self.rectangulo = pygame.Rect(x,y,largo,ancho)
        
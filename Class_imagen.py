import pygame
class Imagen:
    def __init__(self,tamaño,path_imagen):
        self.imagen = pygame.image.load(path_imagen)
        self.superficie = pygame.transform.scale(self.imagen,tamaño)
        self.rectangulo = self.superficie.get_rect()
        
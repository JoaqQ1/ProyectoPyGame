import pygame
from config import obtener_rectangulos

class Objeto_Juego:
    def __init__(self,path_img,tamaño_rect,pos_inicial):
        self.image = pygame.image.load(path_img)
        self.superficie = pygame.transform.scale(self.image,tamaño_rect)
        self.rect = self.superficie.get_rect()        
        self.rect.center = pos_inicial
        self.lados = obtener_rectangulos(self.rect)

    
    # def draw(screen,lista_de_objetos):
    #     screen.blit()
import pygame
from config import obtener_rectangulos

class Objeto_Juego:
    def __init__(self,path_img,tamaño_rect,pos_inicial):
        self.image = pygame.image.load(path_img)
        self.superficie = pygame.transform.scale(self.image,tamaño_rect)
        self.rect = self.superficie.get_rect()        
        self.rect.center = pos_inicial
        self.lados = obtener_rectangulos(self.rect)
        self.posicion_inicial = self.retornar_pos_inicial()

    def retornar_pos_inicial(self):
        posiciones = {}
        
        posiciones["mainx"] = self.lados["main"].x
        posiciones["mainy"] = self.lados["main"].y

        posiciones["topx"] = self.lados["top"].x
        posiciones["topy"] = self.lados["top"].y

        posiciones["bottomx"] = self.lados["bottom"].x
        posiciones["bottomy"] = self.lados["bottom"].y
        
        posiciones["rightx"] = self.lados["right"].x
        posiciones["righty"] = self.lados["right"].y

        posiciones["leftx"] = self.lados["left"].x
        posiciones["lefty"] = self.lados["left"].y
        return posiciones
    
    def draw(self,pantalla):
        pantalla.blit(self.superficie,self.lados["main"])




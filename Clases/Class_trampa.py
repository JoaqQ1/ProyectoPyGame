import pygame
from Clases.Class_objeto_juego import Objeto_Juego
class Trampa(Objeto_Juego):
    def __init__(self, path_img, tamaño_rect, pos_inicial,rango_mov):
        super().__init__(path_img, tamaño_rect, pos_inicial)
        self.velocidad = 15
        self.rango_mov = rango_mov
    def update(self,pantalla):
        self.draw(pantalla)
        for lado in self.lados:
            self.lados[lado].x +=  self.velocidad
        if self.lados["main"].centerx == self.rango_mov[1]:
            self.velocidad =  self.velocidad * -1
        elif self.lados["main"].centerx <= self.rango_mov[0]:
            self.velocidad = 15

            

    def draw(self,pantalla:pygame.Surface):                
        pantalla.blit(self.superficie,self.rect)
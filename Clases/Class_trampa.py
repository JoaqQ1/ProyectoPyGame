import pygame
from Clases.Class_objeto_juego import Objeto_Juego
from config import escalar_png
class Trampa(Objeto_Juego):
    def __init__(self, path_img, tamaño_rect, pos_inicial,rango_mov,lista_animaciones=""):
        super().__init__(path_img, tamaño_rect, pos_inicial)
        self.velocidad = 15
        self.rango_mov = rango_mov
        #######################################
        self.w = tamaño_rect[0]
        self.h = tamaño_rect[1]
        self.lista_animaciones = lista_animaciones
        self.tiene_animacion = False
        if self.lista_animaciones != "":
            escalar_png(self.lista_animaciones,(self.w,self.h))
            self.tiene_animacion = True
        self.frame_actual = 0
        #######################################


    def update(self,pantalla):
        if self.tiene_animacion != True:
            self.draw(pantalla)
        
            for lado in self.lados:
                self.lados[lado].x +=  self.velocidad
            if self.lados["main"].centerx == self.rango_mov[1]:
                self.velocidad =  self.velocidad * -1
            elif self.lados["main"].centerx <= self.rango_mov[0]:
                self.velocidad = 15
        else:  
            for lado in self.lados:
                self.lados[lado].y +=  self.velocidad
            if self.lados["main"].y == self.rango_mov[1] - 60:
                self.velocidad =  -15 
            elif self.lados["main"].y <= self.rango_mov[0]:
                self.velocidad = 15
            self.animar(pantalla)

            

    def draw(self,pantalla:pygame.Surface):                
        pantalla.blit(self.superficie,self.rect)

    
    def animar(self,pantalla:pygame.Surface):                                
        largo = len(self.lista_animaciones)                        
        if self.frame_actual >= largo:
            self.frame_actual = 0                   
        
        pantalla.blit(self.lista_animaciones[self.frame_actual],self.lados["main"])
        self.frame_actual += 1
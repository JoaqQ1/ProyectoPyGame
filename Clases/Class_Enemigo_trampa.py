import pygame
from Clases.Class_personaje import Personaje

class Enemigo_trampa(Personaje):
    def __init__(self, path_img, tamaño_rect, pos_inicial, animaciones, velocidad,rango_mov):
        super().__init__(path_img, tamaño_rect, pos_inicial, animaciones, velocidad)
        ####################
        self.muerto = False
        self.colisiono = False
        self.rango_mov = rango_mov
  
    def update(self,plataformas,pantalla:pygame.Surface,personaje):
        if self.lados["main"].colliderect(personaje.lados["main"]):
             personaje.golpeado = True
        for lado in self.lados:
            self.lados[lado].y +=  self.velocidad
        if self.lados["main"].y == self.rango_mov[1] - 60:
            self.velocidad =  -5 
        elif self.lados["main"].y <= self.rango_mov[0]-30:
                self.velocidad = 15
        
        self.animar(pantalla)
            

    def animar(self,pantalla:pygame.Surface):                                
        largo = len(self.animaciones)                        
        if self.frame_actual >= largo:
            self.frame_actual = 0                   
        
        pantalla.blit(self.animaciones[self.direccion]["quieto"][self.frame_actual],self.lados["main"])
        self.frame_actual += 1
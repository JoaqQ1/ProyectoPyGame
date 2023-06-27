import pygame
from config import escalar_png
from Clases.Class_objeto_juego import Objeto_Juego
from funciones import *


class Personaje(Objeto_Juego):
    def __init__(self, path_img, tamaño_rect, pos_inicial,animaciones,velocidad):
        super().__init__(path_img, tamaño_rect, pos_inicial)        
        # animacion
        self.ancho = tamaño_rect[0]
        self.alto = tamaño_rect[1]
        self.animaciones = animaciones
        self.frame_actual = 0
        self.rescalar_animaciones() 
        self.que_hace = "quieto"
        self.direccion = "derecha"

        #Movimiento
        self.velocidad = velocidad
        self.desplazamiento_y = 0
        #Gravedad
        self.gravedad = 1
        self.limite_velocidad_caida = 15
        self.capacidad_salto = -15
        self.saltando = False

        self.lanzar_proyectil = False
        self.lista_proyectiles = []

    def rescalar_animaciones(self):
        for clave in self.animaciones["izquierda"]:
            escalar_png(self.animaciones["izquierda"][clave],(self.ancho,self.alto))
        for clave in self.animaciones["derecha"]:
            escalar_png(self.animaciones["derecha"][clave],(self.ancho,self.alto))


    def mover_personaje(self,velocidad,ancho_pantalla):
        for lados in self.lados:
            if (self.lados[lados].x < 0 and velocidad < 0) or (self.lados[lados].x == ancho_pantalla - 100 and velocidad > 0):
                velocidad = 0

            self.lados[lados].x += velocidad
    

       
    
    def animar_personaje(self,pantalla:pygame.Surface):                                
        largo = len(self.animaciones[self.direccion][self.que_hace])                        
        if self.frame_actual >= largo:
            self.frame_actual = 0                   
        
        pantalla.blit(self.animaciones[self.direccion][self.que_hace][self.frame_actual],self.lados["main"])
        self.frame_actual += 1
    
    def aplicar_gravedad(self,pantalla:pygame.Surface,plataformas):
       
        if self.saltando:
            self.animar_personaje(pantalla)

            for lado in self.lados:                
                    self.lados[lado].y += self.desplazamiento_y

            if self.desplazamiento_y + self.gravedad <= self.limite_velocidad_caida:
                    self.desplazamiento_y += self.gravedad
        for lado in plataformas:
            if self.lados["bottom"].colliderect(lado["top"]):               
                self.desplazamiento_y = 0
                self.saltando = False
                self.lados["main"].bottom = lado["top"].top
                break
            else:
                self.saltando = True
            
                       


    def detectar_colision_con_pared(self,plataformas):
        if validar_lista(plataformas):
            for i in range(len(plataformas)):
                for pared in plataformas[i]:
                    if pared == "right" or pared == "left":
                        if self.lados["right"].colliderect(plataformas[i][pared]):
                            return 1 
                        elif self.lados["left"].colliderect(plataformas[i][pared]):
                            return -1

    
    def detectar_colision_con_proyectil(self,lista_proyectiles):
        for proyectil in lista_proyectiles:            
            if proyectil.rect.colliderect(self.lados["main"]):
                return  True
            else:
                return  False
    
    def shoot(self,pantalla,velocidad):
        for proyectil in self.lista_proyectiles:
            if proyectil.activo:
                proyectil.update(self,pantalla,velocidad,self.direccion)
            else:
                self.lista_proyectiles.remove(proyectil)
        




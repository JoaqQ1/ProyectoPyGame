import pygame
from Clases.Class_personaje import Personaje
from Clases.Class_proyectil import Proyectil


class Enemigo(Personaje):
    def __init__(self, path_img, tamaño_rect, pos_inicial, animaciones, velocidad):
        super().__init__(path_img, tamaño_rect, pos_inicial, animaciones, velocidad)
        self.muerto = False
        self.colisiono = False
        self.sonido_muere = pygame.mixer.Sound("sonidos/sRockReturn.ogg")


        

    def update(self,plataformas,pantalla,personaje):
        self.que_hace = "quieto" 
        
        #Seguimiento del personaje
        if personaje.lados["main"].x > self.lados["main"].x:
            self.direccion = "derecha"
        else:
            self.direccion = "izquierda"
        #ataque al personaje
        if self.lanzar_proyectil == False:
            if personaje.lados["bottom"].y >= self.lados["main"].centery:
                self.lanzar_proyectil = True
                proyectil = Proyectil("Proyectil/laser.png",(30,30),self.lados["main"].centerx,self.lados["main"].centery)       
                self.lista_proyectiles.append(proyectil)     
                self.que_hace = "atacando"
        
        self.shoot(pantalla,15)

        if self.detectar_colision_con_proyectil(personaje.lista_proyectiles):
            self.colisiono = True
        
        if self.colisiono  != True:
            self.animar_personaje(pantalla)
            self.aplicar_gravedad(pantalla, plataformas)
        else:
            self.sonido_muere.play()
            self.que_hace = "muriendo"
            self.animar_personaje(pantalla)
            ultima_animacion = len(self.animaciones[self.direccion][self.que_hace])
            if ultima_animacion == self.frame_actual:
                self.muerto = True
               
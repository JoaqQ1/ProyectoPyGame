import pygame
from Clases.Class_personaje import Personaje

class Enemigo_fantasma(Personaje):
    def __init__(self, path_img, tamaño_rect, pos_inicial, animaciones, velocidad,rango_mov):
        super().__init__(path_img, tamaño_rect, pos_inicial, animaciones, velocidad)
        ####################
        self.muerto = False
        self.colisiono = False
        self.rango_mov = rango_mov
        self.sonido_muere = pygame.mixer.Sound("sonidos/sonido_fantasma.mp3")
  
    def update(self,plataformas,pantalla:pygame.Surface,personaje):
        
        self.que_hace = "moviendose"
        w = pantalla.get_width()
        if self.lados["main"].x == self.rango_mov[0]+30:
            self.velocidad = 5
        elif self.lados["main"].x == self.rango_mov[1]:
            self.velocidad = self.velocidad * -1
        self.mover_personaje(self.velocidad,w)

        if self.colisiono_cabeza(personaje):
            personaje.desplazamiento_y = -15
            self.colisiono = True
            self.que_hace = "muriendo"
        
        if self.colisiono != True:
            self.animar_personaje(pantalla)
            self.aplicar_gravedad(pantalla,plataformas)
        elif self.colisiono:
            if self.estado_sonido:
                self.sonido_muere.play()
            self.que_hace = "muriendo"
            self.animar_personaje(pantalla)
            ultima_animacion = len(self.animaciones[self.direccion][self.que_hace])
            if ultima_animacion == self.frame_actual:
                self.muerto = True

    def colisiono_cabeza(self,personaje):
        if personaje.lados["bottom"].colliderect(self.lados["top"]):
            return True
        else:
            return False
import pygame
from Class_personaje import Personaje
from funciones import *
class Personaje_principal(Personaje):
    def __init__(self, path_img, tamaño_rect, pos_inicial, animaciones, velocidad):
        super().__init__(path_img, tamaño_rect, pos_inicial, animaciones, velocidad)
        self.score = 0
        self.vida = 3        


    def update(self,pantalla:pygame.Surface,plataformas,que_hace):
    
        match que_hace:
            case "derecha":  
                if not self.saltando:
                    self.animar_personaje(pantalla)
                if self.detectar_colision_con_pared(plataformas) != 1:
                    self.mover_personaje(self.velocidad)
                self.direccion = "derecha"
                self.que_hace = "corriendo"
            case "izquierda":
                if not self.saltando:
                    self.animar_personaje(pantalla)
                if self.detectar_colision_con_pared(plataformas) != -1:                      
                    self.mover_personaje(self.velocidad * -1)
                self.direccion = "izquierda"
                self.que_hace = "corriendo"
            case "saltando":
                if not self.saltando:
                    self.saltando = True
                    self.desplazamiento_y = self.capacidad_salto
                self.que_hace = que_hace 
                
            case "quieto":
                if not self.saltando:
                    self.animar_personaje(pantalla)
                self.que_hace = "quieto" 
            case "atacando":
                if not self.saltando:
                    self.animar_personaje(pantalla)
                self.que_hace = "atacando"        

        self.aplicar_gravedad(pantalla,plataformas)
    
        


                        
    def detectar_colision_enemigo(self,lista_enemigo):
        if validar_lista(lista_enemigo):
            for enemigo in lista_enemigo:
                if self.lados["right"].colliderect(enemigo.lados["main"]):
                    self.golpeado = True
                    for i in range(15):
                        for lados in self.lados:
                            self.lados[lados].x += (-5)
                            self.lados[lados].y += (-5)
                    break
                elif self.lados["left"].colliderect(enemigo.lados["main"]):
                    self.golpeado = True

                    for i in range(15):
                        for lados in self.lados:
                            self.lados[lados].x += 10
                            self.lados[lados].y += (-5)
                    break
                else:
                    self.golpeado = False


    
        
        

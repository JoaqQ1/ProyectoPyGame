import pygame, random
from Clases.Class_personaje import Personaje
from Clases.Class_proyectil import Proyectil


class Boss(Personaje):
    def __init__(self, path_img, tamaño_rect, pos_inicial, animaciones, velocidad,rango):
        super().__init__(path_img, tamaño_rect, pos_inicial, animaciones, velocidad)
        self.muerto = False
        self.colisiono = False
        self.despertando = True
        self.vida = 10
        self.rango = rango
        self.sonido_muere = pygame.mixer.Sound("sonidos/sRockReturn.ogg")


        

    def update(self,plataformas,pantalla:pygame.Surface,personaje):
        w = pantalla.get_width()
        if self.vida > 0:
            if self.despertando:
                self.direccion = "izquierda"
                self.que_hace = "despertando"
                self.animar_personaje(pantalla)
                ultima_animacion = len(self.animaciones[self.direccion][self.que_hace])
                if ultima_animacion == self.frame_actual:
                    self.despertando = False
            else:
                if personaje.arma_especial:
                    if self.detectar_colision_con_proyectil(personaje.lista_proyectiles):
                        self.vida -= 1
                

                velocidad = random.randint(15,25)
                self.que_hace = "moviendose"
                if personaje.lados["main"].x > self.lados["main"].x:
                    self.direccion = "derecha"
                else:
                    self.direccion = "izquierda"


                if self.lados["main"].x == self.rango: 
                    self.velocidad = 5
                    self.que_hace = "moviendose"
                elif (self.lados["main"].x == w - 100):
                    self.velocidad = -5
                    self.que_hace = "moviendose"
                self.mover_personaje(self.velocidad,w)


                if self.lanzar_proyectil == False:
                    self.saltando = True                                                  
                    self.desplazamiento_y = -10
                    if personaje.lados["bottom"].y >= self.lados["main"].centery:
                        self.que_hace = "atacando"
                        self.lanzar_proyectil = True

                        proyectil = Proyectil("Proyectil/laser.png",(40,40),self.lados["main"].centerx,self.lados["main"].centery)       
                        self.lista_proyectiles.append(proyectil)
                            
                self.shoot(pantalla,velocidad)
                self.aplicar_gravedad(pantalla,plataformas)
                if self.saltando == False:
                    self.animar_personaje(pantalla)
        else:
            if self.estado_sonido:
                self.sonido_muere.play()
            personaje.score += 300
            self.que_hace = "muriendo"
            self.animar_personaje(pantalla)
            ultima_animacion = len(self.animaciones[self.direccion][self.que_hace])
            if ultima_animacion == self.frame_actual:
                print("entre")
                self.muerto = True
        
        


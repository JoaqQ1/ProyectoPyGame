import pygame
from Clases.Class_objeto_juego import Objeto_Juego
from config import escalar_png


class Item(Objeto_Juego):
    def __init__(self, path_img, tamaño_rect, pos_inicial,caracteristica,impulso=0,lista_animaciones=""):
        super().__init__(path_img, tamaño_rect, pos_inicial)
        ##################################################        
        self.caracteristica = caracteristica
        self.recogido = False
        self.sonido_item = pygame.mixer.Sound("sonidos/sCoinGet.ogg")
        self.sonido_item_peligroso = pygame.mixer.Sound("sonidos/sRockReturn.ogg")
        self.impulso = impulso
        ###########################################
        self.w = tamaño_rect[0]
        self.h = tamaño_rect[1]
        self.lista_animaciones = lista_animaciones
        self.tiene_animacion = False
        if self.lista_animaciones != "":
            escalar_png(self.lista_animaciones,(self.w,self.h))
            self.tiene_animacion = True
        self.frame_actual = 0
        ##################################################

        
    
    
    def update(self,personaje,pantalla):
        if self.tiene_animacion != True:
            self.draw(pantalla)
        else:
            self.animar(pantalla)
        match self.caracteristica:
            case "vida":
                if self.lados["main"].colliderect(personaje.lados["main"]):
                    self.sonido_item.play()
                    self.recogido = True
                    personaje.vida += 1
            case "impulso":
                if self.lados["top"].colliderect(personaje.lados["bottom"]):
                   personaje.saltando = True
                   personaje.desplazamiento_y = self.impulso
            case "llave":
                if self.lados["main"].colliderect(personaje.lados["main"]):
                    self.sonido_item.play()
                    personaje.llave = True
                    self.recogido = True
            case "puerta":
                if personaje.llave:
                    if self.lados["main"].colliderect(personaje.lados["main"]):
                        self.sonido_item.play()
                        personaje.entro = True
            case "moneda":
                if self.lados["main"].colliderect(personaje.lados["main"]):
                        self.sonido_item.play()
                        self.recogido = True
                        personaje.score += 100
            case "peligroso":
                if self.lados["main"].colliderect(personaje.lados["main"]):
                    self.sonido_item_peligroso.play()
                    self.recogido = True
                    personaje.golpeado = True


    def animar(self,pantalla:pygame.Surface):                                
        largo = len(self.lista_animaciones)                        
        if self.frame_actual >= largo:
            self.frame_actual = 0                   
        
        pantalla.blit(self.lista_animaciones[self.frame_actual],self.lados["main"])
        self.frame_actual += 1

                
    
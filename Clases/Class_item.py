import pygame
from Clases.Class_objeto_juego import Objeto_Juego


class Item(Objeto_Juego):
    def __init__(self, path_img, tamaño_rect, pos_inicial,caracteristica,impulso=0):
        super().__init__(path_img, tamaño_rect, pos_inicial)
        self.caracteristica = caracteristica
        self.recogido = False
        self.sonido_item = pygame.mixer.Sound("sonidos/sCoinGet.ogg")
        self.impulso = impulso
        
    
    
    def update(self,personaje,pantalla):
        self.draw(pantalla)
        match self.caracteristica:
            case "vida":
                if self.lados["main"].colliderect(personaje.lados["main"]):
                    # self.rect.center = (random.randrange(-1000,0,1000),random.randrange(-1000,0,1000))
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

                
    
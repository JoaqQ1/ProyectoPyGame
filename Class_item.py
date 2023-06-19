import random
from Class_objeto_juego import Objeto_Juego
from Class_personaje_pricipal import Personaje_principal

class Item(Objeto_Juego):
    def __init__(self, path_img, tamaño_rect, pos_inicial,caracteristica):
        super().__init__(path_img, tamaño_rect, pos_inicial)
        self.caracteristica = caracteristica
    
    
    def aplicar_efecto(self,personaje:Personaje_principal):
        match self.caracteristica:
            case "vida":
                if self.lados["main"].colliderect(personaje.lados["main"]):
                    self.rect.center = (random.randrange(-1000,0,1000),random.randrange(-1000,0,1000))
                    personaje.vida += 1
            case "impulso":
                if self.lados["main"].colliderect(personaje.lados["main"]):
                    for i in range(15):
                        for lados in personaje.lados:                            
                            personaje.lados[lados].y += (-15)

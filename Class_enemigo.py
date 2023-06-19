from Class_personaje import Personaje

class Enemigo(Personaje):
    def __init__(self, path_img, tamaño_rect, pos_inicial, animaciones, velocidad):
        super().__init__(path_img, tamaño_rect, pos_inicial, animaciones, velocidad)
        self.esta_peleando = False

    def realizar_comportamiento(self,plataformas,pantalla):
        colision = self.detectar_colision_con_pared(plataformas)
        self.que_hace = "corriendo"

        if colision == 1:
            self.direccion = "izquierda"
            self.velocidad = self.velocidad * -1
        elif colision == -1:
            self.direccion = "derecha"
            self.velocidad = 5        
        
        if not self.saltando:
            self.animar_personaje(pantalla)
        self.mover_personaje(self.velocidad)
        self.aplicar_gravedad(pantalla, plataformas)
    
    def colisiono_con_el_personaje(self,personaje:Personaje):
        if self.lados["main"].colliderect(personaje.lados["main"]):
            return True
        else:
            return False
    
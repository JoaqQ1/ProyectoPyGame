import pygame
from config import escalar_png,obtener_rectangulos
class Personaje():
    def __init__(self, tamaño,animaciones, punto_inicio,velocidad):
        #animacion
        self.ancho = tamaño[0]
        self.alto = tamaño[1]
        self.animaciones = animaciones
        self.frame_actual = 0
        self.rescalar_animaciones() 
        self.que_hace = "quieto"
        self.direccion = "derecha"
        #Rectangulo
        rectangulo = animaciones["derecha"]["quieto"][0].get_rect()
        rectangulo.x = punto_inicio[0]
        rectangulo.y = punto_inicio[1]
        self.lados = obtener_rectangulos(rectangulo)
        #Movimiento
        self.velocidad = velocidad
        self.desplazamiento_y = 0
        #Gravedad
        self.gravedad = 1
        self.limite_velocidad_caida = 15
        self.capacidad_salto = -15
        self.saltando = False

    def rescalar_animaciones(self):
        for clave in self.animaciones["izquierda"]:
            escalar_png(self.animaciones["izquierda"][clave],(self.ancho,self.alto))
        for clave in self.animaciones["derecha"]:
            escalar_png(self.animaciones["derecha"][clave],(self.ancho,self.alto))


    def mover_personaje(self,velocidad):
        for lados in self.lados:            
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
            
                       

    def update(self,pantalla:pygame.Surface,plataformas,que_hace):
        
        match que_hace:
            case "derecha":  
                if not self.saltando:
                    self.animar_personaje(pantalla)
                if self.detectar_colision(plataformas) != 1:
                    self.mover_personaje(self.velocidad)
                self.direccion = "derecha"
                self.que_hace = "corriendo"
            case "izquierda":
                if not self.saltando:
                    self.animar_personaje(pantalla)
                if self.detectar_colision(plataformas) != -1:                      
                    self.mover_personaje(self.velocidad*-1)
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
        
            
    
    
    def detectar_colision(self,plataformas):
        
        for i in range(len(plataformas)):
            for pared in plataformas[i]:
                if pared == "right" or pared == "left":
                    if self.lados["right"].colliderect(plataformas[i][pared]):
                        return 1 
                    elif self.lados["left"].colliderect(plataformas[i][pared]):
                        return -1
                    
                    
                
    
    
    
        
        

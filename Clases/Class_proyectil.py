import pygame

class Proyectil():
    def __init__(self,path, tamaño_rect, x,y):
        self.image = pygame.image.load(path)
        self.superficie = pygame.transform.scale(self.image,tamaño_rect)
        self.rect = self.superficie.get_rect()
        self.rect.y = y
        self.rect.centerx = x        
        self.velocidad = 15
        self.primera_vuelta = True
        self.direccion = "derecha"
        self.activo = True      
    
    
    def update(self,personaje,pantalla,velocidad,direccion):
        #La bandera de primera vuelta la hago para capturar la direcion que se encuentra apuntado el personaje
        if self.primera_vuelta:
            self.direccion = direccion
            self.primera_vuelta = False
        if self.direccion == "izquierda":
            velocidad = velocidad * -1

        elif self.direccion == "derecha":
            velocidad = velocidad * 1
        
        self.draw(pantalla)
        self.avanzar(velocidad)

        w = pantalla.get_width()
        
        if self.rect.x > w or self.rect.x < -10:
            personaje.lanzar_proyectil = False
            self.activo = False
        
       
    def draw(self,pantalla:pygame.Surface):                
        pantalla.blit(self.superficie,self.rect)
        

    def avanzar(self,velocidad):
        self.rect.x += velocidad
    


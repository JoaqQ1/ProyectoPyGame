import pygame
from Clases.Class_personaje_pricipal import Personaje_principal
from Clases.Class_item import Item


class Juego:
    def __init__(self):
        self.gravedad = 1
        
    def iniciar_juego():
        pygame.init()

    def crear_pantalla(medidas):
        if(type(medidas) == tuple):
            return pygame.display.set_mode(medidas)

    def retornar_medidas_superficie(superficie:pygame.Surface):
        largo = superficie.get_width()
        alto = superficie.get_height()
        medidas = (largo,alto)
        return  medidas
    
    def detectar_accion(lista_teclas:pygame.key):        
        if lista_teclas[pygame.K_UP]:        
            accion = "saltando"
        elif lista_teclas[pygame.K_LEFT]:
            accion = "izquierda"
        elif lista_teclas[pygame.K_RIGHT]:
            accion = "derecha"
        elif lista_teclas[pygame.K_a]:
            accion = "atacando"
        else:
            accion = "quieto"
        return accion
    
    def actualizar_pantalla(pantalla,personaje:Personaje_principal,fondo,plataformas,lista_enemigos:list,lista_items:Item,lista_trampas):
        ancho_pantalla = Juego.retornar_medidas_superficie(pantalla)
        lista_teclas = pygame.key.get_pressed()
        if personaje.golpeado == False:
            que_hace = Juego.detectar_accion(lista_teclas)
        else:
            que_hace = "muriendo"
       
        pantalla.blit(fondo,(0,0))
        personaje.update(pantalla,plataformas,que_hace,ancho_pantalla,lista_enemigos,lista_trampas)

        for item in lista_items:
            item.update(personaje,pantalla)
            if item.recogido:
                lista_items.remove(item)
        for trampa in lista_trampas:
            trampa.update((615,860),pantalla)
        if len(lista_enemigos) > 0:
            for enemigo in lista_enemigos:
                if enemigo.muerto == False:
                    enemigo.update(plataformas,pantalla,personaje,ancho_pantalla[0])
                else:
                    lista_enemigos.remove(enemigo)
        
        
            
        
        
    
                       


  
        



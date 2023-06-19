import pygame
from Class_personaje_pricipal import Personaje_principal
from Class_enemigo import Enemigo
from Class_item import Item

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
        ancho = superficie.get_height()
        medidas = (largo,ancho)
        return  medidas
    
    def actualizar_pantalla(pantalla,personaje:Personaje_principal,fondo,plataformas,enemigo:Enemigo,items:Item,lista_enemigos:list):
        lista_teclas = pygame.key.get_pressed()        
        que_hace = Juego.detectar_accion(lista_teclas)
        
        pantalla.blit(fondo,(0,0))
        for item in items:
            pantalla.blit(item.superficie,item.lados["main"])
            item.aplicar_efecto(personaje)

            
        personaje.update(pantalla,plataformas,que_hace)
        personaje.detectar_colision_enemigo(lista_enemigos)

        if personaje.golpeado:
            personaje.vida -= 1
        
        if enemigo.esta_peleando != True:
            enemigo.realizar_comportamiento(plataformas,pantalla)
        
        if enemigo.colisiono_con_el_personaje(personaje):
            enemigo.esta_peleando = True
            enemigo.que_hace = "atacando"
            enemigo.animar_personaje(pantalla)            
        else:
            enemigo.esta_peleando = False
    
       

                
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


  
        



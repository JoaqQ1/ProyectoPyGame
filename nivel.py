import pygame,sys
from modo import *
class Nivel:
    def __init__(self,pantalla,personaje_principal,lista_plataformas,imagen_fondo,lista_enemigos,lista_items,lista_trampas):
        ##### ATRIBUTOS #######
        self._slave = pantalla
        self.jugador = personaje_principal
        self.plataformas = lista_plataformas        
        self.imagen_fondo = imagen_fondo
        self.enemigos = lista_enemigos
        self.items = lista_items
        self.trampas = lista_trampas
        #####################

    def update(self,lista_eventos):
        for event in lista_eventos:
            if event.type == pygame.KEYDOWN:         
                if event.key == pygame.K_TAB:            
                    cambiar_modo() 
            elif event.type == pygame.QUIT: 
                sys.exit()
        self.actualizar_pantalla()
        self.dibujear_rectangulos()



    def leer_inputs(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:        
            accion = "saltando"
        elif keys[pygame.K_LEFT]:
            accion = "izquierda"
        elif keys[pygame.K_RIGHT]:
            accion = "derecha"
        elif keys[pygame.K_a]:
            accion = "atacando"
        else:
            accion = "quieto"
        return accion
    
    def dibujear_rectangulos(self):
        if get_debug(): 
            #Personaje
            for lado in self.jugador.lados:
                pygame.draw.rect(self._slave,"Red",self.jugador.lados[lado],1)

            #Enemigo
            if len(self.enemigos) > 0:
                for enemigo in self.enemigos:
                    for lado in enemigo.lados:
                        pygame.draw.rect(self._slave,"Red",enemigo.lados[lado],1)
            
            #Pisos-Plataformas
            for i in range(len(self.plataformas)):
                for lado in self.plataformas[i]:   
                    pygame.draw.rect(self._slave,"Blue",self.plataformas[i][lado],1)
    def actualizar_pantalla(self):
        ancho_pantalla = self.retornar_medidas_superficie()
        # lista_teclas = pygame.key.get_pressed()
        if self.jugador.golpeado == False:
            que_hace = self.leer_inputs()
        else:
            que_hace = "muriendo"
       
        self._slave.blit(self.imagen_fondo,(0,0))
        self.jugador.update(self._slave,self.plataformas,que_hace,ancho_pantalla,self.enemigos,self.trampas)

        for item in self.items:
            item.update(self.jugador,self._slave)
            if item.recogido:
                self.items.remove(item)
        for trampa in self.trampas:
            trampa.update(self._slave)
        if len(self.enemigos) > 0:
            for enemigo in self.enemigos:
                if enemigo.muerto == False:
                    enemigo.update(self.plataformas,self._slave,self.jugador)
                else:
                    self.enemigos.remove(enemigo)
       

    def retornar_medidas_superficie(self):
        largo = self._slave.get_width()
        alto = self._slave.get_height()
        medidas = (largo,alto)
        return  medidas
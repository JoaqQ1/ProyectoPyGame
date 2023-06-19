import pygame,sys

from Constantes import *
from modo import *
from config import *
from Constantes_juego import *
from Constantes_plataformas import *
from Contantes_enemigo import *
from clases import *

medidas_apolo = (LARGO_PLYER,ANCHO_PLYER)
medidas_enemigo =(LARGO_ENEMIGO,ANCHO_ENEMIGO) 

#Creacion de ventana
PANTALLA = Juego.crear_pantalla((LARGO,ANCHO))
screen_size = (LARGO,ANCHO) 
#Inicio juego
Juego.iniciar_juego()
clock = pygame.time.Clock()

fondo_imagen = pygame.image.load("Fondos/fondo_lvl_1.png")
fondo = pygame.transform.scale(fondo_imagen,screen_size)


pygame.display.set_caption("ApoloGame")
fuente = pygame.font.SysFont("consolas",25)

personaje = Personaje_principal("Apolo/Quieto/apolo_quieto_0.png",medidas_apolo,pos_inicial_lvl_1,diccionario_acciones,10)
enemigo = Enemigo("pgn/ENEMIGO/quieto/0.png",medidas_enemigo,punto_de_inicio_enemigo,diccionario_acciones_enemigo,5)
manzana = Item("item/Apple.png",(50,50),(1240,350),"vida")
trampolin = Item("item/trampolin.png",(80,80),(1040,728),"impulso")
lista_enemigos = [enemigo]
lista_items = [manzana,trampolin]

while(True):
    if personaje.vida == 0:
        sys.exit()    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:         
            if event.key == pygame.K_TAB:            
                cambiar_modo() 
        elif event.type == pygame.QUIT: 
            sys.exit()

                                         
  
    Juego.actualizar_pantalla(PANTALLA,personaje,fondo,lista_con_rectangulos_de_colision,enemigo,lista_items,lista_enemigos)
  
    texto = fuente.render(f"VIDA: {personaje.vida}",False,"Red")
    PANTALLA.blit(texto,(0,0))
    # PANTALLA.blit(item.superficie,item.lados["main"])
 
    if get_debug(): 
        #Personaje
        for lado in personaje.lados:
            pygame.draw.rect(PANTALLA,"Red",personaje.lados[lado],1)

        #Enemigo
        for lado in enemigo.lados:
            pygame.draw.rect(PANTALLA,"Red",enemigo.lados[lado],1)
        
        #Pisos-Plataformas
        for i in range(len(lista_con_rectangulos_de_colision)):
            for lado in lista_con_rectangulos_de_colision[i]:   
                pygame.draw.rect(PANTALLA,"Blue",lista_con_rectangulos_de_colision[i][lado],1)

   
    clock.tick(FPS) 
    pygame.display.flip()
   
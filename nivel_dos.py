import pygame
from Constantes.Constantes import *
from Constantes.Constantes_juego import *
from Constantes.Constantes_plataformas import *
from Constantes.Contantes_enemigo import *
from clases import *
from nivel import Nivel

class Nivel_dos(Nivel):
    def __init__(self, pantalla):

        W = pantalla.get_width()
        H = pantalla.get_height()
        screen = (W,H)
        medidas_apolo = (LARGO_PLYER,ANCHO_PLYER)
        medidas_enemigo =(LARGO_ENEMIGO,ANCHO_ENEMIGO) 

        #Fondo
        fondo_imagen = pygame.image.load("Fondos/fondo_lvl_2.png")
        fondo = pygame.transform.scale(fondo_imagen,screen)

        #PJS
        personaje = Personaje_principal("Apolo/Quieto/apolo_quieto_0.png",medidas_apolo,pos_inicial_lvl_2,diccionario_acciones,10)
        #ENEMIGOS
        enemigo = Enemigo("pgn/ENEMIGO/quieto/0.png",medidas_enemigo,punto_de_inicio_enemigo_lvl_2,diccionario_acciones_enemigo,5)
        enemigo_2 = Enemigo("pgn/ENEMIGO/quieto/0.png",medidas_enemigo,(1490,480),diccionario_acciones_enemigo,5)
        fantasma = Enemigo_fantasma("pgn/ENEMIGO3/camina/19.png",(60,60),(800,830),diccionario_acciones_fantasma,5,(0,885))
        
        #TRAMPAS
        cierra = Trampa("trampa/cierra.png",(40,40),(140,533),(130,500))
        
        #ITEMS
        manzana = Item("item/Apple.png",(50,50),(441, 523),"vida")
        trampolin = Item("item/trampolin.png",(70,70),(890,860),"impulso")
        llave = Item("item/llave.png",(20,20),(1833, 689),"llave")        
        puerta = Item("puerta/puerta.png",(60,120),(319,180),"puerta")
        
        #PLATAFORMAS

        piso_abajo_lvl_2 = pygame.Rect(0,885,921,100)
        plataforma_arriba_lvl_2 = pygame.Rect(127, 533,465,60)
        plataforma_de_inicio_lvl_2 = pygame.Rect(190, 240,253,60)
        plataforma_baja_lvl_2 = pygame.Rect(1294,885,424,60)
        plataforma_arriba_de_la_baja_lvl_2 = pygame.Rect(1351, 593,302,60)
        techo_enfrente_lvl_2 = pygame.Rect(1719,710,181,30)
        pared_del_techo_lvl_2 = pygame.Rect(1719,730,30,200)

        plataformas = [plataforma_arriba_lvl_2,piso_abajo_lvl_2,plataforma_de_inicio_lvl_2,plataforma_baja_lvl_2,plataforma_arriba_de_la_baja_lvl_2,techo_enfrente_lvl_2,pared_del_techo_lvl_2]

        lista_plataformas = rectangulos_convertidos(plataformas)


        lista_enemigos = [fantasma,enemigo,enemigo_2]
        lista_items = [manzana,trampolin,llave,puerta]
        lista_trampas = [cierra]
        
        super().__init__(pantalla, personaje, lista_plataformas, fondo, lista_enemigos, lista_items, lista_trampas)
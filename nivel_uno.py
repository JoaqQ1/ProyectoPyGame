import pygame,sqlite3
from Constantes.Constantes import *
from Constantes.Constantes_juego import *
from Constantes.Constantes_plataformas import *
from Constantes.Contantes_enemigo import *
from clases import *
from nivel import Nivel

class Nivel_uno(Nivel):
    def __init__(self, pantalla):   

        W = pantalla.get_width()
        H = pantalla.get_height()
        screen = (W,H)
        medidas_apolo = (LARGO_PLYER,ANCHO_PLYER)
        medidas_enemigo =(LARGO_ENEMIGO,ANCHO_ENEMIGO) 

        #Fondo
        fondo_imagen = pygame.image.load("Fondos/fondo_lvl_1.png")
        fondo = pygame.transform.scale(fondo_imagen,screen)

        #PJS
        personaje = Personaje_principal("Apolo/Quieto/apolo_quieto_0.png",medidas_apolo,pos_inicial_lvl_1,diccionario_acciones,10)
        enemigo = Enemigo("pgn/ENEMIGO/quieto/0.png",medidas_enemigo,punto_de_inicio_enemigo,diccionario_acciones_enemigo,5)

        
        #TRAMPAS
        cierra = Trampa("trampa/cierra.png",(40,40),(650,825),(615,860))
        
        #ITEMS
        manzana = Item("item/Apple.png",(50,50),(1240,350),"vida")
        trampolin = Item("item/trampolin.png",(70,70),(1055,739),"impulso",-30)
        llave = Item("item/llave.png",(20,20),(1500,350),"llave")        
        puerta = Item("puerta/puerta.png",(60,120),(460,290),"puerta",nivel=2)
        moneda = Item("monedas/monedaNo1_00.png",(30,30),(1340,300),"moneda",lista_animaciones=moneda_moviendose_lvl_1)
        moneda_2 = Item("monedas/monedaNo1_00.png",(30,30),(1380,300),"moneda",lista_animaciones=moneda_moviendose_lvl_1)
        moneda_3 = Item("monedas/monedaNo1_00.png",(30,30),(1420,300),"moneda",lista_animaciones=moneda_moviendose_lvl_1)
        moneda_4 = Item("monedas/monedaNo1_00.png",(30,30),(665,650),"moneda",lista_animaciones=moneda_moviendose_lvl_1)
        moneda_5 = Item("monedas/monedaNo1_00.png",(30,30),(680,610),"moneda",lista_animaciones=moneda_moviendose_lvl_1)
        moneda_6 = Item("monedas/monedaNo1_00.png",(30,30),(695,650),"moneda",lista_animaciones=moneda_moviendose_lvl_1)
        
        
        #PLATAFORMAS
        piso_principal = pygame.Rect(0,650,435,60)
        caja_grande = pygame.Rect(435,710,125,125)
        caja_chica = pygame.Rect(550,770,60,60)
        piso_abajo = pygame.Rect(415,825,445,60)
        sobre_piso = pygame.Rect(860,765,245,60) 
        escotilla = pygame.Rect(1100,540,150,300)
        piso_arriba = pygame.Rect(1220,420,670,60)
        plataforma_arriba = pygame.Rect(265,340,465,60)

        plataformas = [piso_principal,piso_abajo,piso_arriba,escotilla,caja_grande,caja_chica,sobre_piso,plataforma_arriba]

        lista_plataformas = rectangulos_convertidos(plataformas)


        lista_enemigos = [enemigo]
        lista_items = [manzana,trampolin,llave,puerta,moneda,moneda_2,moneda_3,moneda_4,moneda_5,moneda_6]
        lista_trampas = [cierra]
        
        super().__init__(pantalla, personaje, lista_plataformas, fondo, lista_enemigos, lista_items, lista_trampas)

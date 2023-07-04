import pygame
from Constantes.Constantes import *
from Constantes.Constantes_juego import *
from Constantes.Constantes_plataformas import *
from Constantes.Contantes_enemigo import *
from clases import *
from nivel import Nivel

class Nivel_tres(Nivel): #-------------------> Seguir creando lvl 3, Falta agregar boss, completar plataformas,y agregar monedas
    def __init__(self, pantalla):
        
        W = pantalla.get_width()
        H = pantalla.get_height()
        screen = (W,H)
        medidas_apolo = (LARGO_PLYER,ANCHO_PLYER)
        medidas_enemigo =(LARGO_ENEMIGO,ANCHO_ENEMIGO) 

        #Fondo
        fondo_imagen = pygame.image.load("Fondos/fondo_lvl_3.png")
        fondo = pygame.transform.scale(fondo_imagen,screen)

        #PJS
        personaje = Personaje_principal("Apolo/Quieto/apolo_quieto_0.png",medidas_apolo,pos_inicial_lvl_2,diccionario_acciones,15)
        #ENEMIGOS
        boss = Boss("pgn/BOSS/DESPERTANDO/28.png",(200,200),punto_de_inicio_boss_lvl_3,diccionario_acciones_boss,5,1050)
        enemigo = Enemigo("pgn/ENEMIGO/quieto/0.png",medidas_enemigo,punto_de_inicio_enemigo_lvl_3,diccionario_acciones_enemigo,5)
        fantasma = Enemigo_fantasma("pgn/ENEMIGO3/camina/19.png",(60,60),(200,580),diccionario_acciones_fantasma,5,(0,460))
        trampa_enemigo = Enemigo_trampa("enemigo_trampa/0.png",(60,60),(400,810),acciones_tram_enemig,15,(300,885))

        
        #TRAMPAS
        # cierra = Trampa("trampa/cierra.png",(40,40),(140,533),(130,500))

        #ITEMS
        trofeo_final = Item("item/End (Idle).png",(60,120),(820 ,190),"puerta")
        manzana = Item("item/Apple.png",(50,50),(441, 523),"vida")
        trampolin_3 = Item("item/trampolin.png",(70,70),(490, 600),"impulso",-25)
        trampolin_2 = Item("item/trampolin.png",(70,70),(700,845),"impulso",-25)
        arma_especial = Item("item/0.png",(30,30),(200,600),"arma_especial")
        llave = Item("item/llave.png",(20,20),(1833, 689),"llave")        
        puerta = Item("puerta/puerta.png",(60,120),(820 ,190),"puerta",desaparece=True)
        moneda = Item("monedas/monedaNo10_00.png",(30,30),(240, 478),"moneda",lista_animaciones=moneda_moviendose_lvl_3)
        moneda_2 = Item("monedas/monedaNo10_00.png",(30,30),(270,478),"moneda",lista_animaciones=moneda_moviendose_lvl_3)
        moneda_3 = Item("monedas/monedaNo10_00.png",(30,30),(300,478),"moneda",lista_animaciones=moneda_moviendose_lvl_3)
        moneda_4 = Item("monedas/monedaNo10_00.png",(30,30),(1037, 605),"moneda",lista_animaciones=moneda_moviendose_lvl_3)
        moneda_5 = Item("monedas/monedaNo10_00.png",(30,30),(1097,605),"moneda",lista_animaciones=moneda_moviendose_lvl_3)
        moneda_6 = Item("monedas/monedaNo10_00.png",(30,30),(1157,605),"moneda",lista_animaciones=moneda_moviendose_lvl_3)
        moneda_7 = Item("monedas/monedaNo10_00.png",(30,30),(1037,565),"moneda",lista_animaciones=moneda_moviendose_lvl_3)
        moneda_8 = Item("monedas/monedaNo10_00.png",(30,30),(1097,565),"moneda",lista_animaciones=moneda_moviendose_lvl_3)
        moneda_9 = Item("monedas/monedaNo10_00.png",(30,30),(1157,565),"moneda",lista_animaciones=moneda_moviendose_lvl_3)
        moneda_10 = Item("monedas/monedaNo10_00.png",(30,30),(330,478),"moneda",lista_animaciones=moneda_moviendose_lvl_3)
        moneda_11 = Item("monedas/monedaNo10_00.png",(30,30),(360,478),"moneda",lista_animaciones=moneda_moviendose_lvl_3)


        calavera = Item("item_peligrosos/36.png",(30,30),(1500,700),"peligroso",lista_animaciones=calavera_moviendose)
        
        #PLATAFORMAS

        piso_abajo_lvl_3 = pygame.Rect(0,885,750,100)
        plataforma_arriba_lvl_3 = pygame.Rect(0, 618,550,30)
        plataforma_de_inicio_lvl_3 = pygame.Rect(424, 269,503,60)
        plataforma_baja_lvl_3 = pygame.Rect(1050,885,850,60)
       

        plataformas = [plataforma_arriba_lvl_3,piso_abajo_lvl_3,plataforma_de_inicio_lvl_3,plataforma_baja_lvl_3]

        lista_plataformas = rectangulos_convertidos(plataformas)
        lista_enemigos = [fantasma,enemigo,boss,trampa_enemigo]
        lista_items = [trofeo_final,manzana,llave,puerta,trampolin_2,trampolin_3,moneda,moneda_2,moneda_3,moneda_4,moneda_5,moneda_6,moneda_7,moneda_8,moneda_9,moneda_10,moneda_11,calavera,arma_especial]
        lista_trampas = []


        

        
        
        super().__init__(pantalla, personaje, lista_plataformas, fondo, lista_enemigos, lista_items, lista_trampas)
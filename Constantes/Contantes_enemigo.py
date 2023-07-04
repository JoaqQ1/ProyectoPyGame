import pygame
from config import girar_png
                    #####ESQUELETO######
enemigo_camina = [
                pygame.image.load("pgn/ENEMIGO/camina/28.png"),
                pygame.image.load("pgn/ENEMIGO/camina/29.png"),
                pygame.image.load("pgn/ENEMIGO/camina/30.png"),
                pygame.image.load("pgn/ENEMIGO/camina/31.png"),
                pygame.image.load("pgn/ENEMIGO/camina/32.png"),
                pygame.image.load("pgn/ENEMIGO/camina/33.png"),
                pygame.image.load("pgn/ENEMIGO/camina/34.png")
                ]
enemigo_quieto = [
                pygame.image.load("pgn/ENEMIGO/quieto/0.png"),
                pygame.image.load("pgn/ENEMIGO/quieto/1.png"),
                pygame.image.load("pgn/ENEMIGO/quieto/2.png"),
                pygame.image.load("pgn/ENEMIGO/quieto/3.png"),
                pygame.image.load("pgn/ENEMIGO/quieto/4.png"),
                pygame.image.load("pgn/ENEMIGO/quieto/5.png"),
                pygame.image.load("pgn/ENEMIGO/quieto/6.png"),
                pygame.image.load("pgn/ENEMIGO/quieto/7.png")
                ] 
enemigo_atacando = [
                pygame.image.load("pgn/ENEMIGO/atacando/8.png"),
                pygame.image.load("pgn/ENEMIGO/atacando/9.png"),
                pygame.image.load("pgn/ENEMIGO/atacando/10.png")
                ]
enemigo_muriendo = [
                pygame.image.load("pgn/ENEMIGO/muriendo/35.png"),
                pygame.image.load("pgn/ENEMIGO/muriendo/36.png"),
                pygame.image.load("pgn/ENEMIGO/muriendo/37.png"),
                pygame.image.load("pgn/ENEMIGO/muriendo/38.png"),
                pygame.image.load("pgn/ENEMIGO/muriendo/39.png"),
                pygame.image.load("pgn/ENEMIGO/muriendo/40.png"),
                pygame.image.load("pgn/ENEMIGO/muriendo/41.png"),
                ]

enemigo_camina_izq = girar_png(enemigo_camina,True,False)
enemigo_quieto_izq = girar_png(enemigo_quieto,True,False)
enemigo_atacando_izq = girar_png(enemigo_atacando,True,False)
enemigo_muriendo_izq = girar_png(enemigo_muriendo,True,False)


diccionario_acciones_enemigo = {
    "derecha":
    {
    "corriendo": enemigo_camina,
    "quieto": enemigo_quieto,
    "atacando": enemigo_atacando,
    "muriendo": enemigo_muriendo
    },
    "izquierda":
    {
    "corriendo": enemigo_camina_izq,
    "quieto": enemigo_quieto_izq,
    "atacando": enemigo_atacando_izq,
    "muriendo": enemigo_muriendo_izq
    }}

#Medidas enemigo
LARGO_ENEMIGO = 100
ANCHO_ENEMIGO = 100

punto_de_inicio_enemigo = (900,680)
punto_de_inicio_enemigo_lvl_2 = (1580,830)
punto_de_inicio_enemigo_lvl_3 = (1200,830)


            ######FANTASMA######

fantasma_moviendose = [
                pygame.image.load("pgn/ENEMIGO3/camina/19.png"),
                pygame.image.load("pgn/ENEMIGO3/camina/20.png"),
                pygame.image.load("pgn/ENEMIGO3/camina/21.png"),
                pygame.image.load("pgn/ENEMIGO3/camina/22.png"),
                pygame.image.load("pgn/ENEMIGO3/camina/23.png")
                ]
fantasma_muriendo = [
                pygame.image.load("pgn/ENEMIGO3/muere/24.png"),
                pygame.image.load("pgn/ENEMIGO3/muere/25.png"),
                pygame.image.load("pgn/ENEMIGO3/muere/26.png"),
                pygame.image.load("pgn/ENEMIGO3/muere/27.png"),
                pygame.image.load("pgn/ENEMIGO3/muere/28.png")
                ]

fantasma_moviendose_izq = girar_png(enemigo_camina,True,False)
fantasma_muriendo_izq = girar_png(enemigo_quieto,True,False)

diccionario_acciones_fantasma = {
    "derecha":
    {
    "moviendose": fantasma_moviendose,
    "muriendo": fantasma_muriendo
    },
    "izquierda":
    {
    "moviendose": fantasma_moviendose_izq,
    "muriendo": fantasma_muriendo_izq
    }}


boss_despertando = [
                pygame.image.load("pgn/BOSS/DESPERTANDO/28.png"),
                pygame.image.load("pgn/BOSS/DESPERTANDO/27.png"),
                pygame.image.load("pgn/BOSS/DESPERTANDO/26.png"),
                pygame.image.load("pgn/BOSS/DESPERTANDO/25.png"),
                pygame.image.load("pgn/BOSS/DESPERTANDO/24.png"),
                pygame.image.load("pgn/BOSS/DESPERTANDO/23.png"),
                pygame.image.load("pgn/BOSS/DESPERTANDO/22.png"),
                pygame.image.load("pgn/BOSS/DESPERTANDO/21.png"),
                ] 
boss_camina = [
                pygame.image.load("pgn/BOSS/MOVIENDOSE/0.png"),
                pygame.image.load("pgn/BOSS/MOVIENDOSE/1.png"),
                pygame.image.load("pgn/BOSS/MOVIENDOSE/2.png"),
                pygame.image.load("pgn/BOSS/MOVIENDOSE/3.png"),
                pygame.image.load("pgn/BOSS/MOVIENDOSE/4.png"),
                pygame.image.load("pgn/BOSS/MOVIENDOSE/5.png"),
                pygame.image.load("pgn/BOSS/MOVIENDOSE/6.png"),
                pygame.image.load("pgn/BOSS/MOVIENDOSE/7.png"),
                pygame.image.load("pgn/BOSS/MOVIENDOSE/8.png"),
                pygame.image.load("pgn/BOSS/MOVIENDOSE/9.png"),
                pygame.image.load("pgn/BOSS/MOVIENDOSE/10.png"),
                pygame.image.load("pgn/BOSS/MOVIENDOSE/11.png"),
                pygame.image.load("pgn/BOSS/MOVIENDOSE/12.png")
                ]
boss_atacando = [
                pygame.image.load("pgn/BOSS/ATACANDO/13.png"),
               pygame.image.load("pgn/BOSS/ATACANDO/14.png"),
               pygame.image.load("pgn/BOSS/ATACANDO/15.png"),
               pygame.image.load("pgn/BOSS/ATACANDO/16.png"),
               pygame.image.load("pgn/BOSS/ATACANDO/17.png"),
               pygame.image.load("pgn/BOSS/ATACANDO/18.png"),
               pygame.image.load("pgn/BOSS/ATACANDO/19.png"),
                ]
boss_muriendo = [
                pygame.image.load("pgn/BOSS/MURIENDO/40.png"),
                pygame.image.load("pgn/BOSS/MURIENDO/41.png"),
                pygame.image.load("pgn/BOSS/MURIENDO/42.png"),
                pygame.image.load("pgn/BOSS/MURIENDO/43.png"),
                pygame.image.load("pgn/BOSS/MURIENDO/44.png"),
                pygame.image.load("pgn/BOSS/MURIENDO/45.png"),
                pygame.image.load("pgn/BOSS/MURIENDO/46.png"),
                pygame.image.load("pgn/BOSS/MURIENDO/47.png"),
                pygame.image.load("pgn/BOSS/MURIENDO/48.png"),
                pygame.image.load("pgn/BOSS/MURIENDO/49.png"),
                pygame.image.load("pgn/BOSS/MURIENDO/50.png"),
                pygame.image.load("pgn/BOSS/MURIENDO/51.png"),
                pygame.image.load("pgn/BOSS/MURIENDO/52.png"),
                pygame.image.load("pgn/BOSS/MURIENDO/53.png"),
                pygame.image.load("pgn/BOSS/MURIENDO/54.png"),
                pygame.image.load("pgn/BOSS/MURIENDO/55.png"),
                pygame.image.load("pgn/BOSS/MURIENDO/56.png"),
                pygame.image.load("pgn/BOSS/MURIENDO/57.png"),
                pygame.image.load("pgn/BOSS/MURIENDO/58.png"),
                pygame.image.load("pgn/BOSS/MURIENDO/59.png"),
                pygame.image.load("pgn/BOSS/MURIENDO/60.png"),
                pygame.image.load("pgn/BOSS/MURIENDO/61.png"),
                pygame.image.load("pgn/BOSS/MURIENDO/62.png"),
                pygame.image.load("pgn/BOSS/MURIENDO/63.png"),
                pygame.image.load("pgn/BOSS/MURIENDO/64.png"),
                pygame.image.load("pgn/BOSS/MURIENDO/65.png"),
                pygame.image.load("pgn/BOSS/MURIENDO/66.png"),
                pygame.image.load("pgn/BOSS/MURIENDO/67.png"),
                pygame.image.load("pgn/BOSS/MURIENDO/68.png")                
                ]
boss_despertando_izq = girar_png(boss_despertando,True,False)
boss_camina_izq = girar_png(boss_camina,True,False)
boss_atacando_izq = girar_png(boss_atacando,True,False)
boss_muriendo_izq = girar_png(boss_muriendo,True,False)

diccionario_acciones_boss = {
    "derecha":
    {
    "despertando": boss_despertando,
    "moviendose": boss_camina,
    "atacando": boss_atacando,
    "muriendo": boss_muriendo
    },
    "izquierda":
    {
    "despertando": boss_despertando_izq,
    "moviendose": boss_camina_izq,
    "atacando": boss_atacando_izq,
    "muriendo": boss_muriendo_izq
    }}
punto_de_inicio_boss_lvl_3 = (1580,500)

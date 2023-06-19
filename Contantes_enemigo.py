import pygame
from config import girar_png
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

punto_de_inicio_enemigo = (600,650)
import pygame
# from Class_plataforma import Plataforma
from config import *

##Personaje_quieto

personaje_quieto_der = [ pygame.image.load("Apolo/Quieto/apolo_quieto_0.png"),
                     pygame.image.load("Apolo/Quieto/apolo_quieto_1.png"),
                     pygame.image.load("Apolo/Quieto/apolo_quieto_2.png"),
                     pygame.image.load("Apolo/Quieto/apolo_quieto_3.png")]


personaje_corriendo_der = [pygame.image.load("/Users/joaquinignacio/Desktop/Proyecto PyGame/Apolo/Corriendo/apolo_corriendo_0.png"),
                    pygame.image.load("/Users/joaquinignacio/Desktop/Proyecto PyGame/Apolo/Corriendo/apolo_corriendo_1.png"),
                     pygame.image.load("/Users/joaquinignacio/Desktop/Proyecto PyGame/Apolo/Corriendo/apolo_corriendo_2.png"),
                     pygame.image.load("/Users/joaquinignacio/Desktop/Proyecto PyGame/Apolo/Corriendo/apolo_corriendo_3.png"),
                     pygame.image.load("/Users/joaquinignacio/Desktop/Proyecto PyGame/Apolo/Corriendo/apolo_corriendo_4.png")]

personaje_saltando_der = [ pygame.image.load("Apolo/Saltando/apolo_saltando_0.png"), 
                      pygame.image.load("Apolo/Saltando/apolo_saltando_1.png"), 
                      pygame.image.load("Apolo/Saltando/apolo_saltando_2.png"),
                    pygame.image.load("Apolo/Saltando/apolo_saltando_3.png"),
                    pygame.image.load("Apolo/Saltando/apolo_saltando_0.png"),
                    pygame.image.load("Apolo/Saltando/apolo_saltando_1.png")]


personaje_cayendo_der = [pygame.image.load("Apolo/Cayendo/apolo_cayendo_0.png"), 
                    pygame.image.load("Apolo/Cayendo/apolo_cayendo_1.png")]


personaje_peleando_der = [ pygame.image.load("Apolo/Atacando/adventurer-attack1-00.png"), 
                      pygame.image.load("Apolo/Atacando/adventurer-attack1-01.png"), 
                      pygame.image.load("Apolo/Atacando/adventurer-attack1-02.png"), 
                      pygame.image.load("Apolo/Atacando/adventurer-attack1-03.png"), 
                      pygame.image.load("Apolo/Atacando/adventurer-attack1-04.png"), 
                      pygame.image.load("Apolo/Atacando/adventurer-attack2-00.png"), 
                      pygame.image.load("Apolo/Atacando/adventurer-attack2-01.png"), 
                      pygame.image.load("Apolo/Atacando/adventurer-attack2-02.png"), 
                      pygame.image.load("Apolo/Atacando/adventurer-attack2-03.png"), 
                      pygame.image.load("Apolo/Atacando/adventurer-attack2-04.png"), 
                      pygame.image.load("Apolo/Atacando/adventurer-attack2-05.png") 
                      ]


personaje_muriendo_der = [ pygame.image.load("Apolo/Muriendo/apolo_muriendo_0.png"), 
                      pygame.image.load("Apolo/Muriendo/apolo_muriendo_1.png"), 
                      pygame.image.load("Apolo/Muriendo/apolo_muriendo_2.png"), 
                      pygame.image.load("Apolo/Muriendo/apolo_muriendo_3.png"), 
                      pygame.image.load("Apolo/Muriendo/apolo_muriendo_4.png"), 
                      pygame.image.load("Apolo/Muriendo/apolo_muriendo_5.png"),
                      pygame.image.load("Apolo/Muriendo/apolo_muriendo_6.png") 
                      ]


          

personaje_quieto_izq = girar_png(personaje_quieto_der,True,False)
personaje_corriendo_izq = girar_png(personaje_corriendo_der,True,False)
personaje_saltando_izq = girar_png(personaje_saltando_der,True,False)

personaje_cayendo_izq = girar_png(personaje_cayendo_der,True,False)
personaje_peleando_izq = girar_png(personaje_peleando_der,True,False)
personaje_muriendo_izq = girar_png(personaje_muriendo_der,True,False)
#Animaciones del personaje
diccionario_acciones = {}

diccionario_acciones = { "derecha": {
                "quieto":  personaje_quieto_der,
                "corriendo": personaje_corriendo_der,
                "saltando": personaje_saltando_der,
                "cayendo": personaje_cayendo_der,
                "atacando": personaje_peleando_der,
                "muriendo": personaje_muriendo_der,},
            "izquierda": {
                "quieto": personaje_quieto_izq,
                "corriendo": personaje_corriendo_izq,
                "saltando": personaje_saltando_izq,
                "cayendo": personaje_cayendo_izq,
                "atacando": personaje_peleando_izq,
                "muriendo": personaje_muriendo_izq
            }
        }


#Medidas del personaje
LARGO_PLYER = 100
ANCHO_PLYER = 150
#Posicion incial del personaje
pos_inicial_lvl_1 = (150,500)
pos_inicial_lvl_2 = (319,160)






 




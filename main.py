import pygame,sys

from Constantes.Constantes_juego import *
from clases import *
from nivel_uno import Nivel_uno
from nivel_dos import Nivel_dos
from APIFORMS.GUI_form_prueba import *
from APIFORMS.GUI_form_menu_inicio import *

 
#Creacion de ventana
PANTALLA = pygame.display.set_mode((LARGO,ANCHO))

#Inicio juego
pygame.init()
pygame.display.set_caption("ApoloGame")
clock = pygame.time.Clock()

#Musica
# pygame.mixer.music.load("sonidos/music.ogg")
# pygame.mixer.music.play(-1)

form_principal = Form_menu_inicio(PANTALLA,773, 321,100,100,"Green","Gold",5,True,"Fondos/fondo_inicio_2.0.png")

# nivel_uno = Nivel_uno(PANTALLA)
# nivel_dos = Nivel_dos(PANTALLA)

while(True):
    clock.tick(FPS) 
    eventos = pygame.event.get()
    for evento in eventos:
        # print(ev  ento)
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:  
                print(evento.pos)
    form_principal.update(eventos)
                
    pygame.display.flip()

#(626, 467)
# (1223, 518)

   
   
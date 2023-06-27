import pygame,sys
from pygame.locals import *
from APIFORMS.GUI_form_prueba import Form_prueba

pygame.init()

W = 1900
H = 1000
FPS = 60
reloj = pygame.time.Clock()
pantanlla = pygame.display.set_mode((W,H)) 
form_prueba = Form_prueba(pantanlla,300,300,1300,350,"Blue","Gold",5)
seguir = True
while(seguir):
    reloj.tick(FPS)
    eventos = pygame.event.get()
    for event in eventos:
        if event.type == pygame.QUIT:
            seguir = False
    pantanlla.fill("Black")
    form_prueba.update(eventos)    
    pygame.display.flip()
pygame.quit()
sys.exit()
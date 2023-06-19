import pygame
from config import obtener_rectangulos
# piso_lados = obtener_rectangulos(pisonuevo)
def rectangulos_convertidos(lista_rectangulos):
    lista_nueva = []
    for rectangulo in lista_rectangulos:
        rectangulo_nuevo = obtener_rectangulos(rectangulo)
        lista_nueva.append(rectangulo_nuevo)
    return lista_nueva
 

# piso = Plataforma(0,700,435,60)
piso_nuevo = pygame.Rect(0,650,435,60)
caja_grande = pygame.Rect(435,710,125,125)
caja_chica = pygame.Rect(550,770,60,60)
piso_abajo = pygame.Rect(415,825,445,60)
sobre_piso = pygame.Rect(860,765,245,60) 
escotilla = pygame.Rect(1100,540,150,300)
piso_arriba = pygame.Rect(1220,420,670,60)
plataformas = [piso_nuevo,piso_abajo,piso_arriba,escotilla,caja_grande,caja_chica,sobre_piso]

lista_con_rectangulos_de_colision = rectangulos_convertidos(plataformas)

import pygame
from config import obtener_rectangulos
# piso_lados = obtener_rectangulos(pisonuevo)
def rectangulos_convertidos(lista_rectangulos):
    lista_nueva = []
    for rectangulo in lista_rectangulos:
        rectangulo_nuevo = obtener_rectangulos(rectangulo)
        lista_nueva.append(rectangulo_nuevo)
    return lista_nueva
 


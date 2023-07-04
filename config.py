import pygame
def girar_png(lista,flip_x,flip_y):
    nueva_lista = []
    for imagen in lista:        
        nueva_lista.append(pygame.transform.flip(imagen,flip_x,flip_y))
    return nueva_lista
def escalar_png(lista,tamaño):
    for i in range(len(lista)):
        lista[i] = pygame.transform.scale(lista[i],tamaño)

def obtener_rectangulos(principal:pygame.Rect)->dict:
    diccionario_rect = {}
    diccionario_rect["main"] = principal
    diccionario_rect["bottom"] = pygame.Rect(principal.left,principal.bottom - 10,principal.width,10)
    diccionario_rect["top"] = pygame.Rect(principal.left,principal.top,principal.width,10)
    diccionario_rect["left"] = pygame.Rect(principal.left,principal.top + diccionario_rect["bottom"].height,5,principal.height - diccionario_rect["bottom"].height*2)
    diccionario_rect["right"] = pygame.Rect(principal.right - 6,principal.top + diccionario_rect["bottom"].height,5,diccionario_rect["left"].height)    
    return diccionario_rect






import pygame
#FPS
FPS = 10
#Pantalla medidas 
LARGO = 1900
ANCHO = 1000

moneda_moviendose_lvl_1 = [
                pygame.image.load("monedas/monedaNo1_00.png"),
                pygame.image.load("monedas/monedaNo1_01.png"),
                pygame.image.load("monedas/monedaNo1_02.png"),
                pygame.image.load("monedas/monedaNo1_03.png")
                ]
moneda_moviendose_lvl_2 = [
                pygame.image.load("monedas/monedaNo2_00.png"),
                pygame.image.load("monedas/monedaNo2_01.png"),
                pygame.image.load("monedas/monedaNo2_02.png"),
                pygame.image.load("monedas/monedaNo2_03.png")
                ]

moneda_moviendose_lvl_3 = [
                pygame.image.load("monedas/monedaNo10_00.png"),
                pygame.image.load("monedas/monedaNo10_01.png"),
                pygame.image.load("monedas/monedaNo10_02.png"),
                pygame.image.load("monedas/monedaNo10_03.png")
                ]


calavera_moviendose = [
                pygame.image.load("item_peligrosos/36.png"),
                pygame.image.load("item_peligrosos/37.png"),
                pygame.image.load("item_peligrosos/38.png"),
                pygame.image.load("item_peligrosos/39.png"),
                pygame.image.load("item_peligrosos/40.png"),
                pygame.image.load("item_peligrosos/41.png"),
                pygame.image.load("item_peligrosos/42.png"),
                pygame.image.load("item_peligrosos/43.png")
                ]
enemigo_trampa = [
                pygame.image.load("enemigo_trampa/0.png"),
                pygame.image.load("enemigo_trampa/1.png"),
                pygame.image.load("enemigo_trampa/2.png"),
                pygame.image.load("enemigo_trampa/3.png"),
                ]

acciones_tram_enemig = {
    "izquierda":
    {
        "quieto": enemigo_trampa},
    "derecha": {
        "quieto": enemigo_trampa
        }
}

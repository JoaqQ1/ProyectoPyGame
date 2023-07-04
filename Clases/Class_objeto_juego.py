import pygame,sqlite3
from config import obtener_rectangulos

class Objeto_Juego:
    def __init__(self,path_img,tamaño_rect,pos_inicial):
        self.image = pygame.image.load(path_img)
        self.superficie = pygame.transform.scale(self.image,tamaño_rect)
        self.rect = self.superficie.get_rect()        
        self.rect.center = pos_inicial
        self.lados = obtener_rectangulos(self.rect)
        self.posicion_inicial = self.retornar_pos_inicial()
        estado_sonido = self.obtener_estado()
        self.estado_sonido = estado_sonido

    def retornar_pos_inicial(self):
        posiciones = {}
        
        posiciones["mainx"] = self.lados["main"].x
        posiciones["mainy"] = self.lados["main"].y

        posiciones["topx"] = self.lados["top"].x
        posiciones["topy"] = self.lados["top"].y

        posiciones["bottomx"] = self.lados["bottom"].x
        posiciones["bottomy"] = self.lados["bottom"].y
        
        posiciones["rightx"] = self.lados["right"].x
        posiciones["righty"] = self.lados["right"].y

        posiciones["leftx"] = self.lados["left"].x
        posiciones["lefty"] = self.lados["left"].y
        return posiciones
    
    def draw(self,pantalla):
        pantalla.blit(self.superficie,self.lados["main"])

    def obtener_estado(self):
        with sqlite3.connect("sonido.db") as conexion:
            try:
                cursor = conexion.cursor()
                sentencia = "SELECT estado FROM Sonido"
                cursor.execute(sentencia)
                resultado = cursor.fetchone()
                if resultado is not None:
                    estado = resultado[0]
                    return estado
                else:
                    print("No se encontró ningún estado en la base de datos.")
                    return None

            except Exception as e:
                print(f"Error: {e}")




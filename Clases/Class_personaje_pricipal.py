import pygame,sqlite3

from Clases.Class_personaje import Personaje
from Clases.Class_proyectil import Proyectil
from funciones import *

class Personaje_principal(Personaje):
    def __init__(self, path_img, tamaño_rect, pos_inicial, animaciones, velocidad):
        super().__init__(path_img, tamaño_rect, pos_inicial, animaciones, velocidad)
        #####SONIDOS####
        self.sonido_saltando = pygame.mixer.Sound("sonidos/sSpecialGet.ogg")
        self.sonido_disparo = pygame.mixer.Sound("sonidos/sFill.ogg")
        #####CARACTERISTICAS####
        self.golpeado = False
        self.llave = False
        self.score = 0
        self.vida = 3
        self.entro = False   
        self.arma_especial = False
        self.nivel_completo = 0  
        self.id = self.leer_id()


    def update(self,pantalla:pygame.Surface,plataformas,que_hace,ancho_pantalla,lista_enemigo,lista_trampas):

        if self.saltando:
            self.que_hace = "cayendo"
        if self.golpeado:
            que_hace = "muriendo"

        match que_hace:
            case "derecha":  
                if not self.saltando:
                    self.que_hace = "corriendo"
                    self.animar_personaje(pantalla)
                if self.detectar_colision_con_pared(plataformas) != 1:
                    self.mover_personaje(self.velocidad,ancho_pantalla[0])
                self.direccion = "derecha"

            case "izquierda":                
                if not self.saltando:
                    self.que_hace = "corriendo"
                    self.animar_personaje(pantalla)
                
                if self.detectar_colision_con_pared(plataformas) != -1:                                        
                    self.mover_personaje(self.velocidad * -1,ancho_pantalla[0])

                self.direccion = "izquierda"
                
            case "saltando":                
                if not self.saltando:
                    if self.estado_sonido == 1 or self.estado_sonido == None:
                        self.sonido_saltando.play()
                    self.que_hace = que_hace 
                    self.saltando = True
                    self.desplazamiento_y = self.capacidad_salto
                
            case "quieto":
                if not self.saltando:
                    self.que_hace = "quieto" 
                    self.animar_personaje(pantalla)
            case "atacando":                
                self.que_hace = "atacando"
                if self.estado_sonido == 1 or self.estado_sonido == None:
                    self.sonido_disparo.play()    
                proyectil = Proyectil("Proyectil/estrella_ninja.png",(30,30),self.lados["main"].centerx,self.lados["main"].centery)       
                self.lista_proyectiles.append(proyectil)           
                if not self.saltando:
                    self.animar_personaje(pantalla)
            
            case "muriendo":
                self.que_hace = "muriendo"
                self.animar_personaje(pantalla)
                ultima_animacion = len(self.animaciones[self.direccion][self.que_hace])
                if ultima_animacion == self.frame_actual:
                    if self.vida > 0:  
                        self.devolver_pos_inicial()
                        self.golpeado = False
                        self.vida -= 1
                    
            
        self.shoot(pantalla,30)
           
        if self.detectar_colision_enemigos(lista_enemigo) or self.colisiono_con_trampa(lista_trampas) or self.cayo_al_precipidio(pantalla):
            self.golpeado = True #----> NO ESTA COLICIONANDO CON EL NUEVO ENEMIGO,VERIFICAR BUG
        for enemigo in lista_enemigo:
            if self.detectar_colision_con_proyectil(enemigo.lista_proyectiles):
                self.golpeado = True
        
        self.aplicar_gravedad(pantalla,plataformas)




                        
    def detectar_colision_enemigos(self,lista_enemigo):
        if validar_lista(lista_enemigo):
            if len(lista_enemigo) > 0:
                for enemigo in lista_enemigo:
                    if enemigo.muerto == False:
                        if self.lados["right"].colliderect(enemigo.lados["main"]) or self.lados["left"].colliderect(enemigo.lados["main"]):
                            return  True
                        else:
                            return False
            else:
                return False
    def colisiono_con_trampa(self,lista_trampas):
        if validar_lista(lista_trampas):
            if len(lista_trampas) > 0:
                for trampas in lista_trampas:
                    if self.lados["main"].colliderect(trampas.lados["main"]):
                        return  True
                    
                    else:
                        return False
            else:
                return False

    def devolver_pos_inicial(self):

        self.lados["main"].x = self.posicion_inicial["mainx"]
        self.lados["main"].y = self.posicion_inicial["mainy"]
        
        self.lados["top"].x =    self.posicion_inicial["topx"]
        self.lados["top"].y =    self.posicion_inicial["topy"]

        self.lados["bottom"].x = self.posicion_inicial["bottomx"]
        self.lados["bottom"].y = self.posicion_inicial["bottomy"]
        
        self.lados["right"].x =  self.posicion_inicial["rightx"]
        self.lados["right"].y =  self.posicion_inicial["righty"]

        self.lados["left"].x =   self.posicion_inicial["leftx"]
        self.lados["left"].y =   self.posicion_inicial["lefty"]
        self.desplazamiento_y = 0


    def cayo_al_precipidio(self,pantalla:pygame.Surface):
        h = pantalla.get_height()
        if self.lados["main"].y > h:
            return True
        else:
            return False
    def leer_id(self):
        with sqlite3.connect("base_datos_jugador.db") as conexion:
            try:
                cursor = conexion.cursor()
                sentencia = "select max(id) from Jugador"
                cursor.execute(sentencia)
                resultado = cursor.fetchone()
                id_maximo = resultado[0] if resultado[0] is not None else 0                
                print("ID encontrado exitosamente:", id_maximo)
                return id_maximo
            except:
                print("error en obetener el id")

    
        
        

import pygame,sys,sqlite3
from modo import *
class Nivel:
    def __init__(self,pantalla:pygame.Surface,personaje_principal,lista_plataformas,imagen_fondo,lista_enemigos,lista_items,lista_trampas):
        ##### ATRIBUTOS #######
        self._slave = pantalla
        self.jugador = personaje_principal
        self.plataformas = lista_plataformas        
        self.imagen_fondo = imagen_fondo
        self.enemigos = lista_enemigos
        self.items = lista_items
        self.trampas = lista_trampas
        #####################
        w = self._slave.get_width()
        h = self._slave.get_width()

        game_over = pygame.image.load("game_over/game_over.png")
        game_over = pygame.transform.scale(game_over,(w,h))
        win = pygame.image.load("next_lvl/win.png")
        win = pygame.transform.scale(win,(w,h))
        
        self.win = win
        self.game_over = game_over
        self.calcular = True
        #####################
        self.fuente = pygame.font.SysFont("Arial",35)
        self.total_game_time = 60
        self.tiempo_en_pantalla = 0
        self.mensaje_bonificacion = "No hubo bonificacion"
        self.segundo_anterior = 0
        self.puntaje_sumado = True
        #####################

    def update(self,lista_eventos):  
        tiempo = pygame.time.get_ticks()
        
        for event in lista_eventos:
            if event.type == pygame.KEYDOWN:         
                if event.key == pygame.K_TAB:            
                    cambiar_modo() 
            elif event.type == pygame.QUIT: 
                sys.exit()
        
        
        if self.jugador.vida > 0 and self.jugador.entro == False:
            
            segundo = int(tiempo / 1000)
            if segundo != self.segundo_anterior and self.total_game_time > 0:
                self.total_game_time -= 1
            self.segundo_anterior = segundo
            
            #Tiempo en pantalla en segundos
            self.tiempo_en_pantalla = self.fuente.render(f"TIME:{self.total_game_time}\nVIDA:{self.jugador.vida}",False,"Red")
            self.actualizar_pantalla()            
            self.dibujear_rectangulos()
        
        elif self.jugador.entro:
            
            self.calcular_puntaje_tiempo()
            self._slave.blit(self.win,(0,0))
            texto = self.fuente.render(f"""
Felicidades completo el nivel.
SCORE: {self.jugador.score}-{self.mensaje_bonificacion}
VIDA: {self.jugador.vida}
TIEMPO:{self.total_game_time}                
""",False,"Blue")            
            self._slave.blit(texto,(0, 800))
            
            if self.puntaje_sumado:
                jugador = self.retornar_datos_personaje()
                self.update_datos(jugador)
                self.puntaje_sumado = False

        else:
            self._slave.blit(self.game_over,(0,0))
        self._slave.blit(self.tiempo_en_pantalla,(0, 0))




    def leer_inputs(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:        
            accion = "saltando"
        elif keys[pygame.K_LEFT]:
            accion = "izquierda"
        elif keys[pygame.K_RIGHT]:
            accion = "derecha"
        elif keys[pygame.K_a]:
            accion = "atacando"
        else:
            accion = "quieto"
        return accion
    
    def retornar_medidas_superficie(self):
        largo = self._slave.get_width()
        alto = self._slave.get_height()
        medidas = (largo,alto)
        return  medidas
    
    def dibujear_rectangulos(self):
        if get_debug(): 
            #Personaje
            for lado in self.jugador.lados:
                pygame.draw.rect(self._slave,"Red",self.jugador.lados[lado],1)

            #Enemigo
            if len(self.enemigos) > 0:
                for enemigo in self.enemigos:
                    for lado in enemigo.lados:
                        pygame.draw.rect(self._slave,"Red",enemigo.lados[lado],1)
            
            #Pisos-Plataformas
            for i in range(len(self.plataformas)):
                for lado in self.plataformas[i]:   
                    pygame.draw.rect(self._slave,"Blue",self.plataformas[i][lado],1)
    def actualizar_pantalla(self):
        ancho_pantalla = self.retornar_medidas_superficie()
        if self.jugador.golpeado == False:
            que_hace = self.leer_inputs()
        else:
            que_hace = "muriendo"
       
        self._slave.blit(self.imagen_fondo,(0,0))
        self.jugador.update(self._slave,self.plataformas,que_hace,ancho_pantalla,self.enemigos,self.trampas)

        for item in self.items:
            item.update(self.jugador,self._slave)
            if item.recogido:
                self.items.remove(item)
        for trampa in self.trampas:
            trampa.update(self._slave)
        if len(self.enemigos) > 0:
            for enemigo in self.enemigos:
                if enemigo.muerto == False:
                    enemigo.update(self.plataformas,self._slave,self.jugador)
                else:
                    self.enemigos.remove(enemigo)
       


    def calcular_puntaje_tiempo(self):    
        if self.calcular:   
            if self.total_game_time > 40 and self.total_game_time <= 50:
                self.jugador.score += 500                
                self.mensaje_bonificacion = "Se bonificaron 300 puntos"
            elif self.total_game_time > 30 and self.total_game_time <= 40:
                self.jugador.score += 300                
                self.mensaje_bonificacion = "Se bonificaron 300 puntos"

            elif self.total_game_time > 20 and self.total_game_time <= 30:
                self.jugador.score += 200
                self.mensaje_bonificacion = "Se bonificaron 300 puntos"

            elif self.total_game_time > 10 and self.total_game_time <= 20:
                self.jugador.score += 100
                self.mensaje_bonificacion = "Se bonificaron 300 puntos"

            elif self.total_game_time == 0:
                self.jugador.score -= 200
                self.mensaje_bonificacion = "Se penalizaron 200 puntos, por terminar fuera de tiempo" 

            self.calcular = False
           
        
    def retornar_datos_personaje(self):
        with sqlite3.connect("base_datos_jugador.db") as conexion:
            try:
                cursor = conexion.cursor()
                sentencia = "SELECT * FROM Jugador WHERE id = ?"
                cursor.execute(sentencia, (self.jugador.id,))
                jugador = cursor.fetchone()
                
                return jugador
            except Exception as e:
                print(f"Error al retornar los datos: {e}")

    def update_datos(self,jugador):
        with sqlite3.connect("base_datos_jugador.db") as conexion:
            try:
                cursor = conexion.cursor()
                
                score = jugador[2]  # Índice 1 para el puntaje en la tabla
                nivel = jugador[3]  # Índice 2 para el nivel en la tabla
                
                if nivel < self.jugador.nivel_completo: # Solo si se esta jugando el nivel por primera vez se van sumar el puntaje 
                    score += self.jugador.score
                    nivel = self.jugador.nivel_completo

                sentencia = "UPDATE Jugador SET puntaje = ?, nivel = ? WHERE id = ?"
                cursor.execute(sentencia, (score,nivel, self.jugador.id))
                
                conexion.commit()  # Guardar los cambios en la base de datos
                print("Se sumo con exito el puntaje")
            except Exception as e:
               print(f"Error al sumar los datos: {e}")

  

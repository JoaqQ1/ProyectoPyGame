import pygame
import sqlite3 
from pygame.locals import *

from APIFORMS.GUI_form import *
from APIFORMS.GUI_form_ingresar_nombre import *





class Form_menu_inicio(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border="Black", border_size=-1, active=True,path_fondo=""):
        super().__init__(screen, x, y, w, h, color_background, color_border, border_size, active,path_fondo)
        self.volumen = 0.2
        self.flag_play = True
        self.create_table()
        pygame.mixer.init()

        ###### CONTROLES #######################
        self.form_nombre = Form_ingrese_nombre(self._master,
                             650, 251,700,500,(220,0,220),"Green",True,"APIFORMS/Window.png",100,10)
            
        ###### AGREGO CONTROLES A LA LISTA ######
        self.lista_widgets.append(self.form_nombre)
        ##########################################

        pygame.mixer.music.load("sonidos/music.ogg")
        pygame.mixer.music.set_volume(self.volumen)
        pygame.mixer.music.play(-1)
        self.render()
    
    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            if self.active:
                self.draw()
                self.render()
                for widged in self.lista_widgets:
                    widged.update(lista_eventos)
                # self.update_volume(lista_eventos)
        else:
            self.hijo.update(lista_eventos)
    
   

    


    def create_table(self):
        with sqlite3.connect("base_datos_jugador.db") as conexion:
            try:
                sentenencia = '''
                create table Jugador
                (
                    id integer primary key autoincrement,
                    nombre text, 
                    puntaje integer,
                    nivel integer 
                )
                '''
                conexion.execute(sentenencia)
                print("Tabla creada")
            except Exception as e:
                print(f"Error: {e}")
                
        
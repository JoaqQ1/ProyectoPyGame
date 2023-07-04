import pygame
import sqlite3
from pygame.locals import *
from APIFORMS.GUI_button_image import *
from APIFORMS.GUI_textbox import *
from APIFORMS.GUI_form import *
from APIFORMS.GUI_label import *
from APIFORMS.GUI_form_play import *


class Form_ingrese_nombre(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border
                 ,active,path_imagen,margen_y,margen_x):
        super().__init__(screen, x, y, w, h, color_background, color_border, active)
        
        aux_imagen = pygame.image.load(path_imagen)
        aux_imagen = pygame.transform.scale(aux_imagen,(w,h))
        
        self._slave = aux_imagen        

        self.margen_y = margen_y
        
        #################CONTROLES#################
        self.lbl_name = Label(self._slave,x = margen_x + 100 ,y = 20, w=w/2-margen_x-10,h=50,
                       text="NOMBRE",font = "Verdana",font_size=30,font_color="White",path_image="APIFORMS/bar.png")
        # self.textbox = TextBox(self._slave,margen_x + 100 ,40,w/2-margen_x-200,100,400,50,"Gray","White","Orange","Black",3,"Comic Sans",15,"Red")
        self.textbox = TextBox(self._slave,x,y,50,250,400,30,"Gray","White","Orange","Black",3,"Comic Sans",15,"Red")

        self.btn_commit = Button_Image(self._slave,x,y,120,300,250,100,"next/next.png",self.btn_next,"lala")
        ##########################################


        ##########################################
        ###### AGREGO CONTROLES A LA LISTA ######
        self.lista_widgets.append(self.lbl_name)
        self.lista_widgets.append(self.textbox)
        self.lista_widgets.append(self.btn_commit)
      

    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            if self.active:
                self.draw()
                self.render()
                for widged in self.lista_widgets:
                    widged.update(lista_eventos)
        else:
            self.hijo.update(lista_eventos) 
    
    def btn_next(self,texto):
        form_play = Form_play(self._master,650, 251,500,700,(220,0,220),"Green",True,"APIFORMS/Window.png",100,10)
        self.show_dialog(form_play)
        nombre = self.textbox.get_text()
        if nombre == '':
            nombre = "Apolo" 
        self.guardar_jugador(nombre)

    def guardar_jugador(self,nombre):
        try:
            # Abrir la conexión a la base de datos
            with sqlite3.connect("base_datos_jugador.db") as conexion:
                # Crear un cursor para ejecutar consultas
                cursor = conexion.cursor()

                # Definir los valores del jugador
                nombre_jugador = nombre
                score = 0
                nivel = 0

                # Ejecutar la consulta utilizando marcadores de posición
                sentencia = "INSERT INTO Jugador (nombre, puntaje, nivel) VALUES (?, ?, ?)"
                cursor.execute(sentencia, (nombre_jugador, score, nivel))

                # Guardar los cambios en la base de datos
                conexion.commit()

                print("Nombre registrado correctamente")
        except sqlite3.Error as error:
            print("Error al ingresar el nombre:", error)

        






        




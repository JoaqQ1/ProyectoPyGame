import pygame,sqlite3
from pygame.locals import *
from APIFORMS.GUI_button_image import *
from APIFORMS.GUI_form import *
from APIFORMS.GUI_label import *
from APIFORMS.GUI_slider import *
from APIFORMS.GUI_form_contenerdor_lvls import *
from manejador_niveles import *



class Form_lvls(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border
                 ,active,path_imagen,fondo):
        super().__init__(screen, x, y, w, h, color_background, color_border, active,path_fondo=fondo)
        
        aux_imagen = pygame.image.load(path_imagen)
        aux_imagen = pygame.transform.scale(aux_imagen,(w,h))
        self._slave = aux_imagen 
        self.manejardor_de_niveles = Manejador_niveles(self._master)
        
        
        nivel_completado = self.retornar_nivel_completado()

        #################CONTROLES#################
        self.lbl_encabezado = Label(self._slave,x = 150 ,y = 20, w=300,h=50,
                       text="LEVELS",font = "Verdana",font_size=30,font_color="White",path_image="APIFORMS/bar.png")

        self.btn_lvl_1 = Button_Image(self._slave,x,y,140,100,300,100,"Levels_png/nivel_1.png",self.entrar_nivel,"nivel_uno")
        
        bandera_2_completado = 0
        bandera_3_completado = 0
        path_lvl_2 = "Levels_png/lvl_2_bloqueado.png"
        path_lvl_3 = "Levels_png/lvl_3_bloqueado.png"
        if nivel_completado >= 2:
            path_lvl_2 = "Levels_png/lvl_2_verde.png"
            bandera_2_completado = 1
        if nivel_completado >= 3:
            path_lvl_3 = "Levels_png/LVL_3.png"
            bandera_3_completado = 1
        if bandera_2_completado:
            self.btn_lvl_2_desbloqueado = Button_Image(self._slave,x,y,100,250,350,250,path_lvl_2,self.entrar_nivel,"nivel_dos")
        else:
            self.btn_lvl_2_desbloqueado = Button_Image(self._slave,x,y,100,250,350,100,path_lvl_2,self.nivel_bloqueado,"nivel_dos")
        if bandera_3_completado:
            self.btn_lvl_3_desbloqueado = Button_Image(self._slave,x,y,100,400,350,150,path_lvl_3,self.entrar_nivel,"nivel_tres")
        else:
            self.btn_lvl_3_desbloqueado = Button_Image(self._slave,x,y,100,400,350,150,path_lvl_3,self.nivel_bloqueado,"nivel_tres")


        self.btn_return = Button_Image(self._slave,x,y,100,550,300,100,"Levels_png/return.png",self.btn_home_click,"lala")
        
         
        ###### AGREGO CONTROLES A LA LISTA ######
        self.lista_widgets.append(self.btn_lvl_1)
        self.lista_widgets.append(self.btn_lvl_2_desbloqueado)
        self.lista_widgets.append(self.btn_lvl_3_desbloqueado)
        self.lista_widgets.append(self.btn_return)
        self.lista_widgets.append(self.lbl_encabezado)
        ##########################################
      
        
        

        
    def btn_home_click(self,parametro):
        self.end_dialog()
    
    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            if self.active:
                self.draw()
                self.render()
                for widget in self.lista_widgets:
                    widget.update(lista_eventos)
        else:
            self.hijo.update(lista_eventos)

    def entrar_nivel(self,nombre_lvl):
       
        nivel = self.manejardor_de_niveles.get_nivel(nombre_lvl)
        form_contenedor_lvl = Form_contenedor_lvls(self._master,nivel)
        self.show_dialog(form_contenedor_lvl)

    def nivel_bloqueado(self,texto):
        print("Todavia no puedes ingresar al nivel")
        pass

    def leer_ultimo_id(self):
        with sqlite3.connect("base_datos_jugador.db") as conexion:
            try:
                cursor = conexion.cursor()
                sentencia = "select max(id) from Jugador"
                cursor.execute(sentencia)
                resultado = cursor.fetchone()
                id_maximo = resultado[0] if resultado[0] is not None else 0                
                return id_maximo
            except:
                print("error en obetener el id")

    def retornar_nivel_completado(self):
        id = self.leer_ultimo_id()
        with sqlite3.connect("base_datos_jugador.db") as conexion:
            try:
                cursor = conexion.cursor()
                sentencia = "SELECT * FROM Jugador WHERE id = ?"
                cursor.execute(sentencia, (id,))
                jugador = cursor.fetchone()
                return jugador[3]
            except Exception as e:
                print(f"Error al retornar los datos: {e}")
    
    


        




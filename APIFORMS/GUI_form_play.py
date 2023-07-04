import pygame,sqlite3
from pygame.locals import *
from APIFORMS.GUI_button_image import *
from APIFORMS.GUI_form import *
from APIFORMS.GUI_label import *
from APIFORMS.GUI_form_setting import *
from APIFORMS.GUI_form_lvls import *
from APIFORMS.GUI_form_menu_scrore import *
from APIFORMS.GUI_form_ingresar_nombre import *





class Form_play(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border
                 ,active,path_imagen,margen_y,margen_x):
        super().__init__(screen, x, y, w, h, color_background, color_border, active)
        
        aux_imagen = pygame.image.load(path_imagen)
        aux_imagen = pygame.transform.scale(aux_imagen,(w,h))
        
        self._slave = aux_imagen        

        self.margen_y = margen_y
        
        #################CONTROLES#################
        self.lbl_menu = Label(self._slave,x = margen_x + 100 ,y = 20, w=w/2-margen_x-10,h=50,
                       text="MENU",font = "Verdana",font_size=30,font_color="White",path_image="APIFORMS/bar.png")
        self.btn_play = Button_Image(self._slave,x,y,140,200,200,50,"APIFORMS/menupngs/play.png",self.btn_play_click,"lala")
        self.btn_setting = Button_Image(self._slave,x,y,140,350,250,50,"APIFORMS/menupngs/setting_amarillo.png",self.btn_settings_click,"lala")
        self.btn_finish = Button_Image(self._slave,x,y,120,500,250,100,"APIFORMS/menupngs/finish.png",self.btn_finish_click,"lala")
        ##########################################btn_finish_click
        self.btn_score = Button_Image(self._slave,x,y,120,395,250,100,"Score_Credit/Score.png",self.btn_score_click,"lala")


        ##########################################
        ###### AGREGO CONTROLES A LA LISTA ######
        self.lista_widgets.append(self.lbl_menu)
        self.lista_widgets.append(self.btn_play)
        self.lista_widgets.append(self.btn_setting)
        self.lista_widgets.append(self.btn_finish)
        self.lista_widgets.append(self.btn_score)


        

    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            if self.active:
                self.draw()
                self.render()
                for widged in self.lista_widgets:
                    widged.update(lista_eventos)
        else:
            self.hijo.update(lista_eventos)
    
    def btn_play_click(self,texto):
        form_lvls = Form_lvls(self._master,
                             650, 251,500,700,(220,0,220),"Green",True,"APIFORMS/Window.png","Fondos/fondo_settin.png")
        self.show_dialog(form_lvls)
            
       
    def btn_settings_click(self,texto):
       
        form_settin = Form_setting(self._master,400, 251,800,400,(220,0,220),"Green",True,"APIFORMS/Window.png",10,"Fondos/fondo_settin.png")
        self.show_dialog(form_settin)

    def btn_finish_click(self,texto):
        pygame.quit()
   
    def btn_score_click(self,texto):
        score = self.traer_mejores_puntajes()
        form_score = FormMenuScore(self._master,400,24,500,550,(230,0,220),"Black",True,"APIFORMS/Window.png",score,100,10,10,"Fondos/fondo_settin.png")
        self.show_dialog(form_score)

    def traer_mejores_puntajes(self):
        with sqlite3.connect("base_datos_jugador.db") as conexion:
            try:
                lista_jugadores = []
                cursor = conexion.cursor()
                sentencia = "SELECT nombre, puntaje FROM Jugador ORDER BY puntaje DESC LIMIT 3"
                cursor.execute(sentencia)
                for fila in cursor:
                    dic_score = {}
                    dic_score["Jugador"] = fila[0]
                    dic_score["Score"] = fila[1]
                    lista_jugadores.append(dic_score)

                return lista_jugadores
            except Exception as e:
                print(f"Error al retornar los datos: {e}")
            
            




        




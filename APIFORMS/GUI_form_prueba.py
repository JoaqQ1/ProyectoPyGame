import pygame
from pygame.locals import *

from APIFORMS.GUI_button import *
from APIFORMS.GUI_button_image import *
from APIFORMS.GUI_slider import *
from APIFORMS.GUI_label import *
from APIFORMS.GUI_textbox import *
from APIFORMS.GUI_widget import *
from APIFORMS.GUI_form import *
from APIFORMS.GUI_form_menu_scrore import *
from APIFORMS.GUI_form_play import *

class Form_prueba(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border="Black", border_size=-1, active=True,path_fondo=""):
        super().__init__(screen, x, y, w, h, color_background, color_border, border_size, active,path_fondo)
        self.volumen = 0.2
        self.flag_play = True
        pygame.mixer.init()

        ###### CONTROLES #######################
        self.textbox = TextBox(self._slave,x,y,50,50,150,30,"Gray","White","Red","Blue",2,font="Comic Sans",font_size=15,font_color="Black")
        self.btn_play = Button(self._slave,x,y,100,100,100,50,"Red","Blue",self.btn_play_click,"Nombre","Pausa",font="Verdana",font_size=15,font_color="White")       
        self.label_volumen = Label(self._slave,650,190,100,50,"20%","Comic Sans",15,"White","APIFORMS/menupngs/label.png")
        self.slider_volumen = Slider(self._slave,x,y,100,200,500,15,self.volumen,"Gold","White")
        self.btn_tabla = Button_Image(self._slave,x,y,255,100,60,60,"APIFORMS/menupngs/0.png",self.btn_tabla_click,"lala")
        self.btn_lvl = Button_Image(self._slave,x,y,400,100,60,60,"APIFORMS/Menu_BTN.png",self.btn_lvl_click,"lala")        
        ###### AGREGO CONTROLES A LA LISTA ######
        self.lista_widgets.append(self.textbox)
        self.lista_widgets.append(self.btn_play)
        self.lista_widgets.append(self.label_volumen)
        self.lista_widgets.append(self.slider_volumen)
        self.lista_widgets.append(self.btn_tabla)
        self.lista_widgets.append(self.btn_lvl)
        ##########################################

        pygame.mixer.music.load("sonidos/music.ogg")
        pygame.mixer.music.set_volume(self.volumen)
        pygame.mixer.music.play(-1)
        self.render()
        # self._btn_home = Button_Image(
        #         screen=self._slave,
        #         x = w - 70,
        #         y = h - 70,
        #         master_x = x,
        #         master_y = y,
        #         w = 50,
        #         h = 50,
        #         color_background = (255,0,0),
        #         color_border = (255,0,255),
        #         onclick = self.btn_home_click,
        #         onclick_param = "",
        #         text="",
        #         font="Verdana",
        #         font_size= 15,
        #         font_color=(0,255,0),
        #         path_image="APIFORMS/menupngs/2.png")
        # self.lista_widgets.append(self._btn_home)
    
    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            if self.active:
                self.draw()
                self.render()
                for widged in self.lista_widgets:
                    widged.update(lista_eventos)
                self.update_volume(lista_eventos)
        else:
            self.hijo.update(lista_eventos)
    
    def render(self):
        self._slave.fill(self._color_background)

    def btn_play_click(self,texto):
       
        if self.flag_play:
            pygame.mixer.music.pause()
            self.btn_play._color_background = "Cyan"
            self.btn_play._font_color = "Red"
            self.btn_play.set_text("Play")
        else:   
            pygame.mixer.music.unpause()
            self.btn_play._color_background = "Red"
            self.btn_play._font_color = "White"
            self.btn_play.set_text("Pause")
        self.flag_play = not self.flag_play


    def update_volume(self,lista_eventos):
        self.volumen = self.slider_volumen.value
        # self.label_volumen.update(lista_eventos)
        self.label_volumen.set_text(f"{round(self.volumen * 100)}%")
        pygame.mixer.music.set_volume(self.volumen)
    
    def btn_lvl_click(self,texto):
        # print(texto)   
        form_lvl = Form_play(self._master,
                             500,25,1000,1050,(220,0,220),"Green",True,"APIFORMS/Window.png",100,10)
        self.show_dialog(form_lvl)


    def btn_tabla_click(self,texto):
        dict_score = [{"Jugador":"Joaco","Score":1900},
                      {"Jugador":"Martin","Score":1},
                      {"Jugador":"Lucas","Score":9}]
        
        form_puntaje = FormMenuScore(self._master,
                                     250,
                                     25,
                                     500,
                                     550,
                                     (220,0,220),
                                     "White",
                                     True,
                                     "APIFORMS/Window.png",
                                     dict_score,
                                     100,
                                     10,
                                     10)
        self.show_dialog(form_puntaje)
    def btn_home_click(self,texto):
        pass
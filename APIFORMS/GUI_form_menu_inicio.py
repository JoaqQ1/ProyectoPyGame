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
from APIFORMS.GUI_form_prueba import *



class Form_menu_inicio(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border="Black", border_size=-1, active=True,path_fondo=""):
        super().__init__(screen, x, y, w, h, color_background, color_border, border_size, active,path_fondo)
        self.volumen = 0.2
        self.flag_play = True
        pygame.mixer.init()

        ###### CONTROLES #######################

        self.form_play = Form_play(self._master,
                             650, 251,500,700,(220,0,220),"Green",True,"APIFORMS/Window.png",100,10)
            
        ###### AGREGO CONTROLES A LA LISTA ######
        self.lista_widgets.append(self.form_play)
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


    def btn_setting_click(self,texto):
        form_setting = Form_prueba(self._master,500,250,900,350,"Blue","Gold",5,True,"Fondos/fondo_settin.png")
        self.show_dialog(form_setting)
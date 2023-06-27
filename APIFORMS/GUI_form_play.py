import pygame
from pygame.locals import *
from APIFORMS.GUI_button_image import *
from APIFORMS.GUI_form import *
from APIFORMS.GUI_label import *
from APIFORMS.GUI_form_setting import *
from APIFORMS.GUI_form_lvls import *




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
        # self.btn_play = Button(self._slave,x,y,200,200,100,50,"Red","Blue",self.btn_play_click,"Nombre","PLAY",font="Verdana",font_size=15,font_color="White")
        self.btn_play = Button_Image(self._slave,x,y,140,200,200,50,"APIFORMS/menupngs/play.png",self.btn_play_click,"lala")
        self.btn_setting = Button_Image(self._slave,x,y,140,350,250,50,"APIFORMS/menupngs/setting_amarillo.png",self.btn_settings_click,"lala")
        self.btn_finish = Button_Image(self._slave,x,y,120,500,250,100,"APIFORMS/menupngs/finish.png",self.btn_finish_click,"lala")

        ##########################################
        ###### AGREGO CONTROLES A LA LISTA ######
        self.lista_widgets.append(self.lbl_menu)
        self.lista_widgets.append(self.btn_play)
        self.lista_widgets.append(self.btn_setting)
        self.lista_widgets.append(self.btn_finish)

        

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
        form_play = Form_lvls(self._master,
                             650, 251,500,700,(220,0,220),"Green",True,"APIFORMS/Window.png","Fondos/fondo_settin.png")
        self.show_dialog(form_play)
            
       
    def btn_settings_click(self,texto):
       
        form_settin = Form_setting(self._master,400, 251,800,400,(220,0,220),"Green",True,"APIFORMS/Window.png",10,"Fondos/fondo_settin.png")
        self.show_dialog(form_settin)
    def btn_finish_click(self,texto):
        pygame.quit()


        




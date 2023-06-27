import pygame
from pygame.locals import *
from APIFORMS.GUI_button_image import *
from APIFORMS.GUI_form import *
from APIFORMS.GUI_label import *
from APIFORMS.GUI_slider import *


class Form_setting(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border
                 ,active,path_imagen,margen_y,fondo):
        super().__init__(screen, x, y, w, h, color_background, color_border, active,path_fondo=fondo)
        
        aux_imagen = pygame.image.load(path_imagen)
        aux_imagen = pygame.transform.scale(aux_imagen,(w,h))
        
        self._slave = aux_imagen        
        self.margen_y = margen_y
        self.volumen = 0.2
        self.flag_play = True
        
        #################CONTROLES#################
        self.lbl_encabezado = Label(self._slave,x = 150 ,y = 10, w=300,h=30,
                       text="SETTIGNS",font = "Verdana",font_size=30,font_color="White",path_image="APIFORMS/bar.png")
        self.btn_play = Button(self._slave,x,y,200,100,100,50,"Red","Blue",self.btn_play_click,"Nombre","Pausa",font="Verdana",font_size=15,font_color="White")       
        self.label_volumen = Label(self._slave,650,290,100,50,"20%","Comic Sans",15,"White","APIFORMS/Table.png")
        self.slider_volumen = Slider(self._slave,x,y,100,300,500,15,self.volumen,"Yellow","Black")    
        ###### AGREGO CONTROLES A LA LISTA ######
        self.lista_widgets.append(self.btn_play)
        self.lista_widgets.append(self.label_volumen)
        self.lista_widgets.append(self.slider_volumen)
        self.lista_widgets.append(self.lbl_encabezado)

        ##########################################
        self._btn_home = Button_Image(
                screen=self._slave,
                x = w - 70,
                y = h - 70,
                master_x = x,
                master_y = y,
                w = 50,
                h = 50,
                color_background = (255,0,0),
                color_border = (255,0,255),
                onclick = self.btn_home_click,
                onclick_param = "",
                text="",
                font="Verdana",
                font_size= 15,
                font_color=(0,255,0),
                path_image="APIFORMS/home.png")
        self.lista_widgets.append(self._btn_home)



        
        
        

        
    def btn_home_click(self,parametro):
        self.end_dialog()
    
    def update(self, lista_eventos):
        if self.active:
            self.draw()
            self.render()
            for widget in self.lista_widgets:
                widget.update(lista_eventos)
            self.update_volume(lista_eventos)
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


        




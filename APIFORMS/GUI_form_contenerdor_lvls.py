import pygame
from pygame.locals import *
from APIFORMS.GUI_button_image import *
from APIFORMS.GUI_form import *
from APIFORMS.GUI_label import *
from APIFORMS.GUI_slider import *
from manejador_niveles import *



class Form_contenedor_lvls(Form):
    def __init__(self, screen:pygame.Surface,nivel):
        super().__init__(screen,0,0,screen.get_width(),screen.get_height())
        nivel._slave = self._slave
        self.nivel = nivel
        self.btn_vuelta_menu = Button_Image(self._slave,self._x,self._y,self._w-100,self._h -100,50,50,"APIFORMS/home.png",self.btn_home_click,"lala")
        self.lista_widgets.append(self.btn_vuelta_menu)
        

        
      
        
    def btn_home_click(self,texto):
        print(texto)
        self.end_dialog()
    
    def update(self, lista_eventos):
        self.nivel.update(lista_eventos)
        for widged in self.lista_widgets:
            widged.update(lista_eventos)
        
        self.draw()
        self.render()
        

       
    


        




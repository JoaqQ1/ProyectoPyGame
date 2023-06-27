import pygame
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
        
        
        
        #################CONTROLES#################
        self.lbl_encabezado = Label(self._slave,x = 150 ,y = 20, w=300,h=50,
                       text="LEVELS",font = "Verdana",font_size=30,font_color="White",path_image="APIFORMS/bar.png")

        self.btn_lvl_1 = Button_Image(self._slave,x,y,140,100,300,100,"Levels_png/nivel_1.png",self.entrar_nivel,"nivel_uno")
        self.btn_lvl_2 = Button_Image(self._slave,x,y,100,250,350,250,"Levels_png/lvl_2_verde.png",self.entrar_nivel,"nivel_dos")
        self.btn_return = Button_Image(self._slave,x,y,100,450,300,100,"Levels_png/return.png",self.btn_home_click,"lala")
        
         
        ###### AGREGO CONTROLES A LA LISTA ######
        self.lista_widgets.append(self.btn_lvl_1)
        self.lista_widgets.append(self.btn_lvl_2)
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
       
    


        




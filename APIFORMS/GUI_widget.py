import pygame
class Widget:
    def __init__(self,screen, x,y,w,h,color_background = "Black", color_border = "Red", border_size = -1,path_fondo=""):
        self._master = screen
        self._x = x
        self._y = y
        self._w = w
        self._h = h
        self._color_background = color_background
        self._color_border = color_border
        self._slave = None
        self.slave_rect = None
        self.border_size = border_size
        ##############
        if path_fondo != "":
            w = self._master.get_width()
            h = self._master.get_height()        
            fondo_imagen = pygame.image.load(path_fondo)
            fondo = pygame.transform.scale(fondo_imagen,(w,h))
            self.fondo = fondo
            self.tiene_fondo = True
        else:
            self.tiene_fondo = False
        
    
    def render(self):
        pass
    
    def update(self, lista_eventos):
        pass
    
    def draw(self):
        if self.tiene_fondo == False:
            self._master.blit(self._slave,self.slave_rect)
            # pygame.draw.rect(self._master, self._color_border, self.slave_rect, self.border_size)

        else: 
            self._master.blit(self.fondo,(0,0))
            self._master.blit(self._slave,self.slave_rect)

            # pygame.draw.rect(self._master, self._color_border, self.slave_rect, self.border_size)

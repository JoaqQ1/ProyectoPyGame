from pygame.locals import *
from nivel_uno import Nivel_uno
from nivel_dos import Nivel_dos

class Manejador_niveles:
    def __init__(self,pantalla) -> None:
        self._slave = pantalla
        self.niveles = {"nivel_uno" : Nivel_uno,
                        "nivel_dos": Nivel_dos}
    def get_nivel(self,nombre_nivel):
        return self.niveles[nombre_nivel](self._slave)

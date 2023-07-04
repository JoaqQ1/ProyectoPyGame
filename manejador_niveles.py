from pygame.locals import *
from nivel_uno import Nivel_uno
from nivel_dos import Nivel_dos
from nivel_tres import Nivel_tres


class Manejador_niveles:
    def __init__(self,pantalla) -> None:
        self._slave = pantalla
        self.niveles = {"nivel_uno" : Nivel_uno,
                        "nivel_dos": Nivel_dos,
                        "nivel_tres": Nivel_tres}
    def get_nivel(self,nombre_nivel):
        return self.niveles[nombre_nivel](self._slave)

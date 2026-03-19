    # TODO: implementa hacer_sonido, comportamiento, moverse
from abc import ABC, abstractmethod

class Mob(ABC):
    pass

class Vaca(Mob):
    pass
class Vaca(Mob):
    #"""Mob pasivo, suena 'Muuuu', camina lento."""
    def hacer_sonido(self):
        return "Muuuu"
    def comportamiento(self):
        return "pasivo"

    def moverse(self):
        return "camina lentamente"

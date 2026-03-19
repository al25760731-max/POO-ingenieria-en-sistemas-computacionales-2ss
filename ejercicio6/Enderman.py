from abc import ABC, abstractmethod

class Mob(ABC):
    pass

class Enderman(Mob):
    def hacer_sonido(self):
        return "sonido distorcionado"
    def comportamiento(self):
        return "neutral"

    def moverse(self):
        return "se teletransporta"
    pass
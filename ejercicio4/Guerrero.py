#clase hija guerrero
from Aventurero import Aventurero

class Guerrero(Aventurero):     
    def __init__(self, nombre, nivel, arma):
        super().__init__(nombre, nivel)
        self.arma = arma

    def usar_habilidad_especial(self):
        print(f"{self.nombre} ataca con su espada: {self.arma}")

#clase hija Mago
from Aventurero import Aventurero

class Mago(Aventurero):
    def __init__(self, nombre, nivel, hechizo):
        super().__init__(nombre, nivel)
        self.hechizo = hechizo


    def usar_habilidad_especial(self):
        super().usar_habilidad()
        print(f"{self.nombre} realiza su hechizo especial: {self.hechizo}")
#clase hija Mago
from Taberna import Taberna

class Mago(Taberna):
    def __init__(self, nombre, nivel, hechizo,habilidad_especial):
        super().__init__(nombre, nivel)
        self.hechizo = hechizo
        self.habilidad_especial = habilidad_especial

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"hechizo: {self.hechizo}")
        print(f"habilidad especial: {self.habilidad_especial}")

    def usar_habilidad_especial(self):
        print(f"{self.nombre} utiliza su habilidad especial: {self.habilidad_especial}")
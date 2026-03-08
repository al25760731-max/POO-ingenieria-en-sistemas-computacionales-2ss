#clase hija guerrero
from Taberna import Taberna

class Guerrero(Taberna):     
    def __init__(self, nombre, nivel, arma, habilidad_especial):
        super().__init__(nombre, nivel)
        self.arma = arma
        self.habilidad_especial = habilidad_especial

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"arma: {self.arma}")
        print(f"habilidad especial: {self.habilidad_especial}")

    def usar_habilidad_especial(self):
        print(f"{self.nombre} utiliza su habilidad especial: {self.habilidad_especial}")

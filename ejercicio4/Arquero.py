#clase hija Arquero
from Taberna import Taberna

class Arquero(Taberna):
    def __init__(self, nombre, nivel, arco,habilidad_especial):
        super().__init__(nombre, nivel)
        self.arco = arco
        self.habilidad_especial = habilidad_especial

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"arco: {self.arco}")
        print(f"habilidad especial: {self.habilidad_especial}")

    def usar_habilidad_especial(self):
        print(f"{self.nombre} utiliza su habilidad especial: {self.habilidad_especial}")
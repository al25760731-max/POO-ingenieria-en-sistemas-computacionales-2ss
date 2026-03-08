#taberna de los aventureros
class Taberna:
    def __init__(self, nombre, nivel):
        self.nombre = nombre
        self.nivel = nivel


    def mostrar_informacion(self):
        print(f"nombre: {self.nombre}")
        print(f"nivel: {self.nivel}")

    def presentacion(self):
        print(f"¡soy {self.nombre}! aventurero de nivel {self.nivel}")

    
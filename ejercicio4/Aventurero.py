#Aventurero de los aventureros
class Aventurero:
    def __init__(self, nombre, nivel):
        self.nombre = nombre
        self.nivel = nivel


    def presentacion(self):
        print(f"¡Hola soy {self.nombre} un {self.__class__.__name__} !de nivel {self.nivel}")

    def usar_habilidad(self):
        return "Habilidad desconocida." 
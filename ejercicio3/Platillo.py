#herencias 
class Platillo:
    def __init__ (self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def mostrar_informacion(self):
        print(f"nombre: {self.nombre}")
        print(f"precio: {self.precio}")

    def tipo(self):
        print("...")    
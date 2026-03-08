from Comida import Comida
from Bebida import Bebida
from Postre import Postre

pastel = Postre ("pastelde chocolate",50 , True)
hamburguesa = Comida ("hamburguesa", 80, "comida rapida")
jugo = Bebida ("jugo de naranja", 30, "fria")


print("--- Información de Pedido ---")
pastel.mostrar_informacion()
print("-" * 20)
hamburguesa.mostrar_informacion()
print("-" * 20)
jugo.mostrar_informacion()
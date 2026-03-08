from Mago import Mago
from Arquero import Arquero
from Guerrero import Guerrero 

Mago = Mago("Megumin's", 50, "ataque especial de la hechizera prodigio de los demonios carmesi", "Explosion")
Arquero = Arquero("sova", 45, "arco de radianita", "i,am the hunter")
Guerrero = Guerrero("Lion-O", 55, "Espada de Augurio", "thundercats thundercats oohhhh")

print("--- Información de aventurero ---")
Mago.mostrar_informacion()
print("-" * 20)
Arquero.mostrar_informacion()
print("-" * 20)
Guerrero.mostrar_informacion()

class Mascota:
    def __init__(self, nombre, edad, raza, nivelFelicidad=50):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        self.nivelFelicidad = nivelFelicidad 

    def jugar(self):
        self.nivelFelicidad = min(self.nivelFelicidad + 20, 100)

    def comer(self):
        self.nivelFelicidad = min(self.nivelFelicidad + 10, 100)

# Interacción con la mascota
mascota1 = Mascota("Willy", 3, "perro", 50)
print(f"Mi mascota se llama {mascota1.nombre}, tiene {mascota1.edad} años de edad y es un {mascota1.raza}")

mascota1.jugar()
print(f"Después de jugar, el nivel de felicidad de {mascota1.nombre} es de {mascota1.nivelFelicidad}")

mascota1.comer()
print(f"Después de comer, el nivel de felicidad de {mascota1.nombre} es de {mascota1.nivelFelicidad}")

if mascota1.nivelFelicidad > 70:
    print(f"{mascota1.nombre} está muy feliz!")
else:
    print(f"{mascota1.nombre} necesita más atención y cariño.")
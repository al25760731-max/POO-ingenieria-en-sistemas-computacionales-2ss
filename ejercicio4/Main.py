from Mago import Mago
from Arquero import Arquero
from Guerrero import Guerrero 

mago = Mago("megumin", 50, "explosion")
guerrero = Guerrero("lion", 35, "espada del augurio")
arquero = Arquero("sova", 20, 85)

mago.presentacion()
guerrero.presentacion()
arquero.presentacion()

mago.usar_habilidad_especial()
guerrero.usar_habilidad_especial()
arquero.usar_habilidad()
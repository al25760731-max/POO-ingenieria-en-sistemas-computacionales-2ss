from abc import ABC, abstractmethod
class Mob(ABC):
    pass

class Creeper(Mob):
   pass
   def hacer_sonido(self):
     return "..ssssss"

   def comportamiento(self):
     return "agresivo"

   def moverse(self):
      return "corre hacia el jugador"
    
    
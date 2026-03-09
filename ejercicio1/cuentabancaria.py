
#ta#tarea 1 cuenta bancaria..
class cuentabancaria:
 def  __init__(self,titular,numerodecuenta,saldo):
    self.titular = titular
    self.numerodecuenta = numerodecuenta
    self.saldo = saldo
  # depositar  de cuenta bancaria 
 def depositar(self, cantidad):
     if cantidad > 0:
         saldo_anterior = self.saldo
         self.saldo += cantidad
         print(f"deposito exitoso. saldo anterior: {saldo_anterior}, nuevo saldo: {self.saldo}")
 def retirar(self,cantidad):
      if cantidad <= self.saldo:
        self.saldo = self.saldo - cantidad
        saldo_anterior = self.saldo + cantidad
        print(f"retiro exitoso. saldo anterior: {saldo_anterior}, nuevo saldo: {self.saldo}")
        return cantidad
 def consultarsaldo(self):
         return self.saldo
         
 def mostrarinformacion(self):
      return f"{self.titular} tienes {self.saldo}"
cuenta1 = cuentabancaria("kevin","64642870235",1000)

cuenta1.depositar(600.0)
print (cuenta1.mostrarinformacion()) 
print(cuenta1.mostrarinformacion())
opcion = input("¿Quieres depositar o retirar dinero? (d/r): ")

if opcion.lower() == "d":
    cantidad = float(input("Ingresa la cantidad a depositar: "))
    cuenta1.depositar(cantidad)
elif opcion.lower() == "r":
    cantidad = float(input("Ingresa la cantidad a retirar: "))
    cuenta1.retirar(cantidad)
else:
    print("Opción no válida.")

print(cuenta1.mostrarinformacion())
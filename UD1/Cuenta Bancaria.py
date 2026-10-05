#Implementa una clase Cuenta con saldo inicial y métodos para ingresar, retirar y mostrar saldo. Añade control de fondos insuficientes.



class Cuenta:
    def __init__(self, saldoInicial):
        self.saldoInicial = saldoInicial

    def ingresar(self, cantidad):
        self.saldoInicial = self.saldoInicial + cantidad

    def retirar(self, cantidad):
        if (cantidad > self.saldoInicial):
            print("No hay suficiente saldo en la cuenta")
        else:
            self.saldoInicial = self.saldoInicial - cantidad

    def mostrar(self):
        return f"El saldo actual es: {self.saldoInicial}"

if __name__ == "__main__":
    saldoInicial = int(input("Introduce el saldo inicial: "))

    micuenta = Cuenta(saldoInicial)

    micuenta.ingresar(20)
    micuenta.retirar(30)
    print(micuenta.mostrar())
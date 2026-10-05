# Define una clase Empleado con atributos nombre, sueldo. Hereda Gerente que añade
# departamento y Programador que añade lenguaje. Implementa un método __str__ adecuado en
# cada clase.


class Empleado:
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo

    def __str__(self):
        return f"Empleado con nombre: {self.nombre} y sueldo {self.sueldo}€."

class Gerente(Empleado):
    def __init__(self, departamento, nombre, sueldo):
        super().__init__(nombre, sueldo)
        self.departamento = departamento

    def __str__(self):
        return super().__str__()+f" Gerente del departamento {self.departamento}"

class Programador(Empleado):
    def __init__(self, lenguaje, nombre, sueldo):
        super().__init__(nombre, sueldo)
        self.lenguaje = lenguaje

    def __str__(self):
        return super().__str__()+f" Trabaja con el lenguaje {self.lenguaje}"

if __name__ == "__main__":
    nombreG = input("Dime el nombre del gerente: ")
    sueldoG = int(input("Dime el sueldo del gerente: "))
    departamentoG = input("Dime el departamento del gerente: ")

    nombreP = input("Dime el nombre del programador: ")
    sueldoP = int(input("Dime el sueldo del programador: "))
    lenguajeP = input("Dime el lenguaje en el que trabaja el programador: ")

    ger = Gerente(departamentoG, nombreG, sueldoG)
    pro = Programador(lenguajeP, nombreP, sueldoP)

    print(ger)
    print(pro)

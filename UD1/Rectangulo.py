
class Rectangulo():
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.ancho * self.alto

    def perimetro(self):
        return self.ancho * 2 + self.alto * 2

if __name__ == "__main__":
    ancho = int(input("Introduce el ancho del rectangulo: "))
    alto = int(input("Introduce el alto del rectangulo: "))

    rect = Rectangulo(ancho, alto)

    print(f"El rectangulo con ancho {rect.ancho} y alto {rect.alto} tiene un área de {rect.area()} y un perímetro de {rect.perimetro()}.")
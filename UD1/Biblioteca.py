# Diseña una clase Libro y una clase Biblioteca que almacene varios libros en una lista.
# Implementa métodos para añadir, buscar y listar libros.

class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []

    def agregarLibro(self):
        nombre = input("Dime el nombre del libro: ")
        autor = input("Dime el nombre del autor del libro: ")
        año = int(input("Dime el año del libro: "))
        identificador = input ("Dime el identificador del libro")
        libro = Libro(nombre, autor, año, identificador)
        self.libros.append(libro)

    def buscarLibro(self):
        id = input("Dime el identificador del libro que buscas: ")
        for i in self.libros:
            if self.libros[i].identificador == id:
                print(self.libros[i])

    def listarLibros(self):
        for i in self.libros:
            print(self.libros[i])

class Libro:
    def __init__(self, nombre, autor, año, identificador):
        self.nombre = nombre
        self.autor = autor
        self.año = año
        self.identificador = identificador

    def __str__(self):
        return f"Titulo: {self.nombre}\nAutor: {self.autor}\nAño: {self.año}\nIdentificador: {self.identificador}"

if __name__ == "__main__":
    nombre = input("Dime el nombre de la biblioteca: ")
    biblio = Biblioteca(nombre)
    n = 1
    while(n != 0):
        print("1. Añadir Libro")
        print("2. Buscar Libro")
        print("3. Listado de los Libros")
        print("0. Salir")
        n = int(input("Elige una de las opciones escribiendo el número de la opción: "))
        match n:
            case 1:
                Biblioteca.agregarLibro()
            case 2:
                Biblioteca.buscarLibro()
            case 3:
                Biblioteca.listarLibros()
    
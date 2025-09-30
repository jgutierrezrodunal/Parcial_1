# Juan Alberto Gutiérrez Rodríguez
# Parcial 1
# Clase Libro

class Libro:
    def __init__(self):
        self.titulo = str()
        self.autor = str()
        self.categoria = str()
        self.isbn = int()
        self.copias = 0
        self._disponible = True

    def registrar_libro(self):
        self.titulo = input(print(f"Ingrese el título del libro: "))
        self.autor = input(print(f"Ingrese el autor del libro: "))
        self.categoria = input(print(f"Ingrese la categoría del libro: "))
        self.isbn = int(input(print(f"Ingrese el ISBN del libro: ")))
        self.copias = int(input(print(f"Ingrese el número de copias disponibles: ")))
    
    def prestar_libro(self):
        if self.copias > 0:
            self.copias -= 1
            print("El libro ha sido prestado")
        else:
            print("No hay copias disponibles para prestar")

    def devolver_libro(self):
        self.copias += 1
        print("El libro ha sido devuelto")


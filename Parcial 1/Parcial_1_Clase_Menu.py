# Juan Alberto Gutiérrez Rodríguez
# Parcial 1
# Clase Menú
from Parcial_1_Clase_Usuario import Usuario
from Parcial_1_Clase_Libro import Libro

l = Libro()


class Menu:
    def __init__(self):
        pass

    def mostrar_menu(self):
        print("--------------------------------------------------")
        print("Bienvenido al sistema de biblioteca universitaria")
        print("--------------------------------------------------")

        print("\n --------------------------------------------------")
        print("Seleccione una de las siguientes opciones: ")
        print("1. Registrar usuario")
        print("2. Registrar libro")
        print("3. Prestar libro")
        print("4. Devolver libro")
        print("5. Salir")
        print("--------------------------------------------------")

    def opcion_1(self):
        print("Ha seleccionado la opción 1")
        

    def opcion_2(self):
        print("Ha seleccionado la opción 2")
        
    def opcion_3(self):
        print("Ha seleccionado la opción 3")
        l.prestar_libro()

    def opcion_4(self):
        print("Ha seleccionado la opción 4")
        l.devolver_libro()

    def opcion_5(self):
        print("Ha seleccionado la opción 5")



        
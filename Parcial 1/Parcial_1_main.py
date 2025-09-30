# Juan Alberto Gutiérrez Rodríguez
# Parcial 1

from Parcial_1_Clase_Menu import Menu
from Parcial_1_Clase_Libro import Libro
from Parcial_1_Clase_Usuario import Usuario

opcion = 0
m = Menu()
l = Libro()

def main():

    m.mostrar_menu()

while opcion != 5:
    match opcion:
        case 1:     
            m.opcion_1()
        case 2:
            m.opcion_2()
        case 3:     
            m.opcion_3()
        case 4:
            m.opcion_4()
        case 5:
            m.opcion_5()

 



if __name__ == "__main__":
    main()
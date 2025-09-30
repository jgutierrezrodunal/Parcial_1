# Juan Alberto Gutiérrez Rodríguez
# Parcial 1
# Clase Usuario

class Usuario:
    def __init__(self, nombre, apellido, nidentificacion):
        self.nombre = nombre
        self.apellido = apellido
        self._ident = nidentificacion

        def Registrar_user(self):
            self.nombre = input(print(f"Ingrese su nombre: "))
            self.apellido = input(print(f"Ingrese su apellido: "))
            self._ident = input(print(f"Ingrese su número de identificación: "))
            

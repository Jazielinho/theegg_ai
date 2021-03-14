'''
Created on 14 mar. 2021
@author: jazielinho
'''


class Persona(object):
    ''' Clase Persona '''

    mayor_edad = 18
    dni_letters = "TRWAGMYFPDXBNJZSQVHLCKE"

    def __init__(self, nombre: str = "", edad: int = 0, dni: str = ""):
        ''' nombre: nombre de la persona
            edad: edad de la persona
            dni: dni de la persona
        '''
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = str(nombre)

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, edad):
        try:
            edad = int(edad)
            if edad < 0:
                raise ValueError(f"Edad: {edad} es menor a cero")
            self.__edad = edad
        except Exception as e:
            raise ValueError(f"Error al guardar la edad: {edad}: {e}")

    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, dni):
        try:
            if len(dni) != 9:
                raise ValueError(f"DNI: {dni} incorrecto")
            letra = dni[8]
            num = int(dni[:8])
            if letra.upper() != self.dni_letters[num % 23]:
                raise ValueError(f"DNI: {dni} incorrecto")
            self.__dni = dni
        except Exception as e:
            raise ValueError(f"Error al guardar el dni {dni}: {e}")

    def mostrar(self):
        print(f"Nombre: {self.__nombre}, edad: {self.__edad}, DNI: {self.__dni}")

    def es_mayor_edad(self):
        if self.__edad >= self.mayor_edad:
            print("Es mayor de edad")
        else:
            print("No es mayor de edad")


class Cuenta(object):
    ''' Clase Cuenta '''

    def __init__(self, titular: str = "", cantidad: float = 0):
        self.titular = titular
        self.cantidad = cantidad

    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self, titular):
        self.__titular = str(titular)

    @property
    def cantidad(self):
        return self.__cantidad

    @cantidad.setter
    def cantidad(self, cantidad):
        try:
            cantidad = float(cantidad)
            self.__cantidad = cantidad
        except Exception as e:
            raise ValueError(f"Error al guardar la cantidad: {cantidad}: {e}")

    def mostrar(self):
        print(f"Titular: {self.titular}, cantidad: {self.cantidad}")

    def ingresar(self, cantidad):
        try:
            self.cantidad = self.cantidad + cantidad
        except Exception as e:
            print(f"No se ha podido ingresar cantidad {cantidad}: {e}")

    def retirar(self, cantidad):
        self.cantidad = self.cantidad - cantidad


if __name__ == '__main__':
    print("\n\n\n")
    print("Clase Persona")
    persona = Persona('a', 18, '33277898A')
    persona.mostrar()
    persona.es_mayor_edad()

    print("\n\n\n")

    print("Clase Cuenta")
    cuenta = Cuenta('Juan', 10)
    cuenta.ingresar(20)
    cuenta.mostrar()
    cuenta.retirar(50)
    cuenta.mostrar()

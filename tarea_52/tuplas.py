'''
Created on 13 mar. 2020
@author: jazielinho
'''


class PasajerosCiudades(object):

    def __init__(self):
        self.lista_pasajeros = []
        self.lista_ciudades = []

    def agregar_pasajeros(self) -> None:
        nombre = input("Ingrese nombre (x para salir):\t")
        while nombre.lower() != 'x':
            dni = int(input("Ingrese DNI: \t"))
            destino = input("Ingrese ciudad destino: \t")
            self.lista_pasajeros.append((nombre, dni, destino))
            nombre = input("Ingrese nombre (x para salir):\t")
        print("Listo, pasajeros ingresados")

    def agregar_ciudades(self) -> None:
        ciudad = input("Ingrese ciudad (x para salir):\t")
        while ciudad.lower() != "x":
            pais = input("Ingrese país:\t")
            self.lista_ciudades.append((ciudad, pais))
            ciudad = input("Ingrese ciudad (x para salir):\t")

    def valida_input(self):
        ''' verifica si hay datos ingresados '''
        if len(self.lista_pasajeros) > 0 and len(self.lista_ciudades) > 0:
            return True
        print("Ingrese datos de pasajeros o ciudades")
        return False

    def buscar_ciudad_por_dni(self) -> None:
        if self.valida_input():
            dni = int(input("Ingrese DNI para buscar ciudad:\t"))
            k = 0
            for viaje_info in self.lista_pasajeros:
                if viaje_info[1] == dni:
                    k += 1
                    print(f"El pasajero viaja a: {viaje_info[2]}")
                    break
            if k == 0:
                print(f"DNI: {dni} no encontrado")

    def cantidad_viajan_ciudad(self) -> None:
        if self.valida_input():
            ciudad = input("Ingrese ciudad para contar pasajeros:\t")
            numero_pasajeros = 0
            for viaje_info in self.lista_pasajeros:
                if viaje_info[2] == ciudad:
                    numero_pasajeros += 1
            if numero_pasajeros > 0:
                print(f"Cantidad de pasajeros que viajan a la ciudad {ciudad}: {numero_pasajeros}")
            else:
                print(f"Ningún pasajero viaja a la ciudad {ciudad}")

    def buscar_pais_por_dni(self) -> None:
        if self.valida_input():
            dni = int(input("Ingrese DNI para buscar pais:\t"))
            k = 0
            for viaje_info in self.lista_pasajeros:
                if viaje_info[1] == dni:
                    ciudad = viaje_info[2]
                    for ciudad_info in self.lista_ciudades:
                        if ciudad == ciudad_info[0]:
                            k += 1
                            print(f"El pasajero viaja a: {ciudad_info[1]}")
                            break
            if k == 0:
                print(f"DNI: {dni} no encontrado")

    def cantidad_viajan_pais(self) -> None:
        if self.valida_input():
            pais = input("Ingrese país para contar pasajeros:\t")
            numero_pasajeros = 0
            for ciudad_info in self.lista_ciudades:
                if pais == ciudad_info[1]:
                    ciudad = ciudad_info[0]
                    for viaje_info in self.lista_pasajeros:
                        if viaje_info[2] == ciudad:
                            numero_pasajeros += 1
            if numero_pasajeros > 0:
                print(f"Cantidad de pasajeros que viajan al país {pais}: {numero_pasajeros}")
            else:
                print(f"Ningún pasajero viaja al país {pais}")


def main():
    pasajeros_ciudades = PasajerosCiudades()
    dict_informacion = {
        1: pasajeros_ciudades.agregar_pasajeros,
        2: pasajeros_ciudades.agregar_ciudades,
        3: pasajeros_ciudades.buscar_ciudad_por_dni,
        4: pasajeros_ciudades.cantidad_viajan_ciudad,
        5: pasajeros_ciudades.buscar_pais_por_dni,
        6: pasajeros_ciudades.cantidad_viajan_pais
    }
    while True:
        print("""
        1. Agregar pasajeros
        2. Agregar ciudades
        3. Buscar ciudad de destino mediante el DNI
        4. Cantidad de usuarios que viajan a una ciudad
        5. Buscar país de destino mediante el DNI
        6. Cantidad de pasajeros que viajan a un país
        7. Salir del programa
        """)
        try:
            opcion = int(input("Ingrese opción:\t"))
        except:
            print("Opción inválida")
            continue

        if opcion == 7:
            break

        dict_informacion[opcion]()


if __name__ == '__main__':
    main()





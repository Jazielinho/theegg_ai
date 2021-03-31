'''
Created on 13 mar. 2020
@author: jazielinho
'''

from typing import List


class String:
    def __init__(self, lista_string: List):
        self.lista_string = lista_string
        self.diccionario_cantidad = {}

        self.de_lista_a_diccionario()

    def de_lista_a_diccionario(self) -> None:
        ''' convierte la lista de string a un diccionario con la cantidad de cada string '''
        for string in self.lista_string:
            if string not in self.diccionario_cantidad:
                self.diccionario_cantidad[string] = 0
            self.diccionario_cantidad[string] += 1

    def __str__(self) -> str:
        ''' Muestra la cantidad de ocurrencias de cada string '''
        text = 'Conteo de elementos:'
        for clave, valor in self.diccionario_cantidad.items():
            text += f'\n{clave}: {valor}'
        return text


def main():
    cantidad_string = 0
    lista_string = []

    while cantidad_string < 50:
        cantidad_string += 1
        string = input(f"Ingrese string {cantidad_string}:\t")
        lista_string.append(string)

    string_ = String(lista_string=lista_string)
    print(string_)

    print('\n')
    input("Presione cualquier tecla para salir de la aplicación")


if __name__ == '__main__':
    main()



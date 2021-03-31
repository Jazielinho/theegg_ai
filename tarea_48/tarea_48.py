
import sys
import re
from typing import List, Any


class LZ77(object):

    @staticmethod
    def valida_string(string: str) -> bool:
        if len(string) > 30 or len(string) <= 0:
            return False
        return True

    @staticmethod
    def retorna_peso(objeto: Any):
        ''' Muestra el tamaño del string '''
        return sys.getsizeof(objeto)

    @staticmethod
    def evalua_resultados(str_original, str_nuevo):
        ''' Compara si los dos string son iguales '''
        return str_original == str_nuevo

    @staticmethod
    def comprimir(string: str) -> List:
        ''' utiliza el algorito LZ77 para comprimir un texto '''
        lista_ubicaciones = []
        longitud = len(string)

        # Empiezo desde el primer elemento
        string_izquierda = ''
        indice_inicio = len(string_izquierda)

        continuar = True
        while continuar:

            all_string_derecha = string[indice_inicio:]
            string_derecha = ''
            indice_encontrado = 0
            continuar_buscando = True

            k = 0
            while continuar_buscando:
                indice_final = indice_inicio + k + 1
                string_derecha = string[indice_inicio: indice_final]

                lista_indices_encontrados = [m.start() for m in re.finditer(string_derecha, string_izquierda)]

                if len(lista_indices_encontrados) > 0:
                    indice_encontrado = max(lista_indices_encontrados)
                    k += 1
                    if string_derecha == all_string_derecha:
                        continuar_buscando = False
                else:
                    continuar_buscando = False

            len_string_derecha = len(string_derecha)

            string_izquierda = string_izquierda + string_derecha

            lista_ubicaciones.append(
                [
                    0 if len_string_derecha == 1 else indice_inicio - indice_encontrado,
                    len_string_derecha - 1,
                    string_derecha[-1]
                ]
            )

            indice_inicio = len(string_izquierda)

            if longitud == len(string_izquierda):
                continuar = False

        return lista_ubicaciones

    @staticmethod
    def descomprimir(lista_comprimida: List) -> str:
        ''' utiliza el algoritmo LZ77 para descomprimir'''
        string = ''
        for m, n, s in lista_comprimida:
            if m > 0:
                inicio_ = max([0, len(string) - m])
                fin_ = inicio_ + n
                string_ = string[inicio_: fin_]
            else:
                string_ = ''
            string = string + string_ + s
        return string


def main():
    solicitar_string = True

    while solicitar_string:
        string = input("Ingrese string:\t")
        if LZ77.valida_string(string=string):
            solicitar_string = False

        else:
            print("Ingrese otro string")

    print("String original")
    print(string)
    print("Peso del string:")
    print(LZ77.retorna_peso(objeto=string))

    lista_comprimida = LZ77.comprimir(string=string)

    print("Lista comprimida")
    print(lista_comprimida)
    print("Peso del string:")
    print(LZ77.retorna_peso(objeto=lista_comprimida))

    string_descomprimido = LZ77.descomprimir(lista_comprimida=lista_comprimida)

    print("String descomprimido")
    print(string_descomprimido)

    iguales_ = LZ77.evalua_resultados(str_original=string, str_nuevo=string_descomprimido)
    print(f"Los string son {'iguales' if iguales_ else 'distintos'}")





if __name__ == '__main__':
    # string = 'abracadabrarrayabracadabrarrayabracadabrarrayabracadabrarray'
    # lista_comprimida = LZ77.comprimir(string)
    # LZ77.descomprimir(lista_comprimida)
    main()
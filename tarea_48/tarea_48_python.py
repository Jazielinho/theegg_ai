'''
Created on 9 ago. 2020
@author: jazielinho
'''

from typing import Any, List
import tempfile
import pickle
import os
import re
import sys


class LZ77(object):
    MAX_LONGITUD = 30

    @staticmethod
    def valida_string(string: str) -> bool:
        ''' valida si el tamaño del string está entre 0 y MAX_LONGITUD '''
        return 0 <= len(string) <= LZ77.MAX_LONGITUD
    
    @staticmethod
    def _devuelve_peso(objeto: Any) -> int:
        ''' devuelve el peso de un objeto en disco '''
        with tempfile.NamedTemporaryFile() as tmp_file:
            pickle.dump(objeto, tmp_file)
            tmp_file.flush()
        return os.path.getsize(tmp_file.name)

    @staticmethod
    def devuelve_peso(string: str) -> int:
        ''' devuelve el peso de un objeto en disco '''
        return sys.getsizeof(string)
    
    @staticmethod
    def evalua_string(string_1: str, string_2: str) -> bool:
        ''' compara los dos string '''
        return string_1 == string_2
    
    @staticmethod
    def comprimir(string: str) -> List:
        ''' comprime el string usando el algoritmo LZ77 '''
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
            
            m = 0 if len_string_derecha == 1 else indice_inicio - indice_encontrado
            n = len_string_derecha - 1
            s = string_derecha[-1]

            lista_ubicaciones.append((m, n, s))
            
            indice_inicio = len(string_izquierda)

            if longitud == len(string_izquierda):
                continuar = False

        return lista_ubicaciones

    @staticmethod
    def descomprimir(lista_comprimida: str) -> str:
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
        string = input("Ingrese texto:\t")
        if LZ77.valida_string(string):
            solicitar_string = False
        else:
            print("El texto debe ser de 0 a {} caracteres".format(LZ77.MAX_LONGITUD))
            print("Ingrese otro texto")
    
    print()
    print(f"Texto ingresado: {string}")
    print(f"Peso del texto: {LZ77.devuelve_peso(string)}")
    
    texto_comprimido = LZ77.comprimir(string)
    print()
    print("Texto comprimido: {}".format(texto_comprimido))
    print(f"Peso del texto comprimido: {LZ77.devuelve_peso(texto_comprimido)}")
    
    texto_reconstruido = LZ77.descomprimir(texto_comprimido)
    print()
    print("Texto reconstruido: {}".format(texto_reconstruido))
    print(f"Peso del texto reconstruido: {LZ77.devuelve_peso(texto_reconstruido)}")
    
    print()
    if LZ77.evalua_string(string, texto_reconstruido):
        print("Los textos coinciden")
    else:
        print("Los textos no coinciden")

    input("Presione cualquier tecla para cerrar la aplicacion")


if __name__ == '__main__':
    main()


        
        





    
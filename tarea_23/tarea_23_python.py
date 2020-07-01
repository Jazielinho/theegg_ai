'''
Created on 18 jun. 2020
@author: jazielinho
'''

import string
import random


class Solitario(object):
    texto_error = "Los textos tienen distinta longitud, ingrese en la misma por favor"

    # El numero 27 lo asocio al espacio en blanco
    dict_letra_entero = {x: (enum + 1) for enum, x in enumerate(string.ascii_uppercase)}
    dict_letra_entero[' '] = 27
    dict_letra_entero['¿'] = 27

    # En lugar de devolver espacio en blanco, devuelvo un ¿ (para evitar espacios en blanco en los extremos)
    dict_entero_letra = {v: k for k, v in dict_letra_entero.items()}
    dict_entero_letra[27] = '¿'

    lista_letras_validas_clave = list(dict_letra_entero.keys())
    lista_letras_validas = list(set(lista_letras_validas_clave) - {'¿'})
    lista_enteros_validos = list(dict_entero_letra.keys())

    @staticmethod
    def verifica_texto(texto, desencriptar=False):
        '''
            Muestra texto que no se puede cifrar. Verifica si el texto es valido
                (el texto debe estar en la lista de letras validas)
            :param texto: texto a validar
            :param desencriptar: verifica incluyendo "¿" (caso desencriptar)
            :return: texto que no esta en la lista de letras validas
        '''
        if desencriptar:
            return set(texto) - set(Solitario.lista_letras_validas_clave)
        return set(texto) - set(Solitario.lista_letras_validas)

    @staticmethod
    def convertir_texto_listanumeros(texto):
        '''
            Convierte texto en numero
            aA -> 1, bB-> 2, ..., zZ -> 26 ' ' -> 27
            :param texto: texto sin espacios en blanco
            :return: lista de numeros
        '''
        return [Solitario.dict_letra_entero[x] for x in texto]

    @staticmethod
    def convertir_listanumeros_texto(lista_numeros, devolver_espacio_blanco=True):
        '''
            Convierte numero a texto
            :param lista_numeros: lista de numeros cada elemento es del 1 al 27
            :return: texto
        '''
        lista_texto = []
        for numero in lista_numeros:
            if numero == 27 and devolver_espacio_blanco:
                lista_texto.append(' ')
            else:
                lista_texto.append(Solitario.dict_entero_letra[numero])
        return lista_texto

    @staticmethod
    def genera_clave_listanumerica(tamanho):
        '''
            Genera una lista de numeros aleatorios entre 1 y 27 (27 indica espacio en blanco)
            :param tamanho: tamanho del texto (sin espacios en blanco)
            :return: Lista de numeros aleatorios entre 1 - 27
        '''
        return random.choices(Solitario.lista_enteros_validos, k=tamanho)

    @staticmethod
    def cifrar_numero(numeros_texto_original, numeros_texto_clave):
        '''
            Genera nuevos numeros como la suma de los numeros del texto original y del texto clave
                la suma pasa por el modulo de 27
            :param numeros_texto_original: lista de numeros del texto original
            :param numeros_texto_clave: lista de numeros del texto clave
            :return: lista de numeros cifrados
        '''
        if len(numeros_texto_original) != len(numeros_texto_clave):
            print(Solitario.texto_error)
            return None

        lista_numeros_cifrados = []
        for x in range(len(numeros_texto_original)):
            valor = numeros_texto_original[x] + numeros_texto_clave[x]
            valor = valor if valor <= 27 else valor - 27
            lista_numeros_cifrados.append(valor)
        return lista_numeros_cifrados

    @staticmethod
    def descifrar_numero(numeros_texto_encriptado, numeros_clave):
        '''
            Genera los numeros originales a partir del los numeros encriptados y los numeros clave
            :param numeros_texto_encriptado: lista de numeros encriptador
            :param numeros_clave: lista de numeros clave
            :return: lista de numeros original
        '''
        if len(numeros_texto_encriptado) != len(numeros_clave):
            print(Solitario.texto_error)
            return None

        lista_numeros_original = []
        for x in range(len(numeros_texto_encriptado)):
            valor = numeros_texto_encriptado[x] - numeros_clave[x]
            valor = valor if valor > 0 else valor + 27
            lista_numeros_original.append(valor)
        return lista_numeros_original

    @staticmethod
    def encriptar(texto):
        '''
            Cifra el texto devolviendo un nuevo texto y la clave
        :param texto: texto a cifrar
        :return: nuevo texto y clave
        '''
        texto = str(texto)
        if len(texto) != len(texto.strip()):
            print('Se eliminan espacios en blanco en los extremos')
        texto = str(texto).strip().upper()
        letras_no_validas = Solitario.verifica_texto(texto=texto, desencriptar=False)

        if len(letras_no_validas) == 0:
            tamanho_texto = len(texto)

            numeros_texto = Solitario.convertir_texto_listanumeros(texto=texto)
            clave_numero = Solitario.genera_clave_listanumerica(tamanho=tamanho_texto)
            clave_texto = Solitario.convertir_listanumeros_texto(lista_numeros=clave_numero,
                                                                 devolver_espacio_blanco=False)

            nuevos_numeros = Solitario.cifrar_numero(numeros_texto_original=numeros_texto, numeros_texto_clave=clave_numero)
            if nuevos_numeros is None:
                return None
            nuevo_texto = Solitario.convertir_listanumeros_texto(lista_numeros=nuevos_numeros,
                                                                 devolver_espacio_blanco=False)

            return {'nuevo_texto': ''.join(nuevo_texto),
                    'clave': ''.join(clave_texto)}
        print(f"Las siguientes letras no se pueden cifrar: {' '.join(letras_no_validas)}")
        return None

    @staticmethod
    def desencriptar(texto_encriptado, clave):
        '''
            Convierte el texto encriptado en el texto original usando la clave
            :param texto_encriptado: texto encriptado
            :param clave: clave para desencriptar
            :return: texto desencriptado
        '''
        texto_encriptado = str(texto_encriptado).upper()
        letras_no_validas = Solitario.verifica_texto(texto=texto_encriptado, desencriptar=True)

        clave = str(clave).upper()
        letras_clave_no_validas = Solitario.verifica_texto(texto=clave, desencriptar=True)

        if len(letras_no_validas) + len(letras_clave_no_validas) == 0:
            numeros_texto_encriptado = Solitario.convertir_texto_listanumeros(texto=texto_encriptado)
            numeros_clave = Solitario.convertir_texto_listanumeros(texto=clave)

            numeros_texto_original = Solitario.descifrar_numero(numeros_texto_encriptado=numeros_texto_encriptado,
                                                                numeros_clave=numeros_clave)
            if numeros_texto_original is None:
                return None
            texto_original = Solitario.convertir_listanumeros_texto(lista_numeros=numeros_texto_original,
                                                                    devolver_espacio_blanco=True)
            return ''.join(texto_original)
        print(f"Las siguientes palabras no se pueden cifrar: {' '.join(letras_no_validas.union(letras_clave_no_validas))}")
        return None


def main():
    encriptar_b = input("Desea encriptar o descencriptar el texto (E: encriptar, D: desencriptar):\t")
    if encriptar_b.lower() not in ('e', 'd'):
        print(f"Por favor, escriba E o D")
    else:
        if encriptar_b.lower() == 'e':
            texto = input("Ingrese texto para encriptarlo:\t")
            dict_encriptado = Solitario.encriptar(texto=texto)
            if dict_encriptado is not None:
                nuevo_texto = dict_encriptado['nuevo_texto']
                clave = dict_encriptado['clave']
                print(f"Texto encriptado: {nuevo_texto}")
                print(f"Clave: {clave}")
        else:
            texto_encriptado = input("Ingrese texto para desencriptarlo:\t")
            clave = input("Ingrese clave:\t")
            texto_original = Solitario.desencriptar(texto_encriptado=texto_encriptado, clave=clave)
            print(f"Texto original: {texto_original}")


if __name__ == '__main__':
    main()















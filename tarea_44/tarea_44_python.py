'''
Created on 3 oct. 2020
@author: jazielinho
'''

import time


def valida_numero(numero):
    '''
        Valida si un número es entero
        :param numero: Numero
        :return: numero en entero o None si falla
    '''
    try:
        numero = float(numero)
        if numero.is_integer():
            if numero > 0:
                return int(numero)
        return None
    except Exception as e:
        print('Error in es_entero, numero {}, e: {}'.format(numero, e))
        return None


def suma_lineal(n):
    '''
        Calcula la suma de los n primeros numeros
        :param n: numero
        :return: suma
    '''
    suma = 0
    for i in range(1, n + 1):
        suma += i
    return suma


def suma_constante(n):
    '''
         Calcula la suma de los n primeros numeros de manera rapida
         :param n: numero
         :return: suma
     '''
    return int(n * (n + 1) / 2)


def compara_algoritmos(cantidad):
    '''
    Compara ambos algoritmos para un n dado
    :param n: numero
    :return: print con tiempos
    '''
    n = valida_numero(cantidad)
    if n is None:
        print('El número proporcionado no es válido')
        return None

    for _ in range(4):
        # Suma lineal
        t0 = time.time()
        suma1 = suma_lineal(n=n)

        # Suma constante
        t1 = time.time()
        suma2 = suma_constante(n=n)

        t2 = time.time()

        print('Suma lineal: n={}, suma={}, tiempo={}'.format(n, suma1, t1 - t0))
        print('Suma constante: n={}, suma={}, tiempo={}'.format(n, suma2, t2 - t1))

        n *= 10


def main():
    cantidad = input("Ingrese cantidad inicial:\t")
    compara_algoritmos(cantidad)
    input("Presione ENTER para cerrar la aplicación")


if __name__ == '__main__':
    main()




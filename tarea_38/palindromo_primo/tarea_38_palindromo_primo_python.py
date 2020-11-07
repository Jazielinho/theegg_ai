'''
Created on 25 jun. 2020
@author: jazielinho
'''


def es_primo(numero):
    '''
    Verificamos si un numero es primo
    :param numero: numero
    :return: True o False si el número es primo o no
    '''
    if numero < 2:
        # numero 1 o menor no son primos
        return False
    divisor = 2

    while divisor < numero:
        if numero % divisor == 0:
            # Si el resto de la división es cero, el número no es primo
            return False
        cociente = numero // divisor
        if divisor > cociente:
            # No es necesario verificar con todos los números posibles
            # https://bit.ly/3hCPPxG
            return True
        divisor += 1

    return True


def es_palindromo(numero):
    '''
    Verifica si un número palíndromo
    :param numero: número
    :return: True o False si el número es palíndromo
    '''
    numero_str = str(numero)
    # invertimos las cifras del número
    numero_invertido_str = numero_str[::-1]
    if numero_str == numero_invertido_str:
        # Verificamos que el número sea igual a si invertimos sus crifras
        return True
    return False


def devuelve_palindromo_primo_cercano(numero):
    '''
    Devuelve el mayor número más cercano que sea primo y palíndromo
    :param numero: número
    :return: número mayor más cercano palíndromo y primo
    '''
    encontrado = False
    numero_mayor = numero - 1
    while encontrado is False:
        # Empezamos con el primer número
        numero_mayor += 1
        if es_palindromo(numero=numero_mayor):
            # Verificamos primero si es palíndromo (es más rápido que verificar si es primo)
            if es_primo(numero=numero_mayor):
                # Verificamos si el número es primo
                encontrado = True
    return numero_mayor


def main():
    numero = input("Ingrese numero:\t")
    numero = int(numero)
    numero_palindromo_primo_mayor = devuelve_palindromo_primo_cercano(numero=numero)
    print(numero_palindromo_primo_mayor)
    input("presione ENTER para cerrar la aplicacion")


if __name__ == '__main__':
    main()
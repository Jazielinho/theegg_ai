'''
Created on 25 jun. 2020
@author: jazielinho
'''

import string


def verifica_secuencia(secuencia):
    '''
    Verifica si una secuencia es correcta
    :param secuencia: secuencia a verificar
    :return: True o False si la secuencia pasa la validación
    '''
    try:
        if len(secuencia) == 0:
            # Al menos texto
            print(f"{secuencia} necesita texto")
            return False
        for palabra in secuencia:
            if palabra.isspace():
                # no espacios en blanco
                print(f"{secuencia} tiene espacios en blanco")
                return False
            if palabra.isdigit():
                # no digitos
                print(f"{secuencia} hay digitos")
                return False
            if palabra in string.punctuation:
                # no signos de puntuación
                print(f"{secuencia} tiene signos de puntuación")
                return False
        return True
    except Exception as e:
        print(f"Error en verifica_secuencia {e}")
        return False


def devuelve_secuencias(secuencia_1, secuencia_2):
    '''
    Devuelve la longitud máxima, la secuencia mayor y secuencia menor
    :param secuencia_1: secuencia mínima
    :param secuencia_2: secuencia máxima
    :return: longitud, secuencia_minima, secuencia_maxima
    '''
    len_1 = len(secuencia_1)
    len_2 = len(secuencia_2)
    if len_1 > len_2:
        return len_2, secuencia_2, secuencia_1
    return len_1, secuencia_1, secuencia_2


def verifica_secuencia_texto(secuencia_comun, secuencia_comparar):
    '''
    verifica si la secuencia común se encuentr adentro de la secuencia_comparar
    :param secuencia_comun: secuencia base a buscar similitud
    :param secuencia_comparar: secuencia donde se va a buscar
    :return:
    '''

    # se puede escribir (secuencia_comun in secuencia_comparar) y va más rápido, pero quiero hacerlo desde cero

    for inicio in range(len(secuencia_comparar) - len(secuencia_comun) + 1):
        secuencia_compara_ = secuencia_comparar[inicio: (inicio + len(secuencia_comun))]
        if secuencia_comun == secuencia_compara_:
            return True
    return False


def devolver_secuencia_comun(secuencia_1, secuencia_2):
    '''
    Tarea 38: devuelve secuencia máxima comun entre dos secuencias
    :param secuencia_1: primera secuencia
    :param secuencia_2: segunda secuencia
    :return: secuencia común de mayor longitud
    '''
    try:
        if (verifica_secuencia(secuencia=secuencia_1) is False) or (verifica_secuencia(secuencia=secuencia_2) is False):
            return None

        longitud_analisis, secuencia_minima, secuencia_maxima = devuelve_secuencias(secuencia_1=secuencia_1,
                                                                                    secuencia_2=secuencia_2)

        for longitud in reversed(range(longitud_analisis)):
            for inicio in range(longitud_analisis - longitud):
                secuencia_comun = secuencia_minima[inicio: (inicio + longitud + 1)]
                if verifica_secuencia_texto(secuencia_comun=secuencia_comun, secuencia_comparar=secuencia_maxima):
                    return secuencia_comun

        return ''
    except Exception as e:
        print(f"Error en devolver_secuencia_común {e}")
        return False
    

def main():
    secuencia_1 = input("Ingrese primera secuencia:\t")
    secuencia_2 = input("Ingrese segunda secuencia:\t")
    secuencia_comun = devolver_secuencia_comun(secuencia_1=secuencia_1, secuencia_2=secuencia_2)
    if secuencia_comun is not None:
        if len(secuencia_comun) > 0:
            print(f'Secuencia común: "{secuencia_comun}"')
        else:
            print(f"no hay secuencia común")
    input("Presione ENTER para cerrar la aplicación")


if __name__ == '__main__':
    main()
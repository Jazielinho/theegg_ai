
import string


def es_secuencia_valida(secuencia):
    '''
    Verifica si una secuencia es valida
    :param secuencia: secuencia a verificar
    :return: True o False si la secuencia pasa la validación
    '''
    try:
        len_secuencia = len(secuencia)
        puntuaciones = string.punctuation
        if len_secuencia > 0:
            contador = 0
            valido = True
            while valido:
                if contador >= len_secuencia:
                    break
                else:
                    palabra = secuencia[contador]
                    if palabra.isspace():
                        print('{} tiene espacio en blanco'.format(secuencia))
                        valido = False
                    else:
                        if palabra.isdigit():
                            print('{} tiene numeros'.format(secuencia))
                            valido = False
                        else:
                            if palabra in puntuaciones:
                                print('{} tiene puntuaciones'.format(secuencia))
                                valido = False
                            else:
                                contador += 1
            return valido
        else:
            print('{} es vacio'.format(secuencia))
            return False
    except Exception as e:
        print('Error en es_secuencia_valida, secuencia {}: {}'.format(secuencia, e))
        return False


def devuelve_secuencias(secuencia_1, secuencia_2):
    '''
    Devuelve la longitud menor, mayor, la secuencia menor y secuencia mayor
    :return: True si el proceso sale bien, caso contrario devuelve False
    '''
    len_sec_1 = len(secuencia_1)
    len_sec_2 = len(secuencia_2)
    if len_sec_1 > len_sec_2:
        longitud_menor = len_sec_2
        longitud_mayor = len_sec_1
        secuencia_menor = secuencia_2
        secuencia_mayor = secuencia_1
    else:
        longitud_menor = len_sec_1
        longitud_mayor = len_sec_2
        secuencia_menor = secuencia_1
        secuencia_mayor = secuencia_2
    return longitud_menor, longitud_mayor, secuencia_menor, secuencia_mayor


def devolver_secuencia_comun(secuencia_1, secuencia_2):
    '''
    Tarea 38: devuelve secuencia máxima comun entre dos secuencias
    :return: secuencia común de mayor longitud
    '''
    try:
        secuencia_comun = None

        valido_secuencia_1 = es_secuencia_valida(secuencia=secuencia_1)
        valido_secuencia_2 = es_secuencia_valida(secuencia=secuencia_2)

        if valido_secuencia_1 is False or valido_secuencia_2 is False:
            return secuencia_comun

        longitud_menor, longitud_mayor, secuencia_menor, secuencia_mayor = devuelve_secuencias(secuencia_1=secuencia_1,
                                                                                               secuencia_2=secuencia_2)

        contador_final = longitud_menor
        contador_inicio = 0

        existe_comun = False

        while existe_comun is False:

            if contador_inicio >= contador_final:
                contador_final -= 1
                contador_inicio = 0
                if contador_final <= 0:
                    break
            else:
                secuencia_comun = secuencia_menor[contador_inicio: contador_final]

                if secuencia_comun in secuencia_mayor:
                    existe_comun = True
                else:
                    contador_inicio += 1

        if existe_comun is False:
            return ''
        else:
            return secuencia_comun

    except Exception as e:
        print('Error en devolver_secuencia_comun: {}'.format(e))
        return None


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
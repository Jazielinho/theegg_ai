'''
Created on 14 jun. 2020
@author: jazielinho
'''


def get_mcd(a, b):
    # https://www.rdocumentation.org/packages/FRACTION/versions/1.0/topics/gcd
    if b == 0:
        return a
    else:
        return get_mcd(b, a % b)


def get_fraccion_irreducible(float_numero):
    '''
    Funcion que dado un numero muestra la fraccion irreducible
    :param float_numero: numero float, preferiblemente decimal
    :param return_string: Indicar si el resultado se quiere en formato fraccion (/) o separado por comas (,)
    :return:
    '''
    try:
        float_numero = float(float_numero)

        if 0.0001 <= float_numero <= 0.9999:

            split_number = str(float_numero).split('.')
            no_decimal = split_number[0]
            decimal = split_number[1]

            num_decimal = len(decimal)
            denominador = 10 ** num_decimal
            numerador = (10 ** num_decimal) * int(no_decimal) + int(decimal)

            mcd = get_mcd(a=numerador, b=denominador)

            denominador = denominador / mcd
            numerador = numerador / mcd

            print(f"{int(numerador)} / {int(denominador)}")
        else:
            print(f"Numero {float_numero} no permitido, escriba entre 0.0001 y 0.9999")

    except Exception as e:
        print(f"Error obteniendo la fraccion irreducible de {float_numero}, {e}")


def main():
    float_numero = input("Ingrese numero decimal:\t")
    get_fraccion_irreducible(float_numero=float_numero)
    input("presione ENTER para cerrar la aplicacion")


if __name__ == '__main__':
    main()


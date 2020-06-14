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


def get_fraccion_irreducible(float_numero, return_string=True):
    '''
    Funcion que dado un numero muestra la fraccion irreducible
    :param float_numero: numero float, preferiblemente decimal
    :param return_string: Indicar si el resultado se quiere en formato fraccion (/) o separado por comas (,)
    :return:
    '''
    try:
        float_numero = float(float_numero)

        num_decimal = len(str(float_numero).split('.')[1])
        denominador = 10 ** num_decimal
        numerador = float_numero * denominador

        mcd = get_mcd(a=numerador, b=denominador)

        denominador = denominador / mcd
        numerador = numerador / mcd

        if return_string:
            print(f"{int(numerador)} / {int(denominador)}")
        else:
            print(f"{int(numerador)},  {int(denominador)}")
    except Exception as e:
        print(f"Error obteniendo la fraccion irreducible de {float_numero}, {e}")


def main():
    float_numero = input("Ingrese numero decimal:\t")
    string_info = input("Desea que la salia sea string? Si o No?: ")
    get_fraccion_irreducible(float_numero=float_numero, return_string=string_info.lower() == 'si')


if __name__ == '__main__':
    main()


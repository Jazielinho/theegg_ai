

def decimal_2_binario(decimal):
    '''
    Convierte a binario un numero decimal
    :param decimal: numero decimal
    :return: numero binario
    '''
    try:
        decimal = float(decimal)
        if decimal % 1 != 0:
            print(f"Decimal {decimal} no es entero, se va a considerar la parte entera {int(decimal)}")
            decimal = int(decimal)
        binario = ''
        if decimal == 0:
            return '0'
        while decimal > 0:
            digito = str(decimal % 2).split('.')[0]
            decimal = decimal // 2
            binario = str(digito) + binario
        return binario
    except Exception as e:
        print(f"Error en decimal_2_binario, decimal: {decimal}, {e}")


def main():
    decimal = input("Ingrese numero:\t")
    print(decimal_2_binario(decimal=decimal))
    input("presione ENTER para cerrar la aplicacion")


if __name__ == '__main__':
    main()

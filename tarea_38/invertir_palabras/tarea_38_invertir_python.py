'''
Created on 25 jun. 2020
@author: jazielinho
'''


def invierte_texto(texto, caso_num):
    '''
    Función que dado un texto, divide en espacios en blanco e invierte el orden
    :param texto: Texto
    :param caso_num: Indice de numeración
    :return: Texto en orden inverso. La división es por espacios en blanco
    '''
    try:
        texto_lista = texto.split()
        texto_reverso_lista = reversed(texto_lista)
        texto_reverso = ' '.join(texto_reverso_lista)
        return f"Case #{caso_num}: {texto_reverso}"
    except Exception as e:
        print(f"Error in invierte_texto {e}")
        return None


def invierte_texto_lista(lista_textos):
    '''
    Función que invierte el orden de cada texto dentro de una lista de textos
    :param lista_textos: lista de textos originales
    :return: lista donde cada elemento es el texto en orden invertido
    '''
    try:
        lista_texto_invertido = [invierte_texto(x, enum + 1) for enum, x in enumerate(lista_textos)]
        if None in lista_texto_invertido:
            return None
        return '\n'.join(lista_texto_invertido)
    except Exception as e:
        print(f"Error en invierte_texto_lista: {e}")
        return None


def main():
    num_textos = input("Ingrese número de textos:\t")
    try:
        num_textos = int(num_textos)
        if num_textos > 0:
            lista_textos = []
            for i in range(num_textos):
                lista_textos.append(input(f"Ingrese texto {(i + 1)}:\t"))
            lista_texto_invertido = invierte_texto_lista(lista_textos=lista_textos)
            if lista_texto_invertido is not None:
                print(lista_texto_invertido)
        else:
            print(f"Ingrese número mayor a cero")
    except Exception as e:
        print(f"Error: {e}")
    input("Presione ENTER para cerrar la aplicación")


if __name__ == '__main__':
    main()
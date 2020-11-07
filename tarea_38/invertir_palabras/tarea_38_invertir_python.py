'''
Created on 25 jun. 2020
@author: jazielinho
'''


def invierte_texto(texto):
    '''
    Función que dado un texto, divide en espacios en blanco e invierte el orden
    :param texto: Texto
    :return: Texto en orden inverso. La división es por espacios en blanco
    '''
    try:
        texto_lista = texto.split()
        texto_reverso_lista = reversed(texto_lista)
        texto_reverso = ' '.join(texto_reverso_lista)
        return texto_reverso
    except Exception as e:
        print(f"Error in invierte_texto, texto: {texto}: {e}")
        return None


def invierte_lista_textos(lista_textos):
    '''
    Función que invierte el orden de cada texto dentro de una lista de textos
    :param lista_textos: lista de textos originales
    :return: mensaje con lista de palabras en orden inverso
    '''
    try:
        len_lista_textos = len(lista_textos)

        index_ = 0

        mostrar = ''

        while index_ < len_lista_textos:
            texto_reverso = invierte_texto(texto=lista_textos[index_])
            mostrar = mostrar + f'\nCase # {(index_ + 1)}: {texto_reverso}'
            index_ += 1
        return mostrar
    except Exception as e:
        print(f"Error in invierte_lista_textos, lista_textos: {lista_textos}: {e}")
        return None


def main():
    num_textos = input("Ingrese número de textos:\t")
    try:
        num_textos = int(num_textos)
        if num_textos > 0:
            lista_textos = []
            for i in range(num_textos):
                lista_textos.append(input(f"Ingrese texto {(i + 1)}:\t"))
            lista_texto_invertido = invierte_lista_textos(lista_textos=lista_textos)
            if lista_texto_invertido is not None:
                print(lista_texto_invertido)
        else:
            print(f"Ingrese número mayor a cero")
    except Exception as e:
        print(f"Error: {e}")
    input("Presione ENTER para cerrar la aplicación")


if __name__ == '__main__':
    main()
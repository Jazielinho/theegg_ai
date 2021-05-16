'''
Created on 1 may. 2020
@author: jazielinho
'''

import collections
import re


texto_base = '''En Strandhill, Irlanda, se cruzó en mi camino Chris, un señor de los que inspiran y se posicionan como referente. Fue una pieza fundamental en un momento de pura congelación. Te cuento? Strandhill es una playa donde el mar ruge muy bien, siempre está lleno de surfistas en busca de buenas olas. Y allí estaba yo también. Después de unos meses viviendo en una ciudad sin costa, mis ganas por hacer un poco de surfing estaban por las nubes. Aunque tenía un «pequeño» problema: no tenía equipo, ni tabla, ni neopreno, y tampoco había ninguna tienda para alquilarlo. Todo se puso a rodar enseguida. Escribí a un famoso surfista de la zona y recibí una respuesta increíble. «Mi casa está en la calle x, la puerta está abierta y tienes la tabla en la esquina. Ven cuando quieras», me dijo. Y eso hice, fui para allá y la cogí. Aunque el neopreno no me lo pudo prestar, y no porque se negara? Lamentablemente le sacaba unos 15 cm de altura. Luego, en la playa, un alemán me solucionó el tema del neopreno. Me prestó uno que había por su maletero, uno muy fino, de los que uso yo en el Mediterráneo en otoño o primavera. Y claro, era invierno y estábamos en Irlanda. El caso es que salí del agua más pronto de lo previsto y con las manos, la cabeza y los labios congelados. Me empecé a cambiar en el mismo paseo que contorneaba la costa y, estando semidesnudo, se me acercó Chris. «Está fría el agua, eh», apuntó este fenómeno. Chris superaba los 65 años y todos los días hacía un recorrido de decenas de kilómetros para llegar hasta allí. Sus gracietas y su buena conversación me hicieron apartar el frío de la parte de mi cabeza que se encarga de pensar, y hasta cantamos juntos la canción de Annie. Sé que esto último puede sonar raro, ¿quién canta Annie semidesudo y congelado en un paseo de Irlanda con un señor que acaba de conocer? Pero? seguro que a ti también te han pasado cosas así.'''


class ExpresionRegular(object):
    patron_caracter = re.compile(r'.')
    patron_caracter_sin_espacios_blanco = re.compile(r'[^\s]')
    patron_palabras = re.compile(r'\w+\b')

    def __init__(self, texto, nombre_archivo):
        if nombre_archivo is not None:
            try:
                self.texto = open(nombre_archivo, encoding='utf-8').read()
                self.texto_valido = True
            except Exception as e:
                print(f'Error al intentar abrir archivo: {e}')
                self.texto = ''
                self.texto_valido = False
        else:
            self.texto = texto
            self.texto_valido = True
        self.lista_palabras = []

    def calcula_caracteres(self):
        ''' Calcula el numero de caracteres que tiene un texto '''
        caracteres = self.patron_caracter.findall(self.texto)
        print(f'Número de caracteres: {len(caracteres)}')
        caracteres_sin_espacios = self.patron_caracter_sin_espacios_blanco.findall(self.texto)
        print(f'Número de caracteres sin espacios en blanco: {len(caracteres_sin_espacios)}')

    def _obtener_palabras(self):
        ''' Obtiene los nombres del texto '''
        self.lista_palabras = self.patron_palabras.findall(self.texto)

    def calcula_num_palabras(self):
        ''' Muestra el número de palabras que tiene el texto '''
        if len(self.lista_palabras) == 0:
            self._obtener_palabras()
        print(f"Número de palabras: {len(self.lista_palabras)}")

    def calcula_frecuencia_palabras(self):
        ''' Muestra Frecuencia de palabras que tiene el texto '''
        if len(self.lista_palabras) == 0:
            self._obtener_palabras()

        dict_palabras = {}

        for palabra in self.lista_palabras:
            dict_palabras[palabra] = dict_palabras.get(palabra, 0) + 1

        print('Frecuencia de palabras:')
        if len(dict_palabras) == 0:
            print('No se ha encontrado palabras')
        else:
            dict_palabras_ordenadas = collections.OrderedDict(sorted(dict_palabras.items(), key=lambda kv: kv[1],
                                                                     reverse=True))
            for palabra, cantidad in dict_palabras_ordenadas.items():
                print(f"{palabra}: {cantidad}")


def main():
    paso_opcion = True

    while paso_opcion:
        print('\n\n')
        print("Aplicación de expresiones regulares")
        print("1: Ingrese Texto")
        print("2: Ingrese Dirección del archivo")
        print("3: Usa texto por defecto")

        try:
            opcion = int(input('Ingrese opción: \t'))
        except Exception as e:
            print(f'Error al ingresar opcion: {e}')
            opcion = None

        if opcion == 1:
            texto = input('Ingrese Texto: \t')
            expresion_regular = ExpresionRegular(texto=texto, nombre_archivo=None)
            paso_opcion = not expresion_regular.texto_valido
        elif opcion == 2:
            nombre_archivo = input('Ingrese Nombre Archivo: \t')
            expresion_regular = ExpresionRegular(texto=None, nombre_archivo=nombre_archivo)
            paso_opcion = not expresion_regular.texto_valido
        elif opcion == 3:
            expresion_regular = ExpresionRegular(texto=texto_base, nombre_archivo=None)
            paso_opcion = not expresion_regular.texto_valido
        else:
            print('Opción no válida, intente de nuevo')

    print('\n\n\nESTADÍSTICAS:')
    print('\n\n')
    print('CARACTERES:')
    expresion_regular.calcula_caracteres()
    print('\n\n')
    print('PALABRAS:')
    expresion_regular.calcula_num_palabras()
    expresion_regular.calcula_frecuencia_palabras()

    print('\n')
    input("Presione cualquier tecla para salir de la aplicación")


if __name__ == '__main__':
    main()
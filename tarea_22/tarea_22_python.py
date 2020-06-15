'''
Created on 15 jun. 2020
@author: jazielinho
'''

import numpy as np
import tqdm
import itertools


class AlgoritmoLechero(object):
    '''
    Clase para calcular el algoritmo del Lechero
    '''

    def __init__(self, lista_pesos, maximo_peso, lista_produccion):
        '''
        :param lista_pesos: lista de pesos de las vacas
        :param maximo_peso: peso maximo en el camion
        :param lista_produccion: lista de produccion de las vacas
        '''
        assert len(lista_pesos) == len(lista_produccion)
        assert len(lista_pesos) > 0
        self.lista_pesos = lista_pesos
        self.maximo_peso = maximo_peso
        self.lista_produccion = lista_produccion
        self.num_vacas = len(self.lista_pesos)
        self.max_combinaciones = 2 ** self.num_vacas
        self.combinacion_optima = [0] * self.num_vacas
        self.maximo_valor = (-1) * np.inf
        self.peso_total = 0
        self.optimizacion_b = False

    def muestra_peso_total(self, seleccion):
        '''
        Calcula el peso total para cierta seleccion de ceros y unos
        :param seleccion: seleccion en ceros y unos
        :return:
        '''
        return np.dot(seleccion, self.lista_pesos)

    def compara_condicion(self, seleccion):
        '''
        Verifica si el peso total es menor al peso maximo
        :param seleccion: seleccion en ceros y unos
        :return:
        '''
        return self.muestra_peso_total(seleccion=seleccion) <= self.maximo_peso

    def muestra_produccion_total(self, seleccion):
        '''
        Calcula la produccion total para cierta seleccion de ceros y unos
        :param seleccion: seleccion en ceros y unos
        :return:
        '''
        return np.dot(seleccion, self.lista_produccion)

    def muestra_todas_combinaciones(self):
        '''
        Muestra todas las posibles combinaciones dependiendo del numero de vacas
        :return:
        '''
        return itertools.product([0, 1], repeat=self.num_vacas)

    def optimizar(self):
        '''
        Funcion principal, de todas las combinaciones posibles, busca la que maximiza la funcion objetivo
            (muestra_produccion_total)
        :return:
        '''
        try:
            maximo_valor = self.maximo_valor
            combinacion_optima = self.combinacion_optima
            posibles_combinaciones = self.muestra_todas_combinaciones()
            for combinacion in tqdm.tqdm(posibles_combinaciones, total=self.max_combinaciones):
                if self.compara_condicion(seleccion=combinacion):
                    produccion = self.muestra_produccion_total(combinacion)
                    if produccion >= maximo_valor:
                        maximo_valor = produccion
                        combinacion_optima = combinacion
            self.combinacion_optima = combinacion_optima
            self.maximo_valor = maximo_valor
            self.peso_total = self.muestra_peso_total(seleccion=self.combinacion_optima)
            self.optimizacion_b = True
            return True
        except Exception as e:
            print(f"Error en AlgoritmoLechero/optimizar {e}")
            self.optimizacion_b = False
            return False

    def de_seleccion_a_reglas(self):
        '''
        Muestra mensaje de la selecccion que maximiza la produccion total teniendo en cuenta el peso maximo
        :return:
        '''
        if self.optimizacion_b is False:
            print(""" Por favor ejecutar la optimizacion """)
        else:
            indice_seleccion_optima = np.where(self.combinacion_optima)[0].tolist()
            indice_seleccion_optima_texto = ', '.join([str(x + 1) for x in indice_seleccion_optima])
            texto = """ 'Algoritmo del lechero'
            Debes seleccionar las siguientes vacas: \n\t"""
            texto += indice_seleccion_optima_texto
            texto += """\nLa produccion maxima esperada es: {}""".format(self.maximo_valor)
            texto += """\nEl peso total en el camion es: {}""".format(self.peso_total)
            print(texto)


class PreparaInput():
    ''' Clase que convierte los textos a formato lista y entero'''
    @staticmethod
    def texto_a_lista(lista_texto):
        '''
        Convierte un texto separado por comas en una lista de enteros
        :param lista_texto: texto separados por comas
        :return: lista de enteros
        '''
        return [int(x) for x in lista_texto.split(',')]

    @staticmethod
    def texto_a_entero(texto):
        '''
        Convierte un texto a entero
        :param texto: text
        :return: entero
        '''
        return int(texto)


def main():
    lista_pesos = input("Ingrese lista de pesos de vacas separado por comas (,):\t")
    lista_produccion = input("Ingrese lista de produccion de vacas separado por comas (,):\t")
    maximo_peso = input("Ingrese peso maximo que el camion puede llevar:\t")
    lista_pesos = PreparaInput.texto_a_lista(lista_texto=lista_pesos)
    lista_produccion = PreparaInput.texto_a_lista(lista_texto=lista_produccion)
    maximo_peso = PreparaInput.texto_a_entero(texto=maximo_peso)

    algoritmo = AlgoritmoLechero(lista_pesos=lista_pesos, lista_produccion=lista_produccion, maximo_peso=maximo_peso)
    optimizacion = algoritmo.optimizar()
    if optimizacion:
        algoritmo.de_seleccion_a_reglas()

    input("Presione ENTER para cerrar la aplicacion")


if __name__ == '__main__':
    main()

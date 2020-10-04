'''
Created on 3 oct. 2020
@author: jazielinho
'''


class Pokemon(object):
    ''' Clase que crea el objeto pokemon '''
    def __init__(self, nombre, puntos_ataque):
        '''
            :param nombre: Nombre del Pokemon
            :param puntos_ataque: Puntos de ataque del Pokemon
        '''
        assert puntos_ataque > 0, 'ataque debe ser positivo'
        self.nombre = nombre
        self.puntos_ataque = puntos_ataque
        self.puntos_vida = 100

    def sigue_vivo(self):
        '''
            Verifica si el pokemon sigue con vida
            :return: True o False
        '''
        return self.puntos_vida > 0

    def recibe_ataque(self, puntos_ataque):
        '''
            Actualiza los puntos de vida del pokemon
            :param puntos_ataque: puntos de ataque del pokemon contrincante
        '''
        self.puntos_vida = self.puntos_vida - puntos_ataque

    def devuelve_puntos_ataque(self):
        '''
            Retorna los puntos de ataque
            :return: puntos de ataque
        '''
        return self.puntos_ataque


def enfrentamiento(pokemon_1, pokemon_2):
    '''
        Enfrenta al Pokemon 1 y Pokemon 2
        :param pokemon_1: Objeto Pokemon 1
        :param pokemon_2: Objeto Pokemon 2
        :return: pokemon que gana
    '''
    turno = 1

    ataque_pokemon_1 = pokemon_1.devuelve_puntos_ataque()
    ataque_pokemon_2 = pokemon_2.devuelve_puntos_ataque()

    print('Empieza el enfrentamiento:')

    while pokemon_1.sigue_vivo() and pokemon_2.sigue_vivo():

        if turno == 1:
            ''' Ataca primer pokemon '''
            print('     Ataca {}'.format(pokemon_1.nombre))
            pokemon_2.recibe_ataque(puntos_ataque=ataque_pokemon_1)
            turno = 0

        else:
            ''' Ataca primer pokemon '''
            print('     Ataca {}'.format(pokemon_2.nombre))
            pokemon_1.recibe_ataque(puntos_ataque=ataque_pokemon_2)
            turno = 1

    nombre_ganador = pokemon_1.nombre if pokemon_1.sigue_vivo() else pokemon_2.nombre
    puntos_vida_ganador = pokemon_1.puntos_vida if pokemon_1.sigue_vivo() else pokemon_2.puntos_vida

    print('Finaliza el enfrentamiento:')
    print('Ha ganado {}, con puntos de vida: {}'.format(nombre_ganador,
                                                        puntos_vida_ganador))


def main():
    ''' Pokemon 1 '''
    nombre_1 = input("Ingrese nombre del primer Pokemon:\t")
    ataque_1 = input("Ingrese los puntos de ataque:\t")
    ataque_1 = float(ataque_1)

    nombre_2 = input("Ingrese nombre del segundo Pokemon:\t")
    ataque_2 = input("Ingrese los puntos de ataque:\t")
    ataque_2 = float(ataque_2)

    pokemon_1 = Pokemon(nombre=nombre_1, puntos_ataque=ataque_1)
    pokemon_2 = Pokemon(nombre=nombre_2, puntos_ataque=ataque_2)

    enfrentamiento(pokemon_1, pokemon_2)
    input("Presione ENTER para cerrar la aplicación")


if __name__ == '__main__':
    main()
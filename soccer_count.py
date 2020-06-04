# -*- coding: utf-8 -*-
"""
@author: zejiran

Para preparar mejor los próximos partidos y asegurar el campeonato de la Premier League, el entrenador Jürgen Klopp
del Liverpool FC ha decidido estudiar algunas estadísticas de su equipo. Entre estas, ha decidido analizar los pases
que se realizan entre sus jugadores titulares (excluyendo al portero, lo que daría un total de 10 jugadores a
analizar), información que se puede representar en una matriz de la siguiente manera:

![Imagen matriz]

Las celdas en negro representan la imposibilidad de un jugador de hacerse pases a si mismo,
y las blancas llevan la cantidad de pases que ha realizado un jugador a otro.
Por ejemplo, la celda con coordenadas (3, 2) contiene la cantidad de pases que hizo Henderson a Firmino.

Uno de los datos de interés es la cantidad de pases que hace cada jugador en total.
Para esto, debe crear una función que reciba la matriz descrita anteriormente y una lista
con los nombres de los jugadores (que están en el mismo orden en que aparecen en las filas/columnas de la matriz)
y retorne una lista de tuplas, donde cada una contiene el nombre de un jugador y la cantidad total de pases
 que ha realizado a sus compañeros.
"""


def total_pases_jugador(matriz_pases: list, nombres_jugadores: list) -> list:
    """
    Función que calcula la cantidad de pases que hace cada jugador en total.

    :param matriz_pases: matriz de analisís de pases de titulares.
    :param nombres_jugadores: lista con los nombres de los jugadores, que están en el mismo orden en que
     aparecen en las filas/columnas de la matriz.
    :return: lista de tuplas, donde cada una contiene el nombre de un jugador y la cantidad total de pases
     que ha realizado a sus compañeros.

     :type matriz_pases: list.
     :type nombres_jugadores: list.
     :rtype: list.
    """
    total_goles = list()
    # Inicio de recorrido por matriz de goles.
    for i in range(1, len(matriz_pases)):
        nombre_actual = nombres_jugadores[i - 1]
        conteo_actual = 0
        # Inicio de recorrido por los goles cada jugador.
        for j in range(1, len(matriz_pases[0])):
            goles_actual = matriz_pases[i][j]
            if i != j:
                conteo_actual += goles_actual
        total_goles.append((nombre_actual, conteo_actual))
    return total_goles

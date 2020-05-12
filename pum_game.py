# -*- coding: utf-8 -*-
"""
@author: alxus27
"""


def pum(numero_jugadores: int, numero_pum: int) -> None:
    # Se define la posición de jugador actual y validez de parámetros.
    jugador = 1
    valido = True
    # Centinela.
    jugada = 1
    # Verificación del número pum menor que 10.
    if numero_pum >= 10:
        print("El número pum no es menor a 10")
        valido = False
    # Verificación de número de jugador.
    if numero_jugadores <= 0:
        print("No se puede jugar sin jugadores")
        valido = False
    # Impresión de encabezados.
    if valido:
        print('{0:}{1:>10}'.format("Jugador", "Jugada"))
    # Inicio de las rondas.
    while jugada <= 500 and valido:
        # Número ¡PUM!
        if jugada % numero_pum == 0:
            jugador_dice = "¡PUM!"
        else:
            jugador_dice = str(jugada)
        # Print de resultados en la jugada actual.
        print('{0:<10}{1}'.format(jugador, jugador_dice))
        # Jugador siguiente.
        if jugador == numero_jugadores:
            jugador = 1
        else:
            jugador += 1
        # Jugada siguiente.
        jugada += 1


pum(7, 5)

# -*- coding: utf-8 -*-
"""
@author: alxus27
"""


def fibonacci(terminos_sucesion: int) -> str:
    ith = 0
    # Primer número inicial.
    anterior = 0
    # Segundo número inicial.
    i = 1
    # Cadena inicial.
    cadena = ""
    while terminos_sucesion > 0:
        # Print de números y se añaden a cadena total.
        print(str(anterior))
        cadena += ", " + str(anterior)
        # Siguiente término centinela.
        terminos_sucesion -= 1
        # Siguientes números.
        ith = anterior + i
        anterior = i
        i = ith
    cadena = cadena[2:]
    print(cadena)
    return cadena


fibonacci(100)

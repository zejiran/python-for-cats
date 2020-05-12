# -*- coding: utf-8 -*-
"""
@author: zejiran.
"""


def matriz_identidad(n: int) -> list:
    matriz = []
    i = 0
    while i < n:
        columna = [0] * n
        columna[i] = 1
        matriz.append(columna)
        i += 1
    return matriz

# -*- coding: utf-8 -*-
"""
@author: alxus27
"""

import random


def generar_numero_aleatorio() -> str:
    centena = random.randint(0, 9)
    decena = random.randint(0, 9)
    unidad = random.randint(0, 9)
    if centena == decena:
        decena = random.randint(0, 9)
    if decena == unidad:
        unidad = random.randint(0, 9)
    if unidad == centena:
        unidad == random.randint(0, 9)
    aleatorio = str(centena) + str(decena) + str(unidad)
    return aleatorio


def intento_picas(intento: string, aleatorio) -> str:
    intento
    return


def intento_fijas(intento: string, aleatorio) -> str:

    return

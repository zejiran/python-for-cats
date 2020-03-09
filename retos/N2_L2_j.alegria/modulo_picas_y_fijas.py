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
        unidad = random.randint(0, 9)
    aleatorio = str(centena) + str(decena) + str(unidad)
    return aleatorio


def picas_y_fijas(numero_secreto: int, intento: int, intentos: dict) -> dict:
    """ Picas y Fijas
    Parámetros:
      numero_secreto (int): Número el cual se debe adivinar
      intento (int): Número el cual trata de adivinar
    Retorno:
      dict: Diccionario con las llaves "PICAS" y "FIJAS" que describe el resultado de la jugada.
    """
    unidad_intento = intento % 10
    unidad_secreto = numero_secreto % 10
    intento //= 10
    numero_secreto //= 10
    decena_intento = intento % 10
    decena_secreto = numero_secreto % 10
    intento //= 10
    numero_secreto //= 10
    centena_intento = intento // 10
    centena_secreto = numero_secreto // 10
    # Picas
    picas = 0
    if unidad_intento == decena_secreto:
        picas += 1
    if unidad_intento == centena_secreto:
        picas += 1
    if decena_intento == unidad_secreto:
        picas += 1
    if decena_intento == centena_secreto:
        picas += 1
    if centena_intento == unidad_secreto:
        picas += 1
    if centena_intento == decena_secreto:
        picas += 1
    # Fijas
    fijas = 0
    if unidad_intento == unidad_secreto:
        fijas += 1
    if decena_intento == decena_secreto:
        fijas += 1
    if centena_intento == centena_secreto:
        fijas += 1
    # Diccionario resultado
    intentos["INTENTOS"] -= 1
    resultado = {"PICAS": picas, "FIJAS": fijas, "INTENTOS": intentos["INTENTOS"]}
    return resultado

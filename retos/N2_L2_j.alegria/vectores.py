# -*- coding: utf-8 -*-
"""
@author: alxus27
"""

import math


def calcular_dimensiones_area_direccion(vector: dict) -> dict:
    vector["v"] = math.sqrt(pow(vector['x'], 2) + pow(vector['y'], 2))
    vector["direccion"] = math.atan(vector['y'] / vector['x'])
    vector["area"] = (vector['x'] * vector['y']) / 2
    return vector


def tresvectores(vector1: dict, vector2: dict, vector3: dict) -> dict:
    determinacion = {"alineados": False, "mayor_area": "uno"}
    vector1 = calcular_dimensiones_area_direccion(vector1)
    vector2 = calcular_dimensiones_area_direccion(vector2)
    vector3 = calcular_dimensiones_area_direccion(vector3)
    if vector1["direccion"] == vector2["direccion"] and vector1["direccion"] == vector3["direccion"]:
        determinacion["alineados"] = True
    else:
        determinacion["alineados"] = False
    areadeterminada = "vector 1"
    mayor_area = vector1["area"]
    if vector2["area"] > mayor_area:
        mayor_area = vector2["area"]
        areadeterminada = "vector 2"
    if vector3["area"] > mayor_area:
        areadeterminada = "vector 3"
    determinacion["mayor_area"] = areadeterminada
    return determinacion

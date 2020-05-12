# -*- coding: utf-8 -*-
"""
@author: zejiran.
"""

import vectors_module as vect


def ejecutar_calcular_dimensiones_area_direccion() -> None:
    vector = {"x": int(input("Digite la coordenada x del vector: ")),
              "y": int(input("Digite la coordenada y del vector: "))}
    vector = vect.calcular_dimensiones_area_direccion(vector)
    print("\nLa magnitud del vector es: " + str(vector["v"]))
    print("El área del vector es: " + str(vector["area"]))


def ejecutar_tresvectores() -> None:
    vector1 = {"x": int(input("\nDigite la coordenada x del vector 1: ")),
               "y": int(input("Digite la coordenada y del vector 1: "))}
    vector2 = {"x": int(input("\nDigite la coordenada x del vector 2: ")),
               "y": int(input("Digite la coordenada y del vector 2: "))}
    vector3 = {"x": int(input("\nDigite la coordenada x del vector 3: ")),
               "y": int(input("Digite la coordenada y del vector 3: "))}
    determinacion = vect.tresvectores(vector1, vector2, vector3)
    if determinacion["alineados"]:
        print("\nLos vectores tienen la misma dirección")
    else:
        print("\nLos vectores no tienen la misma dirección")
    print("El vector de mayor área es: " + determinacion["mayor_area"])


def iniciar_aplicacion() -> None:
    print("Bienvenido")
    ejecutar_calcular_dimensiones_area_direccion()
    ejecutar_tresvectores()


iniciar_aplicacion()

# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 21:47:01 2019

@author: Cupi2
"""

import analisis as mod


def ejecutar_analizar_anio() -> None:
    anio = int(input("Ingrese el año que desea analizar: "))
    resultado = mod.analizar_anio(anio)
    print(resultado)


def iniciar_aplicacion() -> None:
    print("Bienvenido al analizador de años")
    ejecutar_analizar_anio()


# PROGRAMA PRINCIPAL
iniciar_aplicacion()

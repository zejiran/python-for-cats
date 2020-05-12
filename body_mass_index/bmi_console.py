# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 10:49:23 2020

@author: zejiran.
"""

import index_calculator_module as calc


def ejecutar_calcular_IMC() -> None:
    peso = float(input("Ingrese el peso de la persona en kilogramos: "))
    altura = float(input("Ingrese la altura de la persona en metros: "))
    imc = calc.calcular_IMC(peso, altura)
    print("\nSu índice de masa corporal es " + str(imc))


def iniciar_aplicacion() -> None:
    print("\nBienvenido a la calculadora del índice de masa corporal\n")
    ejecutar_calcular_IMC()


# PROGRAMA PRINCIPAL
iniciar_aplicacion()

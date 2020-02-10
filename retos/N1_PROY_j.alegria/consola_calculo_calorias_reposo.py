# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 10:49:23 2020

@author: j.alegria
"""

import calculadora_indices as calc


def ejecutar_calcular_calorias_en_reposo() -> None:
    peso = float(input("Ingrese el peso de la persona en kilogramos: "))
    altura = float(input("Ingrese la altura de la persona en centimetros: "))
    edad = int(input("Ingrese la edad de la persona: "))
    valor_genero = float(input("Ingrese el valor -161 si es mujer, o 5 en caso de ser hombre: "))
    tmb = calc.calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
    print("\nLa persona quema " + str(tmb) + " cal en reposo")


def iniciar_aplicacion() -> None:
    print("\nBienvenido a la calculadora de la tasa metabólica basal\n")
    ejecutar_calcular_calorias_en_reposo()


# PROGRAMA PRINCIPAL
iniciar_aplicacion()


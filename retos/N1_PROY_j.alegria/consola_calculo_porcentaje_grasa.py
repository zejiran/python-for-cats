# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 10:49:23 2020

@author: j.alegria
"""

import calculadora_indices as calc


def ejecutar_calcular_porcentaje_grasa() -> None:
    peso = float(input("Ingrese el peso de la persona en kilogramos: "))
    altura = float(input("Ingrese la altura de la persona en metros: "))
    imc = calc.calcular_IMC(peso, altura)
    edad = int(input("Ingrese la edad de la persona: "))
    valor_genero = float(input("Ingrese el valor 0 si es mujer, o 10.8 en caso de ser hombre: "))
    pgc = calc.calcular_porcentaje_grasa(imc, edad, valor_genero)
    print("\nSu porcentaje de grasa corporal es " + str(pgc) + "%")


def iniciar_aplicacion() -> None:
    print("\nBienvenido a la calculadora del porcentaje de grasa corporal\n")
    ejecutar_calcular_porcentaje_grasa()


# PROGRAMA PRINCIPAL
iniciar_aplicacion()

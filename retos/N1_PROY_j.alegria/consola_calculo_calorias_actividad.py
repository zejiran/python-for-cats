# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 10:49:23 2020

@author: j.alegria
"""

import calculadora_indices as calc


def ejecutar_calcular_calorias_en_actividad() -> None:
    peso = float(input("Ingrese el peso de la persona en kilogramos: "))
    altura = float(input("Ingrese la altura de la persona en centimetros: "))
    edad = int(input("Ingrese la edad de la persona: "))
    valor_genero = float(input("Ingrese el valor -161 si es mujer, o 5 en caso de ser hombre: "))
    tmb = calc.calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
    valor_actividad = float(input("\nDe acuerdo a los siguientes valores digite el valor correspondiente a la "
                                  "persona:\n\n1.2: poco o ningún ejercicio\n1.375: ejercicio ligero (1 a 3 días a la "
                                  "semana)\n1.55: ejercicio moderado (3 a 5 días a la semana)\n1.72: deportista (6 -7 "
                                  "días a la semana)\n1.9: atleta (entrenamientos mañana y tarde)\n\nValor de "
                                  "actividad: "))
    tmbsaf = calc.calcular_calorias_en_actividad(tmb, valor_actividad)
    print("\nLa persona quema " + str(tmbsaf) + " cal en actividad")


def iniciar_aplicacion() -> None:
    print("\nBienvenido a la calculadora de la tasa metabólica basal según la actividad física\n")
    ejecutar_calcular_calorias_en_actividad()


# PROGRAMA PRINCIPAL
iniciar_aplicacion()

# -*- coding: utf-8 -*-
"""
created by zejiran

"""

import conditionals_practice_module as md


def ejecutar_bisiesto()->None:
    print("Vamos a decidir si un año es bisiesto o no")
    anio = int(input("Digite el año correspondiente: "))
    bisiesto = md.bisiesto(anio)
    if bisiesto == True:
        print("\nEl año es bisiesto.")
    else:
        print("\nEl año no es bisiesto.")

def ejecutar_clasificar()->None:
    print("Vamos a determinar de qué tipo es un triángulo dados sus ángulos")
    a1 = float(input("Digite el primer ángulo: "))
    a2 = float(input("Digite el segundo ángulo: "))
    a3 = float(input("Digite el tercer ángulo: "))
    tipo = md.clasificar(a1, a2, a3)
    print("\nSu triángulo es: " + tipo + ".")

def ejecutar_solucionar()->None:
    print("Vamos a tratar de hallar las soluciones de una ecuación cuadrática")
    a = float(input("Digite el término de segundo grado: "))
    b = float(input("Digite el término de primer grado: "))
    c = float(input("Digite el término sin variable: "))
    solucion = md.solucionar(a, b, c)
    print(solucion)

def mostrar_menu()->None:
    print ("Menu principal")
    print ("(1) Año bisiesto")
    print ("(2) Tipo de triángulo")
    print ("(3) Solución ecuación cuadrática")

    x = int(input("Seleccione su opción: "))

    if x == 1:
        ejecutar_bisiesto()
    elif x == 2:
        ejecutar_clasificar()
    elif x == 3:
        ejecutar_solucionar()
    else:
        print("Su elección no es válida")


def iniciar_aplicacion()->None:
    print("Bienvenido al laboratorio de condicionales")
    mostrar_menu()

#PROGRAMA PRINCIPAL
iniciar_aplicacion()

    
# -*- coding: utf-8 -*-
"""
@author: alxus27
"""


def movimiento_robot(orientacion_actual: str, giro_1: str, giro_2: str, giro_3: str) -> str:
    """ Movimiento robótico - V2
    Parámetros:
      orientacion_actual (str): La orientación actual del robot
      giro_1 (str): La acción a ejecutar a partir de la orientación inicial del robot. Debe ser un valor de

                    los siguientes: {"L","H","R","."}
      giro_2 (str): La acción a ejecutar a partir de la orientación posterior al giro_1 del robot. Debe ser
                    un valor de los siguientes: {"L","H","R","."}
      giro_3 (str): La acción a ejecutar a partir de la orientación posterior al giro_2 del robot. Debe ser
                    un valor de los siguientes: {"L","H","R","."}
    Retorno:
      str: La orientación final del robot, debe ser uno de los siguientes valores:  {"W","N","S","E"}
    """
    orientacion_actual = movimiento_1(orientacion_actual, giro_1)
    orientacion_actual = movimiento_2(orientacion_actual, giro_2)
    orientacion_actual = movimiento_3(orientacion_actual, giro_3)
    return orientacion_actual


def movimiento_1(orientacion_actual: str, giro_1: str) -> str:
    # Primer giro
    # Norte
    if orientacion_actual == "N":
        if giro_1 == "L":
            orientacion_actual = "W"
        elif giro_1 == "H":
            orientacion_actual = "S"
        elif giro_1 == "R":
            orientacion_actual = "E"
        elif giro_1 == ".":
            orientacion_actual = orientacion_actual
        else:
            print("Comando no válido")
    # Sur
    elif orientacion_actual == "S":
        if giro_1 == "L":
            orientacion_actual = "E"
        elif giro_1 == "H":
            orientacion_actual = "N"
        elif giro_1 == "R":
            orientacion_actual = "W"
        elif giro_1 == ".":
            orientacion_actual = orientacion_actual
        else:
            print("Comando no válido")
    # Este
    elif orientacion_actual == "E":
        if giro_1 == "L":
            orientacion_actual = "N"
        elif giro_1 == "H":
            orientacion_actual = "W"
        elif giro_1 == "R":
            orientacion_actual = "S"
        elif giro_1 == ".":
            orientacion_actual = orientacion_actual
        else:
            print("Comando no válido")
    # Oeste
    elif orientacion_actual == "W":
        if giro_1 == "L":
            orientacion_actual = "S"
        elif giro_1 == "H":
            orientacion_actual = "E"
        elif giro_1 == "R":
            orientacion_actual = "N"
        elif giro_1 == ".":
            orientacion_actual = orientacion_actual
        else:
            print("Comando no válido")
    else:
        print("Dirección no válida")
    return orientacion_actual


def movimiento_2(orientacion_actual: str, giro_2: str) -> str:
    # Giro 2
    # Norte
    if orientacion_actual == "N":
        if giro_2 == "L":
            orientacion_actual = "W"
        elif giro_2 == "H":
            orientacion_actual = "S"
        elif giro_2 == "R":
            orientacion_actual = "E"
        elif giro_2 == ".":
            orientacion_actual = orientacion_actual
        else:
            print("Comando no válido")
    # Sur
    elif orientacion_actual == "S":
        if giro_2 == "L":
            orientacion_actual = "E"
        elif giro_2 == "H":
            orientacion_actual = "N"
        elif giro_2 == "R":
            orientacion_actual = "W"
        elif giro_2 == ".":
            orientacion_actual = orientacion_actual
        else:
            print("Comando no válido")
    # Este
    elif orientacion_actual == "E":
        if giro_2 == "L":
            orientacion_actual = "N"
        elif giro_2 == "H":
            orientacion_actual = "W"
        elif giro_2 == "R":
            orientacion_actual = "S"
        elif giro_2 == ".":
            orientacion_actual = orientacion_actual
        else:
            print("Comando no válido")
    # Oeste
    elif orientacion_actual == "W":
        if giro_2 == "L":
            orientacion_actual = "S"
        elif giro_2 == "H":
            orientacion_actual = "E"
        elif giro_2 == "R":
            orientacion_actual = "N"
        elif giro_2 == ".":
            orientacion_actual = orientacion_actual
        else:
            print("Comando no válido")
    else:
        print("Dirección no válida")
    return orientacion_actual


def movimiento_3(orientacion_actual: str, giro_3: str) -> str:
    # Giro 3
    # Norte
    if orientacion_actual == "N":
        if giro_3 == "L":
            orientacion_actual = "W"
        elif giro_3 == "H":
            orientacion_actual = "S"
        elif giro_3 == "R":
            orientacion_actual = "E"
        elif giro_3 == ".":
            orientacion_actual = orientacion_actual
        else:
            print("Comando no válido")
    # Sur
    elif orientacion_actual == "S":
        if giro_3 == "L":
            orientacion_actual = "E"
        elif giro_3 == "H":
            orientacion_actual = "N"
        elif giro_3 == "R":
            orientacion_actual = "W"
        elif giro_3 == ".":
            orientacion_actual = orientacion_actual
        else:
            print("Comando no válido")
    # Este
    elif orientacion_actual == "E":
        if giro_3 == "L":
            orientacion_actual = "N"
        elif giro_3 == "H":
            orientacion_actual = "W"
        elif giro_3 == "R":
            orientacion_actual = "S"
        elif giro_3 == ".":
            orientacion_actual = orientacion_actual
        else:
            print("Comando no válido")
    # Oeste
    elif orientacion_actual == "W":
        if giro_3 == "L":
            orientacion_actual = "S"
        elif giro_3 == "H":
            orientacion_actual = "E"
        elif giro_3 == "R":
            orientacion_actual = "N"
        elif giro_3 == ".":
            orientacion_actual = orientacion_actual
        else:
            print("Comando no válido")
    else:
        print("Dirección no válida")
    return orientacion_actual


def verificar_nit(NIT: int, digito: int) -> bool:
    """ Verificar NIT
    Parámetros:
      NIT (int): NIT de una empresa, sin dígito de verificación
      digito (int): Dígito de verificación
    Retorno:
      bool: Retorna True si el dígito de verificación era correcto y False de lo contrario
    """
    residuo = procesamiento_de_digitos(NIT)
    if residuo == 0 or residuo == 1:
        # Es el digito de verificación
        residuo = residuo
    else:
        # Hay que restar el residuo a 11
        residuo = 11 - residuo
    if residuo == digito:
        verificacion = True
    else:
        verificacion = False
    return verificacion


def procesamiento_de_digitos(NIT: int) -> int:
    cadena = str(NIT)
    p0 = int(cadena[0]) * 41
    p1 = int(cadena[1]) * 37
    p2 = int(cadena[2]) * 29
    p3 = int(cadena[3]) * 23
    p4 = int(cadena[4]) * 19
    p5 = int(cadena[5]) * 17
    p6 = int(cadena[6]) * 13
    p7 = int(cadena[7]) * 7
    p8 = int(cadena[8]) * 3
    suma_productos = p0 + p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8
    residuo = suma_productos % 11
    return residuo

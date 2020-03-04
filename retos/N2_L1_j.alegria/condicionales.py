# -*- coding: utf-8 -*-
"""
created by j.alegria

"""


def bisiesto(anio: int) -> bool:
    """
    Retorna true si el año es bisiesto y false si no lo es.
    """
    if (anio % 4) == 0:
        retorno = True
    elif (anio % 100) == 0:
        retorno = False
    elif (anio % 400) == 0:
        retorno = True
    else:
        retorno = True
    return retorno


def clasificar(a1: float, a2: float, a3: float) -> str:
    """
    Retorna 'Equilatero' si el triángulo es equilatero, 'Isóceles'
    si es isóceles y 'Escaleno' si es escaleno.
    """
    if a1 == a2 and a1 == a3 and a2 == a3:
        retorno = "Equilatero"
    elif a1 == a2 or a1 == a3 or a2 == a3:
        retorno = "Isóceles"
    else:
        retorno = "Escaleno"
    return retorno

def solucionar(a: float, b: float, c: float) -> str:
    """
    Retorna una cadena con la(s) soluciones de la ecuación o una
    cadena diciendo que no tiene solucion.
    """
    discriminante = (b ** 2) - 4 * a * c
    if discriminante > 0:
        r1 = (-b + (discriminante ** (1 / 2))) / (2 * a)
        r2 = (-b - (discriminante ** (1 / 2))) / (2 * a)
        r1 = str(r1)
        r2 = str (r2)
        coma = ", "
        return "Su solución es: " + r1 + coma + r2 + "."
    elif discriminante == 0:
        r1 = (-b) / (2 * a)
        return "Su solución es: " + r1 + "."
    else:
        r = "No tiene solución"
        return r

    
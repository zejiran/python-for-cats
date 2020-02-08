# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 21:48:29 2019

@author: Cupi2
"""


def analizar_anio(anio: int) -> str:
    """ Realiza el análisis del año recibido por parámetro.
    Parámetros:
        anio (int) Año que se desea analizar. Debe ser un número entero 
        positivo.
    Retorno:
        str: Mensaje con la forma "El año X hace parte del milenio Y, siglo Z, 
        y década W."
    """
    # Las siguientes instrucciones permiten calcular el milenio
    # el siglo y le década del año ingresado por el usuario
    milenio = anio // 1000 + 1
    siglo = anio // 100 + 1
    decada = (anio % 100) // 10 + 1

    # Se construye el string de respuesta
    respuesta = "El año " + str(anio) + " hace parte del milenio " + \
                str(milenio) + ", siglo " + str(siglo) + " y década " + \
                str(decada) + "."

    # Se retorna el string
    return respuesta

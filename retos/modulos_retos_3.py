# -*- coding: utf-8 -*-
"""
@author: alxus27
"""

import math


def letra_mas_comun(cadena: str) -> str:
    """ Letra
    Parámetros:
      cadena (str): La cadena en la que se quiere saber cuál es la letra más común
    Retorno:
      str: La letra más común en la cadena que ingresa como parámetro,  si son dos es la letra alfabéticamente
           posterior.
    """
    letras_en_conteo = {}
    mayor_conteo = 0
    letra_moda = ""
    for cada_caracter in cadena:
        if cada_caracter != " " and cada_caracter != "," and cada_caracter != ".":
            # Conteo de cada caracter
            if cada_caracter not in letras_en_conteo:
                letras_en_conteo[cada_caracter] = 1
            else:
                letras_en_conteo[cada_caracter] += 1
            # Verificación del mayor carácter contado
            if letras_en_conteo[cada_caracter] == mayor_conteo:
                if cada_caracter > letra_moda:
                    letra_moda = cada_caracter
            elif letras_en_conteo[cada_caracter] > mayor_conteo:
                mayor_conteo = letras_en_conteo[cada_caracter]
                letra_moda = cada_caracter
    print(letras_en_conteo)
    print(letra_moda)
    return letra_moda


def contar_caracteres_repetidos(cadena: str) -> int:
    """ Caracteres Repetidos
    Parámetros:
      cadena (str): La cadena que se debe revisar.
    Retorno:
      int: La cantidad de caracteres diferentes que aparecen repetidos en la cadena.
    """
    caracteres_cadena = {}
    diferentes_repetidos = 0
    for caracter in cadena:
        # Conteo de cada caracter.
        if caracter not in caracteres_cadena:
            caracteres_cadena[caracter] = 1
        else:
            caracteres_cadena[caracter] += 1
        # Verificación de repetición mayor a una vez.
        if caracteres_cadena[caracter] == 2:
            diferentes_repetidos += 1
    return diferentes_repetidos


def es_primo(numero: int) -> bool:
    """ Encontrar si un número es primo
    Parámetros:
      numero (int): Entero que se busca ver si es primo
    Retorno:
      bool: Booleano que indica si el número entero recibido por parámetro es primo
    """
    primo = True
    for i in range(2, numero):
        if numero % i == 0:
            primo = False
    return primo


def invicto_mas_largo(goles_diccionarios: list, goles_adversario: list) -> int:
    """ Invictos
    Parámetros:
      goles_diccionarios (list): Los goles anotados por Diccionarios F.C en cada una de las fechas. Se
                                 garantiza que cada elemento de la lista es un entero no negativo.
      goles_adversario (list): Los goles anotados por los adversarios de Diccionarios F.C en cada una de las
                               fechas. Se garantiza que cada elemento de la lista es un entero no negativo.
    Retorno:
      int: Retorna la cantidad máxima de fechas consecutivas en que el equipo Diccionarios F.C no perdió
           durante la temporada anterior.
    """
    consecutivos_mayor = 0
    i = 0
    consecutivos = 0
    while i < len(goles_diccionarios):
        if goles_diccionarios[i] >= goles_adversario[i]:
            consecutivos += 1
            if consecutivos > consecutivos_mayor:
                consecutivos_mayor = consecutivos
        else:
            consecutivos = 0
        i += 1
    return consecutivos_mayor


def seno(x: float) -> float:
    """ Cálculo del Seno
    Parámetros:
      x (float): Número al cuál se le debe calcular el seno
    Retorno:
      float: Seno de x calculado con 5 cifras de redondeo
    """
    pass

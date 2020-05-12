# -*- coding: utf-8 -*-
"""
@author: j.alegria
"""


def es_palindroma(cadena: str) -> bool:
    """
    Indica si la cadena recibida por parámetro es palíndroma
    Parámetros:
        cadena: cadena a analizar
    Retorno:
        True si la cadena es palíndroma, false de lo contrario
    """
    es_o_no_palindroma = False
    cadena = cadena.lower()
    regular = ""
    invertida = ""
    for caracter in cadena:
        if "A" <= caracter <= "z":
            regular = regular + caracter
            invertida = caracter + invertida
    if regular == invertida:
        es_o_no_palindroma = True
    return es_o_no_palindroma


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
        if cada_caracter >= "A" and cada_caracter <= "z":
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


def invertir_cadena(cadena: str) -> str:
    invertida = ""
    for cada_letra in cadena:
        invertida = cada_letra + invertida
    return invertida

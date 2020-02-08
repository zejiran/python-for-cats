# -*- coding: utf-8 -*-
"""
@author: alxus27
"""


def area_habitacion(largo: float, ancho: float) -> float:
    """ Área de una habitación
    Parámetros:
      largo (float): Largo de la habitación
      ancho (float): Ancho de la habitación
    Retorno:
      float: Número (float) que representa el área de la habitación con dos decimales.
    """
    area = largo * ancho
    resultado = round(area, 2)
    return resultado


def calcular_distancia_manhattan(x1: int, y1: int, x2: int, y2: int) -> int:
    return abs(x1 - x2) + abs(y1 - y2)


def calcular_tarifa_taxi(kms_recorridos: float) -> int:
    cien_metros = (kms_recorridos * 1000) / 100
    tarifa = 4000 + (82 * cien_metros)
    return int(round(tarifa))


def convertir_eficiencia_combustible(millas_por_galon: float) -> float:
    conversion = 236.25 / millas_por_galon
    return round(conversion, 2)


def calcular_mediana(a: int, b: int, c: int) -> int:
    """ Mediana
    Parámetros:
      a (int): El primer entero del conjunto de datos
      b (int): El segundo entero del conjunto de datos
      c (int): El tercer entero del conjunto de datos
    Retorno:
      int: La mediana de los 3 enteros
    """
    suma = a + b + c
    mayor = max(a, b, c)
    menor = min(a, b, c)
    mediana = suma - mayor - menor
    return mediana


def calcular_cambio(cambio: int) -> str:
    """ Cambio a retornar
    Parámetros:
      cambio (int): Valor a retornar al comprador
    Retorno:
      str: Cadena de caracteres que indica cuántas monedas de cada denominación se deben retornar (usando la
           menor cantidad de monedas posible).
    """
    c500 = cambio // 500
    cambio = cambio % 500
    c200 = cambio // 200
    cambio = cambio % 200
    c100 = cambio // 100
    cambio = cambio % 100
    c50 = cambio // 50
    cadena = str(c500) + "," + str(c200) + "," + str(c100) + "," + str(c50)
    return cadena

# -*- coding: utf-8 -*-
"""
@author: alxus27
"""

import math


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


def suma_n_enteros_positivos(n: int) -> int:
    """ Suma de los primeros N enteros positivos
    Parámetros:
      n (int): Número entero hasta el cual se quiere calcular la suma, desde 1
    Retorno:
      int: Suma de los primeros N enteros positivos.
    """
    suma = n * (n + 1) / 2
    suma = int(suma)
    return suma


def calcular_iva_propina_total_factura(costo_factura: int) -> str:
    """ IVA y propina
    Parámetros:
      costo_factura (int): Costo de la factura del restaurante, sin impuestos ni propina
    Retorno:
      str: Cadena con el iva, propina y total de la factura, separados por coma
    """
    iva = costo_factura * 0.19
    propina = costo_factura * 0.10
    total = iva + propina + costo_factura
    cadena = str(round(iva)) + "," + str(round(propina)) + "," + str(round(total))
    return cadena


def altura_en_mts(pies: int, pulgadas: int) -> float:
    """ Altura de una persona
    Parámetros:
      pies (int): Número de pies que componen la altura de la persona
      pulgadas (int): Número de pulgadas que componen la altura de la persona
    Retorno:
      float: Altura en metros de la persona, la cual debe estar redondeada a dos cifras decimales.
    """
    pulgadas_totales = (pies * 12) + pulgadas
    centimetros = pulgadas_totales * 2.54
    metros = round((centimetros / 100), 2)
    return metros


def calcular_pago_botellas(cant_pequenias: int, cant_grandes: int) -> float:
    """ Reciclaje de botellas plásticas
    Parámetros:
      cant_pequenias (int): Cantidad de botellas pequeñas entregadas
      cant_grandes (int): Cantidad de botellas grandes entregadas
    Retorno:
      float: Cantidad de dinero a pagar por las botellas plásticas para reciclaje con dos decimales.
    """
    pago_pequenias = cant_pequenias * 0.10
    pago_grandes = cant_grandes * 0.25
    dinero_pago = round(pago_grandes + pago_pequenias, 2)
    return dinero_pago


def volumen_cilindro(radio: float, altura: float) -> float:
    """ Volumen de un cilindro
    Parámetros:
      radio (float): Radio de la base del cilindro
      altura (float): Altura del cilindro
    Retorno:
      float: El volumen del cilindro readondeado a un decimal
    """
    area_base = math.pi * (radio ** 2)
    volumen = area_base * altura
    return round(volumen, 1)


def tiempo_a_segundos(dias: int, horas: int, mins: int, seg: int) -> int:
    """ Unidades de tiempo a segundos
    Parámetros:
      dias (int): Número de dias del periodo de tiempo
      horas (int): Número de horas del periodo de tiempo
      mins (int): Número de minutos del periodo de tiempo
      seg (int): Número de segundos del periodo de tiempo
    Retorno:
      int: Número de segundos al que equivale el periodo de tiempo dado como parámetro
    """
    dias_a_horas = dias * 24
    horas_a_minutos = (dias_a_horas + horas) * 60
    minutos_a_segundos = (horas_a_minutos + mins) * 60
    segundos_totales = minutos_a_segundos + seg
    return int(segundos_totales)


def saludar_repetidas_veces(nombre: str, veces: int) -> str:
    """ Saludo prolongado
    Parámetros:
      nombre (str): Nombre a incluir en el saludo
      veces (int): Cantidad de veces a repetir las letras
    Retorno:
      str: Cadena con el saludo con letras repetidas
    """
    saludo = "H" + "o" * veces + "l" + "a" * (int(veces / 2))
    return saludo + " " + nombre


def calcular_tiempo_descarga(velocidad: int, tamanio_archivo: int) -> int:
    """ Tiempo de descarga
    Parámetros:
      velocidad (int): Velocidad de descarga de la red, en Mbps
      tamanio_archivo (int): Tamaño del archivo a descargar, en GB
    Retorno:
      int: Tiempo estimado en minutos que toma la descarga del archivo
    """
    megabits_megabyte = velocidad / 8
    megabyte_gigabyte = megabits_megabyte / 1000
    tiempo = tamanio_archivo / megabyte_gigabyte
    segundos_minutos = round(tiempo / 60)
    return segundos_minutos


def calcular_total_pan_comprado(frescos: int, viejos: int) -> int:
    """ Pan del día anterior
    Parámetros:
      frescos (int): Cantidad de panes frescos comprados
      viejos (int): Cantidad de panes del día anterior comprados
    Retorno:
      int: Valor total a pagar por el pan comprado
    """
    costo_fresco = frescos * 450
    costo_viejo = viejos * (450 * 0.40)
    pan_comprado = costo_fresco + costo_viejo
    return round(pan_comprado)


def ordenar_enteros(a: int, b: int, c: int) -> str:
    """ Ordenar 3 enteros
    Parámetros:
      a (int): El primero de los enteros a ordenar
      b (int): El segundo de los enteros a ordenar
      c (int): El tercero de los enteros a ordenar
    Retorno:
      str: Cadena de caracteres con los enteros ordenados de  mayor a menor, separados por coma
    """
    suma = a + b + c
    mayor = max(a, b, c)
    menor = min(a, b, c)
    intermedio = suma - mayor - menor
    cadena = str(mayor) + "," + str(intermedio) + "," + str(menor)
    return cadena



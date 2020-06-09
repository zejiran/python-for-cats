# -*- coding: utf-8 -*-
"""
@author: zejiran.
"""


def matriz_identidad(n: int) -> list:
    matriz = []
    i = 0
    while i < n:
        columna = [0] * n
        columna[i] = 1
        matriz.append(columna)
        i += 1
    return matriz


def hacer_la_vaca(salon: list, vaca: str) -> tuple:
    """ Vaca de Cumpleaños
    Parámetros:
      salon (list): Matriz que representa el salón de estudiantes y con enteros que representan cuanto
                    dinero aportarán
      vaca (str): Cadena que indica qué vaca se está realizando, esta puede ser 'botella' o 'pastel'
    Retorno:
      tuple: Tupla cuya primera posición es un str de la forma 'Hay Vaca' si se alcanzó la vaca, y 'No Alcanza'
             de lo contrario, y las siguientes dos posiciones son las coordenadas del estudiante qué más dinero
             aportó.
    """
    el_rico = [0, 0]
    regalon_del_rico = 0
    hay_vaca = False
    if vaca == 'botella':
        recolecta = 120000
    elif vaca == 'pastel':
        recolecta = 35000
    else:
        recolecta = -1000000000000000
    i = 0
    while i < len(salon):
        j = 0
        while j < len(salon[i]):
            aporte_estudiante = salon[i][j]
            # Verificar el mayor aporte.
            if regalon_del_rico < aporte_estudiante:
                regalon_del_rico = aporte_estudiante
                el_rico = [i, j]
            # Restar a la vaca.
            recolecta -= aporte_estudiante
            if recolecta <= 0 and recolecta != -1000000000000000:
                hay_vaca = True
            else:
                hay_vaca = False
            j += 1
        i += 1
    if hay_vaca:
        retorno = 'Hay Vaca'
    else:
        retorno = 'No Alcanza'
    el_rico.insert(0, retorno)
    return tuple(el_rico)


def calcular_suma_diagonal(diagonal_mayor: bool, matriz: list) -> int:
    """ Suma en la diagonal
    Parámetros:
      diagonal_mayor (bool): bool que indica a cual de las diagonales se debe calcularle la suma. Si es
                             True, se quiere calcular la suma de la diagonal mayor.
      matriz (list): Lista de listas, representa la matriz cuadrada sobre la cual se quiere calcular la suma
                     de alguna de sus diagonales. Todos los elementos de cada una de sus listas son enteros.
    Retorno:
      int: Entero con la suma acumulada sobre la diagonal solicitada de la matriz cuadrada que llega por
           parámetro.
    """
    suma = 0
    for i in range(0, len(matriz)):
        if diagonal_mayor:
            actual = matriz[i][i]
        else:
            actual = matriz[-i - 1][i]
        suma += actual
    return suma


def binarizar_imagen(imagen: list, umbral: float) -> list:
    """ Binarizar (Matriz de Listas)
    Parámetros:
      imagen (list): Matriz que representa la imagen
      umbral (float): Umbral de binarización
    Retorno:
      list: Matriz que representa la imagen binarizada
    """
    alto = len(imagen)
    ancho = len(imagen[0])
    for i in range(alto):
        for j in range(ancho):
            promedio_pixel = 0
            for k in range(3):
                promedio_pixel += imagen[i][j][k]
            promedio_pixel /= 3
            if promedio_pixel >= umbral:
                imagen[i][j] = [255, 255, 255]
            else:
                imagen[i][j] = [0, 0, 0]
    return imagen


def convertir_negativo(imagen: list) -> list:
    """ Transformar a Negativo (Matriz de Listas)
    Parámetros:
      imagen (list): Matriz que representa la imagen
    Retorno:
      list: Matriz que representa la imagen convertida a negativo
    """
    alto = len(imagen)
    ancho = len(imagen[0])
    for i in range(alto):
        for j in range(ancho):
            for k in range(3):
                nuevo = abs(imagen[i][j][k] - 1)
                imagen[i][j][k] = nuevo
    return imagen


def reflejar_imagen(imagen: list) -> list:
    """ Reflejar Verticalmente (Matriz de Listas)
    Parámetros:
      imagen (list): Matriz que representa la imagen
    Retorno:
      list: Matriz que representa la imagen reflejada
    """
    alto = len(imagen)
    ancho = len(imagen[0])
    for i in range(alto):
        for j in range(int(ancho / 2)):
            temp = imagen[i][j]
            imagen[i][j] = imagen[i][-j - 1]
            imagen[i][-j - 1] = temp
    return imagen


def convertir_a_grises(imagen: list) -> list:
    """ Escala de Grises (Matriz de Tuplas)
    Parámetros:
      imagen (list): Matriz que representa la imagen
    Retorno:
      list: Matriz que representa la imagen convertida a grises
    """
    alto = len(imagen)
    ancho = len(imagen[0])
    for i in range(alto):
        for j in range(ancho):
            promedio_pixel = 0
            for k in range(3):
                promedio_pixel += imagen[i][j][k]
            promedio_pixel /= 3
            imagen[i][j] = [promedio_pixel] * 3
    return imagen

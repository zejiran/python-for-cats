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


def encontrar_mejor_puntaje_equipo(salon: list, m: int) -> int:
    """ El Mejor Equipo
    Parámetros:
      salon (list): Una lista de listas que representa una matriz cuadrada, con el número de problemas
                    resueltos por cada estudiante.
      m (int): Número de equipos en los que el profesor divide el salón
    Retorno:
      int: Entero que representa la suma de puntajes de los integrantes del mejor equipo en el juego planteado
           por el profesor.
    """
    n = len(salon)
    primer_e = 0
    segundo_e = 0
    # Filas.
    for i in range(n):
        # Columnas.
        for j in range(n):
            if j <= (n/m) - 1:
                primer_e += salon[i][j]
            elif 2 * (n/m) - 1 >= j >= (n/m):
                segundo_e += salon[i][j]
    if primer_e > segundo_e:
        return primer_e
    else:
        return segundo_e


def calcular_multiplicacion_en_columna(matriz: list, columna: int) -> int:
    """ Multiplicación en la columna
    Parámetros:
      matriz (list): Una matriz de enteros, sobre la cual hay que calcular la suma de la columna dada por
                     parámetro.
      columna (int): Entero que indica sobre cual de las columnas hay que hacer las multiplicaciones. Es un
                     valor entre 0 y M-1, donde M es la cantidad de columnas de la matriz.
    Retorno:
      int: El valor de la multiplicación de todos los elementos que se encuentran en una columna particular de
           la matríz.
    """
    m = 1
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if columna == j:
                m *= matriz[i][j]
    return m


def promedio_fila(matriz: list, fila: int) -> float:
    """ La fila juiciosa
    Parámetros:
      matriz (list): Matriz que representa el salón de clases
      fila (int): Fila a la cual se debe calcular el promedio
    Retorno:
      float: Promedio de la fila que el profesor solicitó.
    """
    if fila <= 0:
        return -1
    else:
        fila = fila - 1
        suma = 0
        estudiantes = 0
        for j in range(len(matriz[fila])):
            if matriz[fila][j] != 0:
                suma += matriz[fila][j]
                estudiantes += 1
        promedio = suma / estudiantes
        if promedio == 0:
            return 0
        else:
            return round(promedio, 2)


def pintar_x(matriz: list, operacion: str) -> list:
    """ Repintar la X
    Parámetros:
      matriz (list): Una matriz cuadrada con números positivos
      operacion (str): Cadena con el símbolo de la operación a realizar. El símbolo puede ser '+', '-', '*'
                       o '/'
    Retorno:
      list: La matriz modificada según la operación indicada.
    """
    if operacion == '+':
        matriz[0][0] += matriz[0][0]
        matriz[0][2] += matriz[0][2]
        matriz[1][2] += matriz[1][2]
        matriz[2][0] += matriz[2][0]
        matriz[2][2] += matriz[2][2]
    elif operacion == '-':
        matriz[0][0] -= matriz[0][0]
        matriz[0][2] -= matriz[0][2]
        matriz[1][2] -= matriz[1][2]
        matriz[2][0] -= matriz[2][0]
        matriz[2][2] -= matriz[2][2]
    elif operacion == '*':
        matriz[0][0] *= matriz[0][0]
        matriz[0][2] *= matriz[0][2]
        matriz[1][2] *= matriz[1][2]
        matriz[2][0] *= matriz[2][0]
        matriz[2][2] *= matriz[2][2]
    elif operacion == '/':
        matriz[0][0] /= matriz[0][0]
        matriz[0][2] /= matriz[0][2]
        matriz[1][2] /= matriz[1][2]
        matriz[2][0] /= matriz[2][0]
        matriz[2][2] /= matriz[2][2]
    return matriz

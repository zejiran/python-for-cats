# -*- coding: utf-8 -*-
"""
Ejercicio nivel 4: Boletin Estadístico.
Módulo de funciones.

Temas:
* Recorridos de Matrices.
* Librerías de Matplotlib.

@author: zejiran
"""


def cargar_matriz_estadisticas(ruta_archivo: str) -> list:
    """
    Esta funcion carga la informacion de la matriz de estadísticas
    de las facultades a partir de un archivo CSV.
        ruta_archivo (str): la ruta del archivo que se quiere cargar
    Retorno: list
        La matriz con las estadisticas por facultad
    """
    archivo = open(ruta_archivo)
    linea = archivo.readline()
    facultades = 11
    elementos = 9
    estadisticas = list()
    for i in range(0, facultades + 1):
        estadisticas.append([0] * (elementos + 1))
    i = 0
    while len(linea) > 0:
        datos = linea.split(",")
        for j in range(0, elementos + 1):
            estadisticas[i][j] = datos[j].strip()
        i += 1
        linea = archivo.readline()
    archivo.close()
    return estadisticas


def cargar_matriz_puestos(ruta_archivo: str) -> list:
    """
    Esta funcion carga la informacion de la matriz de puestos estudiante 
    a partir de un archivo CSV.
        ruta_archivo (str): la ruta del archivo que se quiere cargar
    Retorno: list
        La matriz con los puestos estudiante de cada facultad
    """
    archivo1 = open(ruta_archivo)
    linea = archivo1.readline()
    oferentes = 11
    ocupantes = 12
    puestos = []
    for i in range(0, oferentes + 1):
        puestos.append([0] * (ocupantes + 1))
    i = 0
    while len(linea) > 0:
        datos = linea.split(",")
        for j in range(0, ocupantes + 1):
            puestos[i][j] = datos[j].strip()
        i += 1
        linea = archivo1.readline()
    archivo1.close()
    return puestos


def cargar_matriz_dobles(ruta_archivo: str) -> list:
    """
    Esta funcion carga la informacion de la matriz de dobles programas
    a partir de un archivo CSV.
        ruta_archivo (str): la ruta del archivo que se quiere cargar
    Retorno: list
        La matriz con los puestos estudiante de cada facultad
    """
    archivo2 = open(ruta_archivo)
    linea = archivo2.readline()
    programas = 35
    dobles = []
    for i in range(0, programas + 1):
        dobles.append([0] * (programas + 1))
    i = 0
    while len(linea) > 0:
        datos = linea.split(",")
        for j in range(0, programas + 1):
            dobles[i][j] = datos[j].strip()
        i += 1
        linea = archivo2.readline()
    archivo2.close()
    return dobles

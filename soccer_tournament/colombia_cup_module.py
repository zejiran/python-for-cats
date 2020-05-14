# -*- coding: utf-8 -*-
"""
Created by zejiran.
"""


def cargar_tablero_goles(ruta_archivo: str) -> list:
    """
    Esta función carga la información de un tablero de goles 
    a partir de un archivo CSV.
    La primera fila del archivo contiene la dimensión del tablero (cuadrado).
    Parámetros:
        ruta_archivo (str): la ruta del archivo que se quiere cargar.
    Retorno: list
        La matriz con el tablero de goles.
    """
    archivo = open(ruta_archivo)
    dimensiones = archivo.readline().split(",")
    filas = int(dimensiones[0])
    columnas = filas

    tablero = []
    for i in range(0, filas):
        tablero.append([0] * columnas)

    linea = archivo.readline()
    i = 0
    while len(linea) > 0:
        datos = linea.split(",")
        for j in range(0, columnas):
            tablero[i][j] = int(datos[j])
        i += 1
        linea = archivo.readline()

    archivo.close()
    return tablero


def cargar_equipos(ruta_archivo: str) -> dict:
    """
    Esta función carga la información de los equipos 
    a partir de un archivo CSV.
    Parámetros:
        ruta_archivo (str): la ruta del archivo que se quiere cargar
    Retorno: dict
        Un diccionario en el cual las llaves son los nombres de los equipos y 
        los valores son unos índices consecutivos.
    """
    archivo = open(ruta_archivo)
    equipos = {}
    linea = archivo.readline()
    while len(linea) > 0:
        datos = linea.split(",")
        equipos[datos[0]] = int(datos[1])
        linea = archivo.readline()

    archivo.close()
    return equipos


def anotar_marcador(tablero_goles: list, equipos: dict, equipo1: str, equipo2: str, marcador: str) -> list:
    """
    Esta función registra el marcador de un partido en el tablero de goles.
    Parámetros:
        tablero_goles (list): matriz que contiene el tablero de goles.
        equipos (dict): diccionario de los equipos del campeonato.
        equipo1 (string): nombre del primer equipo del partido.
        equipo2 (string): nombre del segundo equipo del partido.
        marcador (string): string con formato goles1-goles2, donde goles1 son los goles que equipo1
        marcó a equipo2 y goles2 son los goles que equipo2 marcó a equipo1.
    Retorno: list
        La matriz de goles actualizada.
    """
    pos_equipo1 = int(equipos.get(equipo1))
    pos_equipo2 = int(equipos.get(equipo2))
    marcador = marcador.split("-")
    tablero_goles[pos_equipo1][pos_equipo2] = int(marcador[0])
    tablero_goles[pos_equipo2][pos_equipo1] = int(marcador[1])
    return tablero_goles


def total_goles(tablero_goles: list) -> int:
    """
    Esta función calcula el total de goles que se han marcado en el campeonato.
    Parámetros:
        tablero_goles (list): matriz que contiene el tablero de goles.
    Retorno: int
        El total de goles de la matriz.
    """
    goles_totales = 0
    for fila in tablero_goles:
        for columna in fila:
            if columna != -1 and columna != -2:
                goles_totales += int(columna)
    return goles_totales


def partidos_jugados(tablero_goles: list) -> int:
    """
    Esta función calcula el total de partidos que se han jugado en el campeonato.
    Parámetros:
        tablero_goles (list): matriz que contiene el tablero de goles.
    Retorno: int
        El total de partidos jugados en el campeonato.
    """
    jugados = 0
    for fila in tablero_goles:
        for columna in fila:
            if columna != -1 and columna != -2:
                jugados += 0.5
    return int(jugados)


def equipo_mas_goleador(tablero_goles: list, equipos: dict) -> str:
    """
    Esta función retorna el nombre del equipo que ha marcado más goles en el
    campeonato
    Parámetros:
        tablero_goles (list): matriz que contiene el tablero de goles
        equipos (dict): diccionario de los equipos del campeonato
    Retorno: str
        El nombre del equipo más goleador del campeonato
    """
    goleador = "Ninguno"
    goles_goleador = 0
    nombre_equipos = []
    # Agregar equipos a una lista.
    for equipo in equipos:
        nombre_equipos.append(equipo)
    # Recorrido para verificar goleador.
    i = 0
    for fila in tablero_goles:
        goles_equipo = 0
        for columna in fila:
            if columna != -1 and columna != -2:
                goles_equipo += columna
        if goles_goleador < goles_equipo:
            goles_goleador = goles_equipo
            goleador = nombre_equipos[i]
        i += 1
    return goleador


def equipo_mas_goleado(tablero_goles: list, equipos: dict) -> str:
    """
    Esta función retorna el nombre del equipo al cual le han marcado más goles en el
    campeonato
    Parámetros:
        tablero_goles (list): matriz que contiene el tablero de goles
        equipos (dict): diccionario de los equipos del campeonato
    Retorno: str
        El nombre del equipo más goleado del campeonato
    """
    return "Ninguno"


def partidos_empatados(tablero_goles: list) -> int:
    """
    Esta función calcula el total de partidos que se han quedado empatados en el campeonato
    Parámetros:
        tablero_goles (list): matriz que contiene el tablero de goles
    Retorno: int
        El total de partidos empatados en el campeonato
    """
    return 0


def mayor_numero_goles(tablero_goles: list) -> int:
    """
    Esta función calcula el mayor número de goles marcados en un partido del campeonato 
    (sumando los goles de los dos equipos)

    Parámetros:
        tablero_goles (list): matriz que contiene el tablero de goles
    Retorno: int
        El mayor número de goles marcados en un partido del campeonato
    """
    return 0

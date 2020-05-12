# -*- coding: utf-8 -*-
"""
Ejercicio de examen nivel 3 - #2: Nombre de atleta que haya ganado un evento dos veces.

@author: zejiran.
"""


def obtener_doble_ganador(atletas: list) -> str:
    """
    Función en el módulo de Atletas Olímpicos, que retorna el nombre del primer atleta de la lista
     que haya participado del mismo evento en dos ediciones diferentes de los juegos olímpicos y
     haya obtenido medalla en ambas ocasiones.
    Parámetros:
        atletas: list de diccionarios de cada atleta.
    Retorno:
        doble_ganador = str nombre del atleta aplicable.
    """
    # Variables de conteo.
    i = 0
    encontrado = False
    doble_ganador = ""
    diccionario = {}
    # Inicio de recorrido por la lista de atletas.
    while i < len(atletas) and not encontrado:
        nombre = atletas[i]['nombre']
        evento = atletas[i]["evento"]
        if (nombre + evento) not in diccionario:
            diccionario[nombre + evento] = 0
        if atletas[i]['medalla'] != "na":
            diccionario[nombre + evento] += 1
        if diccionario[nombre + evento] > 1:
            encontrado = True
            doble_ganador = nombre
        i += 1
    if not encontrado:
        doble_ganador = "No hay doble ganador de eventos"
    return doble_ganador


# Test.
print(obtener_doble_ganador([{'nombre': "Juan", 'medalla': "gold", 'evento': 'hockey'},
                             {'nombre': "Valde", 'medalla': "silver", 'evento': 'hockey'},
                             {'nombre': "Valde", 'medalla': "silver", 'evento': 'hockey'},
                             {'nombre': "Juan", 'medalla': "silver", 'evento': 'hockey'},
                             {'nombre': "Juan", 'medalla': "silver", 'evento': 'hockey'}]))


# def obtener_doble_ganador(atletas: list) -> str:
#     """
#     Función en el módulo de Atletas Olímpicos, que retorna el nombre del primer atleta de la lista
#      que haya participado del mismo evento en dos ediciones diferentes de los juegos olímpicos y
#      haya obtenido medalla en ambas ocasiones.
#     Parámetros:
#         atletas: list de diccionarios de cada atleta.
#     Retorno:
#         doble_ganador = str nombre del atleta aplicable.
#     """
#     # Variables de conteo.
#     i = 0
#     encontrado = False
#     doble_ganador = ""
#     # Inicio de recorrido por la lista de atletas.
#     while i < len(atletas) and not encontrado:
#         atletas[i]['eventos_ganados'] = {}
#         if atletas[i]['medalla'] != "na":
#             medallas_evento = atletas[i]['eventos_ganados'].get(atletas[i]["evento"], 0)
#             atletas[i]['eventos_ganados'][atletas[i]["evento"]] = medallas_evento + 1
#             medallas_evento = atletas[i]['eventos_ganados'].get(atletas[i]["evento"], 0)
#             if medallas_evento > 1:
#                 encontrado = True
#                 doble_ganador = atletas[i]['nombre']
#         i += 1
#     if not encontrado:
#         doble_ganador = "No hay doble ganador de eventos"
#     return doble_ganador

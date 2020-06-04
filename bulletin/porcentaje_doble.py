# -*- coding: utf-8 -*-
"""
@author: zejiran

Se desea extender el proyecto realizado sobre el boletín estadístico de la Universidad.
Ahora se quiere incluir una función que permita conocer el porcentaje de estudiantes de
una Facultad que realizan doble programa (puede ser con cualquier otro pregrado de la Universidad).
Esta función debe recibir como parámetros el nombre de la Facultad de interés, la matriz de estadísticas,
la matriz de dobles programas y una lista con los nombres de los programas que pertenecen a la Facultad de interés.
El resultado debe retornarse con dos decimales.
"""


def porcentaje_estudiantes_doble_en_facultad(facultad: str, matriz_estadisticas: list, matriz_dobles: list,
                                             dobles_facultad: list) -> float:
    """
    Función que permite conocer el porcentaje de estudiantes de una Facultad que realizan doble programa.

    :param facultad: nombre de la Facultad de interés.
    :param matriz_estadisticas: matriz de estadísticas.
    :param matriz_dobles: matriz de dobles programas.
    :param dobles_facultad: lista con los nombres de los programas que pertenecen a la Facultad de interés.
    :return: porcentaje redondeado a dos decimales.

    :type facultad: str.
    :type matriz_estadisticas: list.
    :type matriz_dobles: list.
    :type dobles_facultad: list.
    :rtype: float.
    """
    estudiantes_dobles = 0
    total_estudiantes = 0
    # Inicio de recorrido por filas.
    for i in range(1, len(matriz_dobles)):
        # Se verifica que estemos en la fila de la facultad de interés.
        if matriz_dobles[i][0].lower() == facultad.lower():
            # Inicio de recorrido por columnas.
            for j in range(1, len(matriz_dobles[0])):
                # Inicio de recorrido por dobles programas de la facultad.
                for k in dobles_facultad:
                    # Se verifica que la columna actual sea de un doble programa.
                    if matriz_dobles[0][j] == k:
                        estudiantes_dobles += int(matriz_dobles[i][j])
    # Se realizará el conteo del total de estudiantes en la facultad.
    for fila in range(1, len(matriz_estadisticas)):
        for columna in range(1, len(matriz_estadisticas[0])):
            if matriz_estadisticas[0][columna] == "Estudiantes hombres":
                hombres = matriz_estadisticas[fila][columna]
                mujeres = matriz_estadisticas[fila][columna + 1]
                total_estudiantes += hombres + mujeres
    # Se calcula el porcentaje de estudiantes en doble programa.
    porcentaje_doble = float(estudiantes_dobles / total_estudiantes)
    # Retorno redondeado y en porcentaje (0,100).
    return round(porcentaje_doble, 2) * 100

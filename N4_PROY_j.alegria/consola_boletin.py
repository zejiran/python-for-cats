# -*- coding: utf-8 -*-
"""
Ejercicio nivel 4: Boletín Estadístico.
Consola.

Temas:
* Recorridos de Matrices.
* Librerías de Matplotlib.

@author: zejiran
"""

import boletin as be


def mostrar_menu() -> None:
    """Imprime las opciones de ejecucion disponibles para el usuario."""
    print("\nOpciones")
    print("1. Cargar archivos.")
    print("2. Consultar puestos estudiante atendidos por una facultad.")
    print("3. Consultar puestos estudiante ocupados por una facultad.")
    print("4. Consultar la facultad mas servicial.")
    print("5. Consultar si existe una facultad generosa.")
    print("6. Calcular el porcentaje de autocubrimiento.")
    print("7. Consultar el doble progama mas popular.")
    print("8. Consultar todos los dobles programas de un programa.")
    print("9. Consultar las estadisticas del PGA.")
    print("10. Consultar si hay una facultad con mas de x% de estudiantes de un genero.")
    print("11. Salir de la aplicacion.")


def ejecutar_cargar_matriz_estadisticas() -> list:
    """Solicita al usuario que ingrese el nombre de un archivo CSV con los datos de
    la matriz de estadisticas de facultades y la carga.
    Retorno: list
        La matriz de estadisticas de las facultades.
    """
    archivo = input("Por favor ingrese el nombre del archivo CSV con la matriz de estadísticas: ")
    estadisticas = be.cargar_matriz_estadisticas(archivo)
    if len(estadisticas) == 0:
        print("El archivo seleccionado no es valido. No se pudo cargar la matriz de estadisticas.")
    else:
        print("Se cargó la matriz de estadisticas.", estadisticas)
    return estadisticas


def ejecutar_cargar_matriz_puestos() -> list:
    """Solicita al usuario que ingrese el nombre de un archivo CSV con los datos de
    la matriz de los puestos estudiante y la carga.
    Retorno: list
        La matriz de los puestos estudiante.
    """
    archivo = input("Por favor ingrese el nombre del archivo CSV con la matriz de puestos estudiante: ")
    puestos = be.cargar_matriz_puestos(archivo)
    if len(puestos) == 0:
        print("El archivo seleccionado no es valido. No se pudo cargar la matriz de puestos estudiante.")
    else:
        print("Se cargo la matriz de puestos estudiante.", puestos)
    return puestos


def ejecutar_cargar_matriz_dobles() -> list:
    """Solicita al usuario que ingrese el nombre de un archivo CSV con los datos de
    la matriz de dobles programas y la carga.
    Retorno: list
        La matriz de los dobles programas entre las carreras.
    """
    archivo = input("Por favor ingrese el nombre del archivo CSV con la matriz de dobles programas: ")
    dobles = be.cargar_matriz_dobles(archivo)
    if len(dobles) == 0:
        print("El archivo seleccionado no es valido. No se pudo cargar la matriz de dobles programas.")
    else:
        print("Se cargo la matriz de dobles programas.", dobles)
    return dobles


def ejecutar_puestos_atendidos(puestos: list) -> None:
    """ Ejecuta la opcion de consultar los puestos estudiantes atendidos
    por una facultad en especifico.
    """
    facultad = input("Ingrese la facultad de su interes: ")
    puestos_facultad = be.puestos_atendidos(puestos, facultad)
    print("En la facultad de", facultad, "atiende un total de", puestos_facultad, "estudiantes.\n")


def ejecutar_puestos_ocupados(puestos: list) -> None:
    """ Ejecuta la opcion de consultar los puestos estudiantes ocupados
    por una facultad en especifico
    """
    facultad = input("Ingrese la facultad de su interes: ")

    # TODO: complete el codigo haciendo el llamado a la funcion del modulo que
    # implementa este requerimiento e imprimiendo por pantalla el resultado


def ejecutar_facultad_mas_servicial(puestos: list) -> None:
    """ Ejecuta la opcion de consultar la facultad mas servicial
    """

    # TODO: complete el codigo haciendo el llamado a la funcion del modulo que
    # implementa este requerimiento e imprimiendo por pantalla el resultado


def ejecutar_hay_facultad_generosa(puestos: list) -> None:
    """ Ejecuta la opcion de consultar si existe una facultad generosa
    para una facultad en especifico
    """

    facultad = input("Ingrese la facultad de su interes: ")
    porcentaje = float(input("Ingrese el porcentaje de su interes: "))

    # TODO: complete el codigo haciendo el llamado a la funcion del modulo que
    # implementa este requerimiento e imprimiendo por pantalla el resultado


def ejecutar_calcular_autocubrimiento(puestos: list, estadisticas: list) -> None:
    """ Ejecuta la opcion de calcular el autocubrimiento para todas
    las facultades
    """

    # TODO: complete el codigo haciendo el llamado a la funcion del modulo que
    # implementa este requerimiento e imprimiendo por pantalla el resultado
    # Le sugerimos solo imprimir la informacion de ultima columna de la
    # matriz de respuesta pues es la que contiene la informacion calculada.


def ejecutar_doble_mas_comun(dobles: list) -> None:
    """ Ejecuta la opcion de consultar el doble programa mas comun
    """

    # TODO: complete el codigo haciendo el llamado a la funcion del modulo que
    # implementa este requerimiento e imprimiendo por pantalla el resultado


def ejecutar_dobles_de_un_programa(dobles: list) -> None:
    """ Ejecuta la opcion de consultar todos los dobles programas
    de una facultad de su interes
    """
    programa = input("Ingrese el programa de su interes: ")

    # TODO: complete el codigo haciendo el llamado a la funcion del modulo que
    # implementa este requerimiento e imprimiendo por pantalla el resultado


def ejecutar_estadisticas_pga(estadisticas: list):
    """ Ejecuta la opcion de consultar la facultad con mayor pga, con
    menor pga y la que ocupa la mediana
    """

    # TODO: complete el codigo haciendo el llamado a la funcion del modulo que
    # implementa este requerimiento e imprimiendo por pantalla el resultado


def ejecutar_hay_facultad_con_porcentaje_estudiantes(estadisticas: list):
    """ Ejecuta la opcion de consultar si existe una facultad con un 
    porcentaje de estudiantes por genero mayor al requerido
    """
    genero = input("Ingrese el genero de su interes (m o f): ")
    porcentaje = float(input("Ingrese el porcentaje de su interes: "))

    # TODO: complete el codigo haciendo el llamado a la funcion del modulo que
    # implementa este requerimiento e imprimiendo por pantalla el resultado


def iniciar_aplicacion():
    """Ejecuta el programa para el usuario."""
    continuar = True
    dobles = list()
    estadisticas = list()
    puestos = list()
    while continuar:
        mostrar_menu()
        opcion_seleccionada = input("Por favor seleccione una opcion: ")
        if opcion_seleccionada == "1":
            dobles = ejecutar_cargar_matriz_dobles()
            estadisticas = ejecutar_cargar_matriz_estadisticas()
            puestos = ejecutar_cargar_matriz_puestos()
        elif opcion_seleccionada == "2":
            ejecutar_puestos_atendidos(puestos)
        elif opcion_seleccionada == "3":
            ejecutar_puestos_ocupados(puestos)
        elif opcion_seleccionada == "4":
            ejecutar_facultad_mas_servicial(puestos)
        elif opcion_seleccionada == "5":
            ejecutar_hay_facultad_generosa(puestos)
        elif opcion_seleccionada == "6":
            ejecutar_calcular_autocubrimiento(puestos, estadisticas)
        elif opcion_seleccionada == "7":
            ejecutar_doble_mas_comun(dobles)
        elif opcion_seleccionada == "8":
            ejecutar_dobles_de_un_programa(dobles)
        elif opcion_seleccionada == "9":
            ejecutar_estadisticas_pga(estadisticas)
        elif opcion_seleccionada == "10":
            ejecutar_hay_facultad_con_porcentaje_estudiantes(estadisticas)
        elif opcion_seleccionada == "11":
            continuar = False
        else:
            print("Por favor seleccione una opcion valida.")


# PROGRAMA PRINCIPAL
iniciar_aplicacion()

# -*- coding: utf-8 -*-
"""
Ejercicio nivel 3: Atletas Olímpicos.
Interfaz basada en consola para la interacción con el usuario.

Temas:
* Instrucciones repetitivas.
* Listas
* Diccionarios
* Archivos

@author: zejiran.
"""

import olympics_module as olim


def ejecutar_cargar_atletas() -> list:
    """
    Solicita al usuario que ingrese el nombre de un archivo CSV con los datos de
    los atletas y los carga.
    Retorno: list
        La lista de atletas con la información del archivo.
    """
    archivo = input("Por favor ingrese el nombre del archivo CSV con los atletas: ")
    atletas = olim.cargar_atletas(archivo)
    if len(atletas) == 0:
        print("El archivo seleccionado no es válido. No se pudieron cargar los atletas olímpicos.")
        atletas = None
    else:
        print("Se cargaron", len(atletas), "atletas a partir del archivo.")
    print(atletas)
    return atletas


def ejecutar_atletas_por_anio(atletas: list) -> None:
    # Ejecuta la opción de buscar los atletas de un año dado.
    anio = int(input("Ingrese el año de su interés: "))
    eventos_anio = olim.obtener_atletas_de_anio(atletas, anio)
    print("\nEventos y sus atletas en el año", anio, ":\n")
    print("-----------------------------------------------------" + "\n")
    for cada_evento in eventos_anio.keys():
        print(cada_evento + " - atletas: " + str(eventos_anio[cada_evento]) + "\n")
        print("-----------------------------------------------------" + "\n")


def ejecutar_medallas_en_rango(atletas: list) -> None:
    # Ejecuta la opción de buscar las medallas de un atleta en un rango específico de años.
    nombre = input("Ingrese el nombre del atleta de su interés: ")
    aniomenor = int(input("Ingrese el límite inferior del rango: "))
    aniomayor = int(input("Ingrese el límite superior del rango: "))
    medallas_atleta = olim.obtener_medallas_de_atleta(atletas, aniomenor, aniomayor, nombre)
    if medallas_atleta:
        print("\nMedallas de", nombre, "desde", aniomenor, "a", aniomayor, ":\n")
        print("-----------------------------------------------------" + "\n")
        for cada_medalla in medallas_atleta:
            print("Evento:", cada_medalla['evento'], "\n")
            print("Año:", cada_medalla['anio'], "\n")
            print("Medalla:", cada_medalla['medalla'] + "\n")
            print("-----------------------------------------------------" + "\n")
    else:
        print("No hay medallas para ese atleta")


def ejecutar_atletas_por_pais(atletas: list) -> None:
    # Ejecuta la opción de buscar los atletas de un país específico.
    pais = input("Ingrese el nombre del país de su interés: ")
    atletas_pais = olim.obtener_atletas_pais(atletas, pais)
    print("\nAtletas de", pais, ":\n")
    print("-----------------------------------------------------" + "\n")
    for cada_atleta in atletas_pais:
        print("Nombre:", cada_atleta['nombre'], "\n")
        print("Evento:", cada_atleta['evento'], "\n")
        print("Año:", cada_atleta['anio'], "\n")
        print("-----------------------------------------------------" + "\n")


def ejecutar_pais_con_mas_atletas(atletas: list) -> None:
    # Ejecuta la opción de buscar el país con más atletas.
    pais_atletico = olim.encontrar_pais_medallista(atletas)
    print("-----------------------------------------------------" + "\n")
    print(list(pais_atletico.keys())[0],
          "es el país con la mayor cantidad de medallistas en todos los tiempos de los juegos olímpicos.", "\n")
    print("Cantidad de medallistas:", pais_atletico[list(pais_atletico.keys())[0]], "\n")
    print("-----------------------------------------------------" + "\n")


def ejecutar_medallistas_por_evento(atletas: list) -> None:
    # Ejecuta la opción de buscar los medallistas de un evento dado.
    evento = input("Ingrese el evento de su interés: ")
    medallistas = olim.obtener_ganadores_de_evento(atletas, evento)
    print("-----------------------------------------------------" + "\n")
    for cada_medallista in medallistas:
        print("Medallista:", cada_medallista, "\n")
        print("-----------------------------------------------------" + "\n")


def ejecutar_atletas_con_mas_medallas_que(atletas: list) -> None:
    # Ejecuta la opción de buscar los atletas que han obtenido una cantidad de medallas superior a un número dado.
    limite = int(input("Ingrese el mínimo de medallas: "))
    sobrepasa_limite = olim.obtener_atletas_medallas_superiores_a_numero(atletas, limite)
    if sobrepasa_limite != {}:
        print("-----------------------------------------------------" + "\n")
        for cada_atleta in sobrepasa_limite:
            print("Atleta:", cada_atleta, "\n")
            print("Cantidad de medallas ganadas:", sobrepasa_limite[cada_atleta], "\n")
            print("-----------------------------------------------------" + "\n")
    else:
        print("Ningún atleta tiene tantas medallas.")


def ejecutar_atleta_estrella(atletas: list) -> None:
    # Ejecuta la opción de buscar el atleta con más medallas de todos los tiempos.
    estrellas = olim.encontrar_atletas_estrella(atletas)
    print("-----------------------------------------------------" + "\n")
    for cada_atleta in estrellas:
        print("Atleta estrella:", cada_atleta, "\n")
        print("Cantidad de medallas ganadas:", estrellas[cada_atleta], "\n")
        print("-----------------------------------------------------" + "\n")


def ejecutar_mejor_pais_en_un_evento(atletas: list) -> None:
    # Ejecuta la opción de buscar el país con mejor desempeño en un evento en específico.
    evento = input("Ingrese el evento de su interés: ")
    destacado = olim.encontrar_pais_destacado_en_evento(atletas, evento)
    print("-----------------------------------------------------" + "\n")
    for cada_pais in destacado:
        print("País destacado en", evento, cada_pais, "\n")
        print("Cantidad de medallas de oro ganadas:", destacado[cada_pais][0], "\n")
        print("Cantidad de medallas de plata ganadas:", destacado[cada_pais][1], "\n")
        print("Cantidad de medallas de bronce ganadas:", destacado[cada_pais][2], "\n")
        print("-----------------------------------------------------" + "\n")


def ejecutar_todoterreno(atletas: list) -> None:
    # Ejecuta la opción de buscar el atleta más todoterreno de todos los tiempos.
    todoterreno = olim.encontrar_todoterreno(atletas)
    print(todoterreno, "es el atleta todoterreno, aquel que ha participado en más eventos diferentes.")


def ejecutar_medallistas_por_nacion_y_genero(atletas: list) -> None:
    # Ejecuta la opción de buscar los medallistas de un país y género específicos.
    pais = input("Ingrese el país de su interés: ")
    genero = input("Ingrese el género de su interés (m o f): ")
    medallistas = olim.obtener_medallistas_por_genero_pais(atletas, pais, genero)
    print("Hay", len(medallistas), "atletas de", pais, "y género", genero, "\n")
    print("-----------------------------------------------------" + "\n")
    for cada_medallista in medallistas:
        print(cada_medallista, "\n")
        for cada_evento in medallistas[cada_medallista]:
            print("--> ")
            print("Evento:", cada_evento['evento'], "\n")
            print("Año:", cada_evento['anio'], "\n")
            print("Medalla:", cada_evento['medalla'] + "\n")
        print("-----------------------------------------------------" + "\n")


def ejecutar_porcentaje_medallistas(atletas: list) -> None:
    # Ejecuta la opción de calcular el porcentaje de medallistas.
    porcentaje = str(olim.calcular_porcentaje_ganador(atletas) * 100) + "%"
    print("El porcentaje de atletas que ganan medallas es", porcentaje, "\n")


def mostrar_menu() -> None:
    # Imprime las opciones de ejecución disponibles para el usuario.
    print("\nOpciones")
    print("1. Cargar un archivo de atletas")
    print("2. Consultar los atletas de un año dado")
    print("3. Consultar las medallas de un atleta en un periodo")
    print("4. Consultar los atletas de un país dado")
    print("5. Consultar el país con más medallistas")
    print("6. Consultar todos los medallistas de un evento dado")
    print("7. Consultar los atletas más populares")
    print("8. Consultar el atleta estrella de todos los tiempos")
    print("9. Consultar el mejor país en un evento")
    print("10. Consultar el atleta Todoterreno")
    print("11. Consultar los medallistas por nación y género")
    print("12. Consultar el porcentaje de atletas que son medallistas")
    print("13. Salir de la aplicación")


def iniciar_aplicacion() -> None:
    # Ejecuta el programa para el usuario.
    continuar = True
    atletas = list()
    while continuar:
        mostrar_menu()
        opcion_seleccionada = int(input("\nPor favor seleccione una opción: "))
        if opcion_seleccionada == 1:
            atletas = ejecutar_cargar_atletas()
        elif opcion_seleccionada == 2:
            ejecutar_atletas_por_anio(atletas)
        elif opcion_seleccionada == 3:
            ejecutar_medallas_en_rango(atletas)
        elif opcion_seleccionada == 4:
            ejecutar_atletas_por_pais(atletas)
        elif opcion_seleccionada == 5:
            ejecutar_pais_con_mas_atletas(atletas)
        elif opcion_seleccionada == 6:
            ejecutar_medallistas_por_evento(atletas)
        elif opcion_seleccionada == 7:
            ejecutar_atletas_con_mas_medallas_que(atletas)
        elif opcion_seleccionada == 8:
            ejecutar_atleta_estrella(atletas)
        elif opcion_seleccionada == 9:
            ejecutar_mejor_pais_en_un_evento(atletas)
        elif opcion_seleccionada == 10:
            ejecutar_todoterreno(atletas)
        elif opcion_seleccionada == 11:
            ejecutar_medallistas_por_nacion_y_genero(atletas)
        elif opcion_seleccionada == 12:
            ejecutar_porcentaje_medallistas(atletas)
        elif opcion_seleccionada == 13:
            continuar = False
        else:
            print("Por favor seleccione una opción válida.")


# PROGRAMA PRINCIPAL
iniciar_aplicacion()

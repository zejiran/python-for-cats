# -*- coding: utf-8 -*-
"""
@author: alxus27
"""

import math


def letra_mas_comun(cadena: str) -> str:
    """ Letra
    Parámetros:
      cadena (str): La cadena en la que se quiere saber cuál es la letra más común
    Retorno:
      str: La letra más común en la cadena que ingresa como parámetro,  si son dos es la letra alfabéticamente
           posterior.
    """
    letras_en_conteo = {}
    mayor_conteo = 0
    letra_moda = ""
    for cada_caracter in cadena:
        if cada_caracter != " " and cada_caracter != "," and cada_caracter != ".":
            # Conteo de cada caracter n
            if cada_caracter not in letras_en_conteo:
                letras_en_conteo[cada_caracter] = 1
            else:
                letras_en_conteo[cada_caracter] += 1
            # Verificación del mayor carácter contado
            if letras_en_conteo[cada_caracter] == mayor_conteo:
                if cada_caracter > letra_moda:
                    letra_moda = cada_caracter
            elif letras_en_conteo[cada_caracter] > mayor_conteo:
                mayor_conteo = letras_en_conteo[cada_caracter]
                letra_moda = cada_caracter
    print(letras_en_conteo)
    print(letra_moda)
    return letra_moda


def contar_caracteres_repetidos(cadena: str) -> int:
    """ Caracteres Repetidos
    Parámetros:
      cadena (str): La cadena que se debe revisar.
    Retorno:
      int: La cantidad de caracteres diferentes que aparecen repetidos en la cadena.
    """
    caracteres_cadena = {}
    diferentes_repetidos = 0
    for caracter in cadena:
        # Conteo de cada caracter.
        if caracter not in caracteres_cadena:
            caracteres_cadena[caracter] = 1
        else:
            caracteres_cadena[caracter] += 1
        # Verificación de repetición mayor a una vez.
        if caracteres_cadena[caracter] == 2:
            diferentes_repetidos += 1
    return diferentes_repetidos


def es_primo(numero: int) -> bool:
    """ Encontrar si un número es primo
    Parámetros:
      numero (int): Entero que se busca ver si es primo
    Retorno:
      bool: Booleano que indica si el número entero recibido por parámetro es primo
    """
    primo = True
    for i in range(2, numero):
        if numero % i == 0:
            primo = False
    return primo


def invicto_mas_largo(goles_diccionarios: list, goles_adversario: list) -> int:
    """ Invictos
    Parámetros:
      goles_diccionarios (list): Los goles anotados por Diccionarios F.C en cada una de las fechas. Se
                                 garantiza que cada elemento de la lista es un entero no negativo.
      goles_adversario (list): Los goles anotados por los adversarios de Diccionarios F.C en cada una de las
                               fechas. Se garantiza que cada elemento de la lista es un entero no negativo.
    Retorno:
      int: Retorna la cantidad máxima de fechas consecutivas en que el equipo Diccionarios F.C no perdió
           durante la temporada anterior.
    """
    consecutivos_mayor = 0
    i = 0
    consecutivos = 0
    while i < len(goles_diccionarios):
        if goles_diccionarios[i] >= goles_adversario[i]:
            consecutivos += 1
            if consecutivos > consecutivos_mayor:
                consecutivos_mayor = consecutivos
        else:
            consecutivos = 0
        i += 1
    return consecutivos_mayor


def seno(x: float) -> float:
    """ Cálculo del Seno
    Parámetros:
      x (float): Número al cuál se le debe calcular el seno
    Retorno:
      float: Seno de x calculado con 5 cifras de redondeo
    """
    sen = 0
    for n in range(0, 5):
        sen = sen + ((((-1) ** n) / math.factorial(2 * n + 1)) * x ** (2 * n + 1))
    return round(sen, 5)


def traducir_a_pig_latin(texto: str) -> str:
    """ Pig Latin
    Parámetros:
      texto (str): Texto (cadena de caracteres) a traducir al Pig Latin. Consiste solamente de palabras en
                   minúscula, separadas por espacios.
    Retorno:
      str: Texto con las palabras de la cadena original traducidas a Pig Latin, separadas por espacios.
    """
    i = 0
    texto = texto.split()
    while i < len(texto):
        sin_stop = True
        if 'a' in texto[i] or 'e' in texto[i] or 'i' in texto[i] or 'o' in texto[i] or 'u' in texto[i]:
            if texto[i][0] == 'a' or texto[i][0] == 'e' or \
                    texto[i][0] == 'i' or texto[i][0] == 'o' or texto[i][0] == 'u':
                texto[i] += "way"
            else:
                final = ""
                for caracter in texto[i]:
                    if 'a' == caracter or 'e' == caracter or 'i' == caracter or 'o' == caracter or 'u' == caracter:
                        sin_stop = False
                    elif sin_stop:
                        texto[i] = texto[i][1:]
                        final += caracter
                texto[i] += final + "ay"
        i += 1
    return " ".join(texto)


def promedio_lista(numeros: list) -> float:
    suma = 0
    cantidad_positivos = 0
    for num in numeros:
        if num > 0:
            suma += num
            cantidad_positivos += 1
    promedio = suma / cantidad_positivos
    return promedio


def mediana_lista(numeros: list) -> float:
    # Orden de n￿úmeros y posici￿ón de elementos.
    numeros.sort()
    posiciones = len(numeros)
    central = int(posiciones / 2)
    # Definir mediana.
    if posiciones % 2 == 0:
        mediana = (numeros[central] + numeros[central - 1]) / 2
    else:
        mediana = numeros[central]
    return mediana


def menor_posicion_lista(numeros: list) -> int:
    posicion_menor_numero = numeros[0]
    for numero in numeros:
        if numero < posicion_menor_numero:
            posicion_menor_numero = numero
    return numeros.index(posicion_menor_numero)


def buscar_numero(numeros: list, numero: int) -> int:
    if numero in numeros:
        return numeros.index(numero)
    else:
        return -1


def homonimia(nombres: list) -> bool:
    i = 0
    homonimo = False
    while i < len(nombres) and not homonimo:
        j = i + 1
        while j < len(nombres) and not homonimo:
            if nombres[j] == nombres[i]:
                homonimo = True
            j += 1
        i += 1
    return homonimo


def escala_musical(notas: list) -> str:
    """ Escalas musicales
    Parámetros:
      notas (list): Lista de enteros que representan notas musicales en Hertz
    Retorno:
      str: Mensaje que indique si encontró notas similares: "No hay coincidencia", "Hay una nota idéntica" o
           "Hay una nota en otra escala". En caso que haya idénticas y en otra escala, primará retornar el
           mensaje que informe sobre la idéntica.
    """
    coincidencia = 0
    misma_escala = False
    nota = 0
    while nota < len(notas) and not misma_escala:
        nota_a_comparar = nota + 1
        while nota_a_comparar < len(notas) and not misma_escala:
            if notas[nota] == notas[nota_a_comparar]:
                coincidencia += 1
                misma_escala = True
            elif notas[nota_a_comparar] % notas[nota] == 0 or notas[nota] % notas[nota_a_comparar] == 0:
                coincidencia += 1
            nota_a_comparar += 1
        nota += 1
    if coincidencia >= 1 and misma_escala:
        coincidencia = "Hay una nota idéntica"
    elif coincidencia >= 1:
        coincidencia = "Hay una nota en otra escala"
    else:
        coincidencia = "No hay coincidencia"
    return coincidencia


def vuelos_mas2horas(vuelos: dict) -> None:
    archivo_mas2horas = open("mas2horas.txt", "w")
    archivo_mas2horas.write("Vuelos que duran más de dos horas\n")
    archivo_mas2horas.write("---------------------------------\n")
    for vuelo in vuelos.keys():
        if vuelos[vuelo]['duracion'] > 120:
            archivo_mas2horas.write(vuelos[vuelo]['codigo'])
            archivo_mas2horas.write(" - ")
            archivo_mas2horas.write(vuelos[vuelo]['origen'])
            archivo_mas2horas.write(" - ")
            archivo_mas2horas.write(vuelos[vuelo]['destino'])
            archivo_mas2horas.write("\n")
    archivo_mas2horas.close()


def insertar_cadena_ordenada(lista_ordenada: list, cadena_insertar: str) -> None:
    i = 0
    while i < len(lista_ordenada) and lista_ordenada[i] <= cadena_insertar:
        i += 1
    lista_ordenada.insert(i, cadena_insertar)


def addsecuencia_strings() -> list:
    lista = []
    string = input('Cadena a insertar: ')
    while string != "terminar":
        insertar_cadena_ordenada(lista, string)
        string = input('Cadena a insertar: ')
    return lista


def ordenar_secuencia(lista_desordenada: list) -> list:
    nueva_lista = []
    for cadena in lista_desordenada:
        insertar_cadena_ordenada(nueva_lista, cadena)
    return nueva_lista


def frase_intercalada(string1: str, string2: str) -> str:
    palabras1 = string1.split()
    palabras2 = string2.split()
    intercalada = []
    i = 0
    while i < len(palabras1):
        intercalada.append(palabras1[i])
        intercalada.append(palabras2[i])
        i += 1
    intercalada = " ".join(intercalada)
    return intercalada


def horas_llegada(vuelos: list):
    vuelos_llegada = list()
    for vuelo in vuelos:
        segundos_llegada = vuelo['segundos_partida'] + vuelo['segundos_duracion']
        minutos_llegada = vuelo['minutos_partida'] + vuelo['horas_duracion']
        hora_llegada = vuelo['horas_partida'] + vuelo['horas_duracion']
        while segundos_llegada >= 60:
            minutos_llegada += 1
            segundos_llegada -= 60
        while minutos_llegada >= 60:
            hora_llegada += 1
            minutos_llegada -= 60
        while hora_llegada > 24:
            hora_llegada -= 24
        vuelos_llegada.append({'HHllegada': hora_llegada, 'MMllegada': minutos_llegada,
                               'SSllegada': segundos_llegada})
    return vuelos_llegada


def vuelos_en_aeropuerto(codigo_aeropuerto: str, vuelos: dict) -> list:
    codigo_vuelos = list()
    for vuelo in vuelos.keys():
        if vuelos[vuelo]['origen'] == codigo_aeropuerto:
            codigo_vuelos.append(vuelo)
    return codigo_vuelos


def buscar_vuelo(codigo_vuelo: str, vuelos: dict) -> dict:
    dict_vuelos = {}
    no_encontro = True
    for vuelo in vuelos:
        if vuelo == codigo_vuelo:
            dict_vuelos = vuelos[vuelo]
            no_encontro = False
    if not no_encontro:
        pass
    return dict_vuelos


def vuelo_mas_largo(codigo_aerolinea: str, vuelos: dict) -> str:
    mayor_duracion = 0
    mas_largo = ''
    for codigo_vuelo in vuelos:
        if vuelos[codigo_vuelo]['aerolinea'] == codigo_aerolinea:
            if vuelos[codigo_vuelo]['duracion'] > mayor_duracion:
                mayor_duracion = vuelos[codigo_vuelo]['duracion']
                mas_largo = codigo_vuelo
    return mas_largo


def vuelos_a_destino(vuelos: dict, origen: str, destino: str) -> list:
    lista = []
    if vuelos != {}:
        # Vuelos directos.
        for codigo_vuelo in vuelos:
            if vuelos[codigo_vuelo]['origen'] == origen and vuelos[codigo_vuelo]['destino'] == destino:
                lista.append(codigo_vuelo)
        # Vuelos con una escala
        codigos_origen = []
        codigos_destino = []
        for codigo_vuelo in vuelos:
            diccionario = vuelos[codigo_vuelo]
            if diccionario['origen'] == origen and diccionario['destino'] != destino:
                codigos_origen.append(codigo_vuelo)
            if diccionario['destino'] == destino and diccionario['origen'] != origen:
                codigos_destino.append(codigo_vuelo)
        for codigoX in codigos_destino:
            for codigoY in codigos_origen:
                if vuelos[codigoX]['origen'] == vuelos[codigoY]['destino']:
                    lista.append([codigoY, codigoX])
    return lista

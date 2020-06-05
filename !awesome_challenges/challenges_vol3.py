# -*- coding: utf-8 -*-
"""
@author: zejiran.
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


def aeropuerto_mas_visitado(vuelos: dict) -> str:
    aero_mas_visitado = None
    mas_visitas = 0
    conteo_visitas = {}
    for cada_vuelo in vuelos:
        origen = vuelos[cada_vuelo]['origen']
        destino = vuelos[cada_vuelo]['destino']
        veces_origen = conteo_visitas.get(origen, 0)
        veces_destino = conteo_visitas.get(destino, 0)
        conteo_visitas[destino] = veces_destino + 1
        conteo_visitas[origen] = veces_origen + 1
        if conteo_visitas[destino] > mas_visitas:
            mas_visitas = conteo_visitas[destino]
            aero_mas_visitado = destino
        if conteo_visitas[origen] > mas_visitas:
            mas_visitas = conteo_visitas[origen]
            aero_mas_visitado = origen
    return aero_mas_visitado


def vuelos_tarde(vuelos: dict) -> None:
    # Retorna codigo-vuelo, origen, destino, y hora salida de vuelos por la tarde
    codigos_tarde = list()
    reporte = open("reporte.txt", "w")
    # Se añaden a una lista los códigos de vuelos por la tarde
    for cada_vuelo in vuelos:
        if vuelos[cada_vuelo]['salida'] > 1200:
            codigos_tarde.append(cada_vuelo)
    # Se escribe el reporte a partir de la lista
    reporte.write("Vuelos de la tarde\n")
    reporte.write("----------------------------------------\n")
    for cada_codigo in codigos_tarde:
        reporte.write("Código de vuelo: " + vuelos[cada_codigo])
        reporte.write("Origen de vuelo: " + vuelos[cada_codigo]['origen'])
        reporte.write("Destino de vuelo: " + vuelos[cada_codigo]['destino'])
        reporte.write("Hora de salida: " + str(vuelos[cada_codigo]['salida']))
    reporte.write("----------------------------------------\n")
    reporte.close()


def encontrar_mayor(entrada: list) -> int:
    """ Encontrar el elemento mayor
    Parámetros:
      entrada (list): La lista de números que se desea buscar
    Retorno:
      int: El número más grande en la lista, si está vacía -1.
    """
    mayor = -1
    for numero in entrada:
        if numero > mayor:
            mayor = numero
    return mayor


def encontrar_menor(entrada: list) -> int:
    """ Encontrar el elemento menor
    Parámetros:
      entrada (list): La lista
    Retorno:
      int: El número más pequeño en la lista, si es vacía None.
    """
    menor = None
    if entrada:
        menor = max(entrada)
        for numero in entrada:
            if numero < menor:
                menor = numero
    return menor


def buscar_elemento(entrada: list, buscado: int) -> int:
    """ Buscar un elemento en una lista
    Parámetros:
      entrada (list): Lista en la que se debe buscar el número
      buscado (int): Número entero a buscar
    Retorno:
      int: Número que indica el índice en que se encuentra el elemento buscado. Si no está, retorna -1.
    """
    i = 0
    encontrado = -1
    se_encontro = False
    while i < len(entrada) and not se_encontro:
        if buscado == entrada[i]:
            encontrado = i
            se_encontro = True
        i += 1
    return encontrado


def separar_por_edad(animales: dict, minimo: int, maximo: int) -> list:
    """ Adopción Canina
    Parámetros:
      animales (dict): Diccionario cuyas llaves son los nombres de las mascotas y sus valores la edad de
                       cada una
      minimo (int): Edad mínima de los animales para esta habitación
      maximo (int): Edad máxima de los animales para esta habitacion
    Retorno:
      list: Lista de str con los nombres de los animales para la habitación
    """
    seleccionados = []
    if animales:
        for animal in animales:
            if minimo <= animales[animal] < maximo:
                seleccionados.append(animal)
    seleccionados.sort()
    return seleccionados


def encontrar_primer_par(numeros: list) -> int:
    """ Primer par
    Parámetros:
      numeros (list): La lista de números a revisar
    Retorno:
      int: El primer número par en la lista. Si en la lista no hay números pares, se debe retornar None
    """
    es_par = False
    i = 0
    par = None
    while i < len(numeros) and not es_par:
        numero = numeros[i]
        if numero % 2 == 0:
            es_par = True
            par = numero
        i += 1
    return par


def sumar_valores_pares(numeros: list) -> int:
    """ Sumar valores pares
    Parámetros:
      numeros (list): Una lista de números enteros.
    Retorno:
      int: La suma de los números de la lista que sean pares.
    """
    suma_par = 0
    for numero in numeros:
        if numero % 2 == 0:
            suma_par += numero
    return suma_par


def sumar_pares(numeros: list) -> int:
    """ Sumar posiciones pares
    Parámetros:
      numeros (list): La lista con los números a sumar.
    Retorno:
      int: La suma de los números de la lista que están en posiciones pares.
    """
    i = 0
    suma_pospar = 0
    while i < len(numeros):
        if i % 2 == 0:
            suma_pospar += numeros[i]
        i += 1
    return suma_pospar


def calcular_definitivas(estudiantes: list) -> list:
    """ Aproximación de Notas
    Parámetros:
      estudiantes (list): Una lista de diccionarios que representan a los estudiantes que han finalizado el
                          curso, con su nota final sin aproximar.  Cada diccionario tiene las siguientes
                          llaves: "nombre": (str) el nombre del estudiante.  "nota": (float), un float que
                          representa la nota sin aproximar del estudiante.
    Retorno:
      list: La función retorna una lista de diccionarios, con tantos diccionarios como estudiantes había en la
            lista inicial, pero con sus notas aproximadas. El orden de los diccionarios debe ser el mismo de la
            lista de entrada. Cada uno de los diccionarios retornados debe tener las llaves: "nombre" (str) y
            "nota" (float).
    """
    for estudiante in estudiantes:
        nota_actual = estudiante['nota']
        if nota_actual >= 4.5:
            nueva_nota = 5.0
        elif nota_actual >= 3.5:
            nueva_nota = 4.0
        elif nota_actual >= 2.5:
            nueva_nota = 3.0
        else:
            nueva_nota = 1.5
        estudiante['nota'] = nueva_nota
    return estudiantes


def hay_suficientes_divisibles(d: int, numeros: list, n: int) -> bool:
    """ Conteo de Divisibles
    Parámetros:
      d (int): El divisor contra el que se evaluarán los números de la lista. El número 'd' será un entero
               positivo.
      numeros (list): Una lista de números enteros positivos. La lista tiene al menos un elemento.
      n (int): La cantidad de números mínima que se espera que cumplan con la condición de ser divisibles
               por 'd'. El número 'n' será un entero mayor o igual a 0.
    Retorno:
      bool: Retorna el valor True si la lista recibida tiene al menos 'n' números que cumplen con ser divisibles
            por el número 'd'. Retorna False de lo contrario.
    """
    divisibles = 0
    for numero in numeros:
        if numero % d == 0:
            divisibles += 1
    if divisibles >= n:
        divisibles = True
    else:
        divisibles = False
    return divisibles


def mismos_digitos(a: int, b: int) -> bool:
    """ Mismos Dígitos
    Parámetros:
      a (int): El primer número. Es un entero positivo.
      b (int): El segundo número. Es un entero positivo.
    Retorno:
      bool: True si los digitos que aparecen en ambos números son los mismos. False de lo contrario.
    """
    c = str(min(a, b))
    d = str(max(a, b))
    i = 0
    diferentes = False
    while i < len(c) and not diferentes:
        j = 0
        contiene = 0
        while j < len(d):
            if c[i] == d[j]:
                contiene += 1
            j += 1
        if contiene < 1:
            diferentes = True
        i += 1
    return not diferentes


def comprar_jugador(jugadores: list, monedas: int) -> str:
    """ Fifa Ultimate Team
    Parámetros:
      jugadores (list): Una lista de diccionarios que representan a los jugadores de FUT que podrían ser
                        comprados por Juan.  Cada diccionario tiene las siguientes llaves: "nombre": (str)
                        el nombre del jugador. "precio": (int), un entero que representa la cantidad de
                        monedas que vale el jugador. "media" (int): un entero mayor o igual a 50 y menor o
                        igual a 99, que representa la ponderación general del jugador.
      monedas (int): La cantidad de monedas FIFA de las que dispone Juan para comprar su jugador.
    Retorno:
      str: La función retorna el nombre del jugador comprado por Juan. Si las monedas no son suficientes para
           comprar algún jugador, retorna None.
    """
    media_selecto = 0
    precio_selecto = -1
    selecto = 'MELANI2'
    for jugador in jugadores:
        if precio_selecto == -1:
            precio_selecto = jugador['precio']
        if monedas >= jugador['precio']:
            if jugador['media'] > media_selecto or (precio_selecto >= jugador['precio'] and jugador['media'] ==
                                                    media_selecto):
                selecto = jugador['nombre']
                media_selecto = jugador['media']
                precio_selecto = jugador['precio']
        elif selecto == 'MELANI2':
            selecto = None
    return selecto


def construir_equipo_pokemon(cantidad: int, lista_pkmn: list) -> list:
    """ Ash y la liga Kalos
    Parámetros:
      cantidad (int): La cantidad de Pokémon que usará cada entrenador en la batalla final. Es un entero
                      entre 3 y 6.
      lista_pkmn (list): Una lista compuesta de diccionarios. Los diccionarios representan cada uno de los
                         Pokémon elegibles por Ash. Cada diccionario tiene las siguientes llaves: "nombre":
                         (str) el nombre del Pokémon; se garantiza que no hay nombres repetidos en los
                         diccionarios de la lista. "vida": (int),  "ataque": (int),  "defensa": (int),
                         "ataque_especial": (int), "defensa_especial": (int) , "velocidad": (int) Cada uno
                         de estos valores enteros representa la estadística respectiva del Pokémon.
    Retorno:
      list: La función retorna None si es imposible generar un equipo de Pokémon seudolegendarios para la
            batalla. De lo contrario, retorna una lista con los nombres de los Pokémon a utilizar en la batalla.
    """
    pakimanes = []
    i = 0
    cant_pakimanes = 0
    while cant_pakimanes < cantidad and i < len(lista_pkmn):
        statistics = (lista_pkmn[i]["vida"] + lista_pkmn[i]["ataque"] + lista_pkmn[i]["defensa"] +
                      lista_pkmn[i]["ataque_especial"] + lista_pkmn[i]["defensa_especial"] + lista_pkmn[i]["velocidad"])
        if statistics >= 600:
            pakimanes.append(lista_pkmn[i]['nombre'])
            cant_pakimanes += 1
        i += 1
    if cant_pakimanes != cantidad:
        pakimanes = None
    return pakimanes


def ordenar_cadena(cadena: str) -> str:
    """ Ordenar cadena de caracteres
    Parámetros:
      cadena (str): La cadena a ordenar.
    Retorno:
      str: La cadena que entró por parámetro ordenada alfabéticamente.
    """
    cadena = list(cadena)
    for i in range(0, len(cadena)):
        for j in range(0, len(cadena)):
            if cadena[i] < cadena[j]:
                temp = cadena[i]
                cadena[i] = cadena[j]
                cadena[j] = temp
    return ''.join(cadena)




# -*- coding: utf-8 -*-
"""
@author: alxus27
"""


def movimiento_robot(orientacion_actual: str, giro_1: str, giro_2: str, giro_3: str) -> str:
    """ Movimiento robótico - V2
    Parámetros:
      orientacion_actual (str): La orientación actual del robot
      giro_1 (str): La acción a ejecutar a partir de la orientación inicial del robot. Debe ser un valor de

                    los siguientes: {"L","H","R","."}
      giro_2 (str): La acción a ejecutar a partir de la orientación posterior al giro_1 del robot. Debe ser
                    un valor de los siguientes: {"L","H","R","."}
      giro_3 (str): La acción a ejecutar a partir de la orientación posterior al giro_2 del robot. Debe ser
                    un valor de los siguientes: {"L","H","R","."}
    Retorno:
      str: La orientación final del robot, debe ser uno de los siguientes valores:  {"W","N","S","E"}
    """
    orientacion_actual = movimiento_1(orientacion_actual, giro_1)
    orientacion_actual = movimiento_2(orientacion_actual, giro_2)
    orientacion_actual = movimiento_3(orientacion_actual, giro_3)
    return orientacion_actual


def movimiento_1(orientacion_actual: str, giro_1: str) -> str:
    # Primer giro
    # Norte
    if orientacion_actual == "N":
        if giro_1 == "L":
            orientacion_actual = "W"
        elif giro_1 == "H":
            orientacion_actual = "S"
        elif giro_1 == "R":
            orientacion_actual = "E"
        elif giro_1 == ".":
            orientacion_actual = orientacion_actual
        else:
            print("Comando no válido")
    # Sur
    elif orientacion_actual == "S":
        if giro_1 == "L":
            orientacion_actual = "E"
        elif giro_1 == "H":
            orientacion_actual = "N"
        elif giro_1 == "R":
            orientacion_actual = "W"
        elif giro_1 == ".":
            orientacion_actual = orientacion_actual
        else:
            print("Comando no válido")
    # Este
    elif orientacion_actual == "E":
        if giro_1 == "L":
            orientacion_actual = "N"
        elif giro_1 == "H":
            orientacion_actual = "W"
        elif giro_1 == "R":
            orientacion_actual = "S"
        elif giro_1 == ".":
            orientacion_actual = orientacion_actual
        else:
            print("Comando no válido")
    # Oeste
    elif orientacion_actual == "W":
        if giro_1 == "L":
            orientacion_actual = "S"
        elif giro_1 == "H":
            orientacion_actual = "E"
        elif giro_1 == "R":
            orientacion_actual = "N"
        elif giro_1 == ".":
            orientacion_actual = orientacion_actual
        else:
            print("Comando no válido")
    else:
        print("Dirección no válida")
    return orientacion_actual


def movimiento_2(orientacion_actual: str, giro_2: str) -> str:
    # Giro 2
    # Norte
    if orientacion_actual == "N":
        if giro_2 == "L":
            orientacion_actual = "W"
        elif giro_2 == "H":
            orientacion_actual = "S"
        elif giro_2 == "R":
            orientacion_actual = "E"
        elif giro_2 == ".":
            orientacion_actual = orientacion_actual
        else:
            print("Comando no válido")
    # Sur
    elif orientacion_actual == "S":
        if giro_2 == "L":
            orientacion_actual = "E"
        elif giro_2 == "H":
            orientacion_actual = "N"
        elif giro_2 == "R":
            orientacion_actual = "W"
        elif giro_2 == ".":
            orientacion_actual = orientacion_actual
        else:
            print("Comando no válido")
    # Este
    elif orientacion_actual == "E":
        if giro_2 == "L":
            orientacion_actual = "N"
        elif giro_2 == "H":
            orientacion_actual = "W"
        elif giro_2 == "R":
            orientacion_actual = "S"
        elif giro_2 == ".":
            orientacion_actual = orientacion_actual
        else:
            print("Comando no válido")
    # Oeste
    elif orientacion_actual == "W":
        if giro_2 == "L":
            orientacion_actual = "S"
        elif giro_2 == "H":
            orientacion_actual = "E"
        elif giro_2 == "R":
            orientacion_actual = "N"
        elif giro_2 == ".":
            orientacion_actual = orientacion_actual
        else:
            print("Comando no válido")
    else:
        print("Dirección no válida")
    return orientacion_actual


def movimiento_3(orientacion_actual: str, giro_3: str) -> str:
    # Giro 3
    # Norte
    if orientacion_actual == "N":
        if giro_3 == "L":
            orientacion_actual = "W"
        elif giro_3 == "H":
            orientacion_actual = "S"
        elif giro_3 == "R":
            orientacion_actual = "E"
        elif giro_3 == ".":
            orientacion_actual = orientacion_actual
        else:
            print("Comando no válido")
    # Sur
    elif orientacion_actual == "S":
        if giro_3 == "L":
            orientacion_actual = "E"
        elif giro_3 == "H":
            orientacion_actual = "N"
        elif giro_3 == "R":
            orientacion_actual = "W"
        elif giro_3 == ".":
            orientacion_actual = orientacion_actual
        else:
            print("Comando no válido")
    # Este
    elif orientacion_actual == "E":
        if giro_3 == "L":
            orientacion_actual = "N"
        elif giro_3 == "H":
            orientacion_actual = "W"
        elif giro_3 == "R":
            orientacion_actual = "S"
        elif giro_3 == ".":
            orientacion_actual = orientacion_actual
        else:
            print("Comando no válido")
    # Oeste
    elif orientacion_actual == "W":
        if giro_3 == "L":
            orientacion_actual = "S"
        elif giro_3 == "H":
            orientacion_actual = "E"
        elif giro_3 == "R":
            orientacion_actual = "N"
        elif giro_3 == ".":
            orientacion_actual = orientacion_actual
        else:
            print("Comando no válido")
    else:
        print("Dirección no válida")
    return orientacion_actual


def verificar_nit(NIT: int, digito: int) -> bool:
    """ Verificar NIT
    Parámetros:
      NIT (int): NIT de una empresa, sin dígito de verificación
      digito (int): Dígito de verificación
    Retorno:
      bool: Retorna True si el dígito de verificación era correcto y False de lo contrario
    """
    residuo = procesamiento_de_digitos(NIT)
    if residuo == 0 or residuo == 1:
        # Es el digito de verificación
        residuo = residuo
    else:
        # Hay que restar el residuo a 11
        residuo = 11 - residuo
    if residuo == digito:
        verificacion = True
    else:
        verificacion = False
    return verificacion


def procesamiento_de_digitos(NIT: int) -> int:
    cadena = str(NIT)
    p0 = int(cadena[0]) * 41
    p1 = int(cadena[1]) * 37
    p2 = int(cadena[2]) * 29
    p3 = int(cadena[3]) * 23
    p4 = int(cadena[4]) * 19
    p5 = int(cadena[5]) * 17
    p6 = int(cadena[6]) * 13
    p7 = int(cadena[7]) * 7
    p8 = int(cadena[8]) * 3
    suma_productos = p0 + p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8
    residuo = suma_productos % 11
    return residuo


def cambio_de_cartas(carta_mano: dict, opcion_1: dict, opcion_2: dict) -> int:
    """ Cartas
    Parámetros:
      carta_mano (dict): Carta que tiene en la mano. Tiene las llaves "numero" y "palo".
      opcion_1 (dict): Primera opción de robo. Tiene las llaves "numero" y "palo".
      opcion_2 (dict): Segunda opción de robo. Tiene las llaves "numero" y "palo".
    Retorno:
      int: Número de la carta que será robada para hacer trampa (1 o 2), o 0 si ninguna carta le ayuda.
    """
    if carta_mano["numero"] == opcion_2["numero"] or carta_mano["palo"] == opcion_2["palo"]:
        saca = 2
        if carta_mano["numero"] == opcion_1["numero"] or carta_mano["palo"] == opcion_1["palo"]:
            saca = 1
    elif carta_mano["numero"] == opcion_1["numero"] or carta_mano["palo"] == opcion_1["palo"]:
        saca = 1
    else:
        saca = 0
    return saca


def clasificar_regalo(id: int) -> str:
    """ Regalo de Santa
    Parámetros:
      id (int): El identificador del regalo cuyo tipo de persona se quiere calcular.
    Retorno:
      str: Si el número es Palíndromo e impar, el regalo corresponde a una niña, y se retorna "girl" Si el
           número es Palíndromo y par, el regalo corresponde a un niño, y se retorna "boy" Si el número es par,
           pero no palíndromo, el regalo corresponde a un hombre, y se retorna "man" Si el número es impar,
           pero no palíndromo, el regalo corresponde a una mujer, y se retorna "woman"
    """
    unidad = id % 10
    centena = id // 100
    if unidad == centena:
        if unidad % 2 == 0:
            correspondiente = "boy"
        else:
            correspondiente = "girl"
    else:
        if unidad % 2 == 0:
            correspondiente = "man"
        else:
            correspondiente = "woman"
    return correspondiente


def picas_y_fijas(numero_secreto: int, intento: int) -> dict:
    """ Picas y Fijas
    Parámetros:
      numero_secreto (int): Número el cual se debe adivinar
      intento (int): Número el cual trata de adivinar
    Retorno:
      dict: Diccionario con las llaves "PICAS" y "FIJAS" que describe el resultado de la jugada.
    """
    unidad_intento = intento % 10
    unidad_secreto = numero_secreto % 10
    intento //= 10
    numero_secreto //= 10
    decena_intento = intento % 10
    decena_secreto = numero_secreto % 10
    intento //= 10
    numero_secreto //= 10
    centena_intento = intento % 10
    centena_secreto = numero_secreto % 10
    millar_intento = intento // 10
    millar_secreto = numero_secreto // 10
    # Picas
    picas = 0
    if unidad_intento == decena_secreto:
        picas += 1
    if unidad_intento == centena_secreto:
        picas += 1
    if unidad_intento == millar_secreto:
        picas += 1
    if decena_intento == unidad_secreto:
        picas += 1
    if decena_intento == centena_secreto:
        picas += 1
    if decena_intento == millar_secreto:
        picas += 1
    if centena_intento == unidad_secreto:
        picas += 1
    if centena_intento == decena_secreto:
        picas += 1
    if centena_intento == millar_secreto:
        picas += 1
    if millar_intento == unidad_secreto:
        picas += 1
    if millar_intento == decena_secreto:
        picas += 1
    if millar_intento == centena_secreto:
        picas += 1
    # Fijas
    fijas = 0
    if unidad_intento == unidad_secreto:
        fijas += 1
    if decena_intento == decena_secreto:
        fijas += 1
    if centena_intento == centena_secreto:
        fijas += 1
    if millar_intento == millar_secreto:
        fijas += 1
    # Diccionario resultado
    resultado = {"PICAS": picas, "FIJAS": fijas}
    return resultado


def secuencia_de_fibonacci(fib_1: int, fib_2: int, fib_3: int, fib_4: int) -> str:
    """ Consecutivos de Fibonacci
    Parámetros:
      fib_1 (int): El primer caso base de esta posible secuencia de fibonacci
      fib_2 (int): El segundo caso base de esta posible secuencia de fibonacci
      fib_3 (int): El tercer término de esta posible secuencia de fibonacci; no es un caso base.
      fib_4 (int): El cuarto término de esta posible secuencia de fibonacci; no es un caso base.
    Retorno:
      str: Retorna "Fibofacil", si la secuencia corresponde a una secuencia de Fibonacci. De lo contrario,
           retorna "Fibofalsa"
    """
    if fib_3 == (fib_2 + fib_1) and fib_4 == (fib_3 + fib_2):
        verificar = "Fibofacil"
    else:
        verificar = "Fibofalsa"
    return verificar


def desperdicio_de_gaseosa(amigo_1: dict, amigo_2: dict, amigo_3: dict, capacidad_boton: float) -> str:
    """ Ida al Cine
    Parámetros:
      amigo_1 (dict): Un diccionario con las siguientes llaves: "nombre", el nombre del amigo, (str)
                      "capacidad_vaso", la capacidad máxima de su vaso, (float) "capacidad_actual", la
                      capacidad que ha sido llenada de su vaso hasta el momento (float)
      amigo_2 (dict): Un diccionario con las siguientes llaves: "nombre", el nombre del amigo, (str)
                      "capacidad_vaso", la capacidad máxima de su vaso, (float) "capacidad_actual", la
                      capacidad que ha sido llenada de su vaso hasta el momento (float)
      amigo_3 (dict): Un diccionario con las siguientes llaves: "nombre", el nombre del amigo, (str)
                      "capacidad_vaso", la capacidad máxima de su vaso, (float) "capacidad_actual", la
                      capacidad que ha sido llenada de su vaso hasta el momento (float)
      capacidad_boton (float): La cantidad de gaseosa que se servirá si los amigos deciden oprimir el botón
                               correspondiente.
    Retorno:
      str: El nombre del amigo a quien se le riega primero la gaseosa, suponiendo un orden ascendente en cuanto
           a que amigo llena primero su vaso. (Es decir, primero llena el amigo_1, luego el 2, luego el 3) Si a
           ningun amigo se le riega la gaseosa, retorne None. Si a más de un amigo se le riega la gaseosa,
           retorna el primero.
    """
    cap_restante1 = amigo_1["capacidad_vaso"] - amigo_1["capacidad_actual"]
    cap_restante2 = amigo_2["capacidad_vaso"] - amigo_2["capacidad_actual"]
    cap_restante3 = amigo_3["capacidad_vaso"] - amigo_3["capacidad_actual"]
    if cap_restante1 < capacidad_boton:
        riega = amigo_1["nombre"]
    elif cap_restante2 < capacidad_boton:
        riega = amigo_2["nombre"]
    elif cap_restante3 < capacidad_boton:
        riega = amigo_3["nombre"]
    else:
        riega = None
    return riega


def filtro_ternario(cantidad_autos: int, numero_auto: int) -> int:
    """ Filtro ternario
    Parámetros:
      cantidad_autos (int): La cantidad de carros que recibe el operario en su parqueadero
      numero_auto (int): El número único del carro a ubicar en alguno de los tres lotes de parqueo. Se
                         garantiza que es un número menor o igual que n, y mayor o igual que 1.
    Retorno:
      int: El lote de parqueadero donde el carro con el número que llega por parámetro deberá parquear. Debe
           ser un valor entre 1 y 3.
    """
    capacidad_lote = cantidad_autos // 3
    if 1 <= numero_auto <= capacidad_lote:
        lote = 1
    elif (capacidad_lote + 1) <= numero_auto <= (2 * capacidad_lote):
        lote = 2
    else:
        lote = 3
    return lote


def despacho_buses(personas_bus: int, personas_estacion: int) -> bool:
    """ La estación de Transmilenio
    Parámetros:
      personas_bus (int): Número de personas en el bus que va a detenerse
      personas_estacion (int): Número de personas esperando el bus en la estación
    Retorno:
      bool: Retorna el valor True si se debe despachar un bus nuevo y retorna False de lo contrario.
    """
    if personas_bus >= 150 or personas_estacion >= 50:
        despacho = True
    else:
        despacho = False
    return despacho


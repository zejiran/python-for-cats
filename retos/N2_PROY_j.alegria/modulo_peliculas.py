# -*- coding: utf-8 -*-
"""
Ejercicio nivel 2: Agenda de peliculas.
Módulo de cálculos.

Temas:
* Variables.
* Tipos de datos.
* Expresiones aritmeticas.
* Instrucciones basicas y consola.
* Dividir y conquistar: funciones y paso de parametros.
* Especificacion y documentacion.
* Instrucciones condicionales.
* Diccionarios.

@author: j.alegria y Cupi2.

NOTA IMPORTANTE PARA TENER EN CUENTA EN TODAS LAS FUNCIONES DE ESTE MODULO:
        Los diccionarios de pelicula tienen las siguientes parejas de clave-valor:
            - nombre (str): Nombre de la pelicula agendada.
            - genero (str): Generos de la pelicula separados por comas.
            - duracion (int): Duracion en minutos de la pelicula.
            - anio (int): Anio de estreno de la pelicula.
            - clasificacion (str): Clasificacion de restriccion por edad.
            - hora (int): Hora de inicio de la pelicula.
            - dia (str): Indica que día de la semana se planea ver la película.
"""


def crear_pelicula(nombre: str, genero: str, duracion: int, anio: int,
                   clasificacion: str, hora: int, dia: str) -> dict:
    """Crea un diccionario que representa una nueva película con toda su información 
       inicializada.
    Parámetros:
        nombre (str): Nombre de la pelicula agendada.
        genero (str): Generos de la pelicula separados por comas.
        duracion (int): Duracion en minutos de la pelicula.
        anio (int): Anio de estreno de la pelicula.
        clasificacion (str): Clasificacion de restriccion por edad.
        hora (int): Hora a la cual se planea ver la pelicula, esta debe estar entre 
                    0 y 2359.
        dia (str): Dia de la semana en el cual se planea ver la pelicula.
    Retorna:
        dict: Diccionario con los datos de la pelicula.
    """
    pelicula = {"nombre": nombre, "genero": genero, "duracion": duracion, "anio": anio, "clasificacion": clasificacion,
                "hora": hora, "dia": dia}
    return pelicula


def encontrar_pelicula(nombre_pelicula: str, p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> dict:
    """Encuentra en cual de los 5 diccionarios que se pasan por parametro esta la 
       pelicula cuyo nombre es dado por parametro.
       Si no se encuentra la pelicula se debe retornar None.
    Parametros:
        nombre_pelicula (str): El nombre de la pelicula que se desea encontrar.
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        dict: Diccionario de la pelicula cuyo nombre fue dado por parametro. 
        None si no se encuentra una pelicula con ese nombre.
    """
    if nombre_pelicula == p1["nombre"]:
        pelicula = p1
    elif nombre_pelicula == p2["nombre"]:
        pelicula = p2
    elif nombre_pelicula == p3["nombre"]:
        pelicula = p3
    elif nombre_pelicula == p4["nombre"]:
        pelicula = p4
    elif nombre_pelicula == p5["nombre"]:
        pelicula = p5
    else:
        pelicula = None
    return pelicula


def encontrar_pelicula_mas_larga(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> dict:
    """Encuentra la pelicula de mayor duracion entre las peliculas recibidas por
       parametro.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        dict: El diccionario de la pelicula de mayor duracion.
    """
    pelicula_mas_larga = {}
    # Se extraen las duraciones de las películas.
    duracion1 = p1["duracion"]
    duracion2 = p2["duracion"]
    duracion3 = p3["duracion"]
    duracion4 = p4["duracion"]
    duracion5 = p5["duracion"]
    # Se define aleatoriamente una duración larga por defecto para ser comparada con las demás.
    duracion_mas_larga = duracion1
    # Se comienzan a comparar las duraciones.
    if duracion_mas_larga == duracion1:
        pelicula_mas_larga = p1
    if duracion_mas_larga < duracion2:
        pelicula_mas_larga = p2
        duracion_mas_larga = duracion2
    if duracion_mas_larga < duracion3:
        pelicula_mas_larga = p3
        duracion_mas_larga = duracion3
    if duracion_mas_larga < duracion4:
        pelicula_mas_larga = p4
        duracion_mas_larga = duracion4
    if duracion_mas_larga < duracion5:
        pelicula_mas_larga = p5
    return pelicula_mas_larga


def duracion_promedio_peliculas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> str:
    """Calcula la duracion promedio de las peliculas que entran por parametro. 
       Esto es, la duración total de todas las peliculas dividida sobre el numero de peliculas. 
       Retorna la duracion promedio en una cadena de formato 'HH:MM' ignorando los posibles decimales.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        str: la duracion promedio de las peliculas en formato 'HH:MM'.
    """
    # Se extraen las duraciones de las películas.
    duracion1 = p1["duracion"]
    duracion2 = p2["duracion"]
    duracion3 = p3["duracion"]
    duracion4 = p4["duracion"]
    duracion5 = p5["duracion"]
    # Promedio de duraciones de las películas.
    promedio = (duracion1 + duracion2 + duracion3 + duracion4 + duracion5) / 5
    # Conversión a formato 'HH:MM'.
    horas = promedio // 60
    minutos = promedio % 60
    if horas < 10:
        horas = '0' + str(int(horas))
    else:
        horas = str(int(horas))
    if minutos < 10:
        minutos = '0' + str(int(minutos))
    else:
        minutos = str(int(minutos))
    return horas + ":" + minutos


def encontrar_estrenos(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict, anio: int) -> str:
    """Busca entre las peliculas cuales tienen como anio de estreno una fecha estrictamente
       posterior a la recibida por parametro.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
        anio (int): Anio limite para considerar la pelicula como estreno.
    Retorna:
        str: Una cadena con el nombre de la pelicula estrenada posteriormente a la fecha recibida. 
        Si hay mas de una pelicula, entonces se retornan los nombres de todas las peliculas 
        encontradas separadas por comas. Si ninguna pelicula coincide, retorna "Ninguna".
    """
    # Se establece la cadena vacía de los string a retornar con el nombre de la(s) pelicula(s) estrenada(s)
    # posteriormente a la fecha recibida.
    peliculas_posteriores = ""
    pel1 = ""
    pel2 = ""
    pel3 = ""
    pel4 = ""
    pel5 = ""
    # Se extraen los años de estreno de las películas.
    anio1 = p1["anio"]
    anio2 = p2["anio"]
    anio3 = p3["anio"]
    anio4 = p4["anio"]
    anio5 = p5["anio"]
    # Se comparan si los anios son posteriores o no a la fecha recibida.
    if anio1 > anio:
        pel1 = p1["nombre"] + ", "
    if anio2 > anio:
        pel2 = p2["nombre"] + ", "
    if anio3 > anio:
        pel3 = p3["nombre"] + ", "
    if anio4 > anio:
        pel4 = p4["nombre"] + ", "
    if anio5 > anio:
        pel5 = p5["nombre"] + ", "
    # Se prepara la cadena final
    if pel1 != "":
        peliculas_posteriores += pel1
    if pel2 != "":
        peliculas_posteriores += pel2
    if pel3 != "":
        peliculas_posteriores += pel3
    if pel4 != "":
        peliculas_posteriores += pel4
    if pel5 != "":
        peliculas_posteriores += pel5
    # Eliminar coma y esapcio final si no le sigue nada
    peliculas_posteriores = peliculas_posteriores[:-2]
    if peliculas_posteriores == "":
        peliculas_posteriores = "Ninguna"
    return peliculas_posteriores


def cuantas_peliculas_18_mas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> int:
    """Indica cuantas peliculas de clasificación '18+' hay entre los diccionarios recibidos.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        int: Numero de peliculas con clasificacion '18+'
    """
    # Contador de películas.
    numero_de18 = 0
    # Se extraen la clasificación de las películas.
    clasif1 = p1["clasificacion"]
    clasif2 = p2["clasificacion"]
    clasif3 = p3["clasificacion"]
    clasif4 = p4["clasificacion"]
    clasif5 = p5["clasificacion"]
    if "18+" in clasif1:
        numero_de18 += 1
    if "18+" in clasif2:
        numero_de18 += 1
    if "18+" in clasif3:
        numero_de18 += 1
    if "18+" in clasif4:
        numero_de18 += 1
    if "18+" in clasif5:
        numero_de18 += 1
    return numero_de18


def reagendar_pelicula(peli: dict, nueva_hora: int, nuevo_dia: str,
                       control_horario: bool, p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> bool:
    """Verifica si es posible reagendar la pelicula que entra por parametro. Para esto verifica
       si la nueva hora y el nuevo dia no entran en conflicto con ninguna otra pelicula, 
       y en caso de que el usuario haya pedido control horario verifica que se cumplan 
       las restricciones correspondientes.
    Parametros:
        peli (dict): Pelicula a reagendar
        nueva_hora (int): Nueva hora a la cual se quiere ver la pelicula
        nuevo_dia (str): Nuevo dia en el cual se quiere ver la pelicula
        control_horario (bool): Representa si el usuario quiere o no controlar
                                el horario de las peliculas.
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        bool: True en caso de que se haya podido reagendar la pelicula, False de lo contrario.
    """
    # Sacar horarios iniciales.
    peliin = nueva_hora
    h1in = p1["hora"]
    h2in = p2["hora"]
    h3in = p3["hora"]
    h4in = p4["hora"]
    h5in = p5["hora"]
    # Sacar horarios finales.
    h1fin = horafinal_en24h(p1, h1in)
    h2fin = horafinal_en24h(p2, h2in)
    h3fin = horafinal_en24h(p3, h3in)
    h4fin = horafinal_en24h(p4, h4in)
    h5fin = horafinal_en24h(p5, h5in)
    # Sacar días.
    d1 = p1["dia"]
    d2 = p2["dia"]
    d3 = p3["dia"]
    d4 = p4["dia"]
    d5 = p5["dia"]
    # Sacar género película.
    generopeli = peli["genero"]
    # Verificar conflicto.
    conflicto = False
    verificacion = False
    if control_horario:
        if "Documental" in generopeli:
            if peliin >= 2000:
                conflicto = True
        elif "Drama" in generopeli:
            if nuevo_dia == "Viernes":
                conflicto = True
        elif nuevo_dia == "Lunes" or nuevo_dia == "Martes" or nuevo_dia == "Miércoles" or nuevo_dia == "Jueves" or \
                nuevo_dia == "Viernes":
            if peliin >= 2300 or peliin <= 600:
                conflicto = True
        else:
            conflicto = False
    elif d1 == nuevo_dia:
        if peliin > h1in and peliin > h1fin:
            conflicto = False
        else:
            conflicto = True
    elif d2 == nuevo_dia:
        if peliin > h2in and peliin > h2fin:
            conflicto = False
        else:
            conflicto = True
    elif d3 == nuevo_dia:
        if peliin > h3in and peliin > h3fin:
            conflicto = False
        else:
            conflicto = True
    elif d4 == nuevo_dia:
        if peliin > h4in and peliin > h4fin:
            conflicto = False
        else:
            conflicto = True
    elif d5 == nuevo_dia:
        if peliin > h5in and peliin > h5fin:
            conflicto = False
        else:
            conflicto = True
    else:
        conflicto = False
    if not conflicto:
        verificacion = True
    return verificacion


def decidir_invitar(peli: dict, edad_invitado: int, autorizacion_padres: bool) -> bool:
    """Verifica si es posible invitar a la persona cuya edad entra por parametro a ver la 
       pelicula que entra igualmente por parametro. 
       Para esto verifica el cumplimiento de las restricciones correspondientes.
    Parametros:
        peli (dict): Pelicula que se desea ver con el invitado
        edad_invitado (int): Edad del invitado con quien se desea ver la pelicula
        autorizacion_padres (bool): Indica si el invitado cuenta con la autorizacion de sus padres 
        para ver la pelicula
    Retorna:
        bool: True en caso de que se pueda invitar a la persona, False de lo contrario.
    """
    puede = True
    if peli["clasificacion"] == "todos":
        puede = True
    elif peli["clasificacion"] == "7+":
        if edad_invitado > 7:
            puede = True
        elif autorizacion_padres or peli["genero"] == "Documental":
            puede = True
        else:
            puede = False
    elif edad_invitado <= 10:
        if peli["genero"] == "Familiar":
            puede = True
    elif peli["clasificacion"] == "13+":
        if edad_invitado > 13:
            puede = True
        elif autorizacion_padres or peli["genero"] == "Documental":
            puede = True
        else:
            puede = False
    elif edad_invitado < 15:
        if peli["genero"] == "Terror":
            puede = False
    elif peli["clasificacion"] == "16+":
        if edad_invitado > 16:
            puede = True
        elif autorizacion_padres or peli["genero"] == "Documental":
            puede = True
        else:
            puede = False
    if edad_invitado >= 18:
        puede = True
    elif peli["clasificacion"] == "18+":
        if edad_invitado > 18:
            puede = True
        elif autorizacion_padres or peli["genero"] == "Documental":
            puede = True
        else:
            puede = False
    return puede


def horafinal_en24h(peli: dict, actual: int) -> int:
    """Calcula la duracion de las peliculas que entran por parametro.
       Retorna la duracion en una cadena de formato HHMM ignorando los posibles decimales.
    Parametros:
        peli (dict): Diccionario que contiene la informacion de la pelicula.
    Retorna:
        int: la duracion de las peliculas en formato HHMM.
    """
    # Se extraen las duraciones de las películas.
    duracion = peli["duracion"]
    # Conversión a formato 'HH:MM'.
    horas = duracion // 60
    minutos = duracion % 60
    if horas < 10:
        horas = '0' + str(horas)
    else:
        horas = str(horas)
    if minutos < 10:
        minutos = '0' + str(minutos)
    else:
        minutos = str(minutos)
    hora_final = (int(horas + minutos) + actual) % 2400
    return hora_final

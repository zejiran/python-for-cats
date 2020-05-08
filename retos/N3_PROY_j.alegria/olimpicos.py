# -*- coding: utf-8 -*-
"""
Ejercicio nivel 3: Atletas Olímpicos.
Modulo de funciones para la aplicación.

@author: zejiran
"""


# Función 1.
def cargar_atletas(nombre_archivo: str) -> list:
    """
    Función que carga el archivo con los atletas a una lista.
    Parámetro:
        nombre_archivo: str.
    Retorna:
        atletas: list de diccionarios de cada atleta.
            diccionario de cada atleta: {'nombre': Nombre del atleta, 'genero': "m" o "f", 'edad': XX,
                                         'pais': país, 'anio': año de los juegos, 'evento': evento concursado,
                                         'medalla': "gold", "silver", "bronze", o "na"}.
    """
    # Inicializar lista y apertura de archivo.
    atletas = list()
    archivo = open(nombre_archivo, "r")
    # Omitir línea de títulos.
    archivo.readline()
    # Agregar datos a la lista.
    linea = archivo.readline()
    while len(linea) > 0:
        datos = linea.split(",")
        # Creación de diccionario de atleta individual
        atleta = {'nombre': datos[0], 'genero': datos[1], 'edad': datos[2],
                  'pais': datos[3], 'anio': datos[4], 'evento': datos[5],
                  'medalla': datos[6].replace("\n", '')}
        # Se añade el diccionario del atleta a la lista global de atletas.
        atletas.append(atleta)
        # Siguiente línea del archivo
        linea = archivo.readline()
    # Cierre de archivo.
    archivo.close()
    return atletas


# Función 2.
def obtener_atletas_de_anio(atletas: list, anio_interes: int) -> dict:
    """
    Función que genera un diccionario mostrando los eventos deportivos en un año
     en específico y los respectivos nombres de los atletas que estaban inscritos
     en cada evento.
    Parámetros:
        atletas: list de diccionarios con la información de cada atleta.
        anio_interes: int.
    Retorna:
        nombres_anio: dict con eventos y nombres de los atletas del año.
            diccionario con 'eventos':list: {'evento0': [nombre0, ..., nombrei],
                                              ...,
                                              'eventoi': [nombre0, ..., nombrei]}.
    """
    # Inicializar diccionario de retorno.
    nombres_anio = {}
    # Inicio de reccorido por la lista de atletas.
    for cada_atleta in atletas:
        # Verificar atletas del año de interés.
        if anio_interes == int(cada_atleta['anio']):
            # Verificar si el evento deportivo ya estaba agregado al diccionario de retorno.
            evento = nombres_anio.get(cada_atleta['evento'], "")
            if evento == "":
                # Si el evento no está en el diccionario se agrega la nueva llave de evento y el primer nombre.
                nombres_anio[cada_atleta['evento']] = [cada_atleta['nombre']]
            else:
                # De lo contrario, se anexa el nombre a la lista de nombres del evento.
                nombres_anio[cada_atleta['evento']].append(cada_atleta['nombre'])
    return nombres_anio


# Función 3.
def obtener_medallas_de_atleta(atletas: list, anio_0: int, anio_f: int, nombre_atleta: str) -> list:
    """
    Función que genera una lista de las medallas de un atleta en cierto período de tiempo definido.
    Parámetros:
        atletas: list de diccionarios con la información de cada atleta.
        anio_0: int año de inicio.
        anio_f: int año final.
        nombre_atleta: str
    Retorna:
        medallas_atleta: list con diccionarios de cada medalla.
            diccionario de cada medalla: {'evento': str, 'anio': int, 'medalla': str}.
    """
    # Inicializar lista de medallas.
    medallas_atleta = list()
    # Inicio de recorrido por la lista de atletas.
    for cada_atleta in atletas:
        # Definición de variables del atleta actual.
        anio_actual = int(cada_atleta['anio'])
        nombre_actual = cada_atleta['nombre']
        evento_actual = cada_atleta['evento']
        medalla_actual = cada_atleta['medalla']
        # Verificación de nombre y rango de tiempo.
        if nombre_actual == nombre_atleta:
            if anio_0 <= anio_actual <= anio_f:
                # Se añade el diccionario de medalla a la lista.
                medallas_atleta.append({'evento': evento_actual, 'anio': anio_actual, 'medalla': medalla_actual})
    # Si no hay medallas se coloca un mensaje en la lista de retorno.
    if not medallas_atleta:
        medallas_atleta.append("No hay medallas para ese atleta")
    return medallas_atleta


# Función 4.
def obtener_atletas_pais(atletas: list, pais_interes: str) -> list:
    """
    Función que genera una lista con la información de los atletas del país dado,
     sin importar el año en que participaron los atletas.
    Parámetros:
        atletas: list de diccionarios con la información de cada atleta.
        pais_interes: str.
    Retorna:
        atletas_pais: list con los diccionarios de los atletas del país.
            diccionario de cada atleta: {'nombre': str, 'evento': str, 'anio': int}.
    """
    # Inicializar lista de atletas del país.
    atletas_pais = list()
    # Inicio de recorrido por la lista de atletas.
    for cada_atleta in atletas:
        # Definición de variables del atleta actual.
        anio_actual = cada_atleta['anio']
        nombre_actual = cada_atleta['nombre']
        evento_actual = cada_atleta['evento']
        pais_actual = cada_atleta['pais']
        # Verificación de nombre y rango de tiempo.
        if pais_actual == pais_interes:
            # Se añade el diccionario de atleta a la lista de atletas.
            atletas_pais.append({'nombre': nombre_actual, 'evento': evento_actual, 'anio': anio_actual})
    # Si no hay atletas en el país se coloca un mensaje en la lista de retorno.
    if not atletas_pais:
        atletas_pais.append("No hay medallas para ese atleta")
    return atletas_pais


# Función 5.
def encontrar_pais_medallista(atletas: list) -> dict:
    """
    Función que genera un diccionario mostrando el país con mayor
     cantidad de medallistas en todos los tiempos de los juegos olímpicos.
    Parámetros:
        atletas: list de diccionarios con la información de cada atleta.
    Retorna:
        pais_medallista: {nombre pais: int cantidad de medallistas}.
    """
    # Inicializar diccionario del país medallista.
    pais_medallista = dict()
    # Definición de variables.
    max_medallas = 0
    medallista = ""
    # Inicio de recorrido por la lista de atletas.
    for cada_atleta in atletas:
        # Definición de país y medalla del atleta actual.
        pais_actual = cada_atleta['pais']
        medalla_actual = cada_atleta['medalla']
        # Se agrega temporalmente cada país y sus medallas al diccionario.
        if medalla_actual != "na":
            # Si el país nunca ha aparecido en el diccionario, se agrega.
            if pais_actual not in pais_medallista:
                pais_medallista[pais_actual] = 1
            # Si el país ya estaba en el diccionario, se suma una medalla.
            else:
                pais_medallista[pais_actual] += 1
            # Se verifica el país con el máximo número de medallas por el momento.
            if pais_medallista[pais_actual] > max_medallas:
                max_medallas = pais_medallista[pais_actual]
                medallista = pais_actual
    # Se agrega la información del país con mayor cantidad de medallas al diccionario.
    pais_medallista = {medallista: max_medallas}
    return pais_medallista


# Función 6.
def obtener_ganadores_de_evento(atletas: list, evento_interes: str) -> list:
    """
    Función que genera una lista de str, que contiene los nombres de todos los
     atletas que han ganado alguna medalla en el evento de interés (sin importar el año en que la obtuvieron).
     Si un atleta ha ganado más de una medalla en este evento, no debe aparecer repetido el nombre de dicho atleta.
    Parámetros:
        atletas: list de diccionarios con la información de cada atleta.
        evento_interes: str.
    Retorna:
        ganadores: list de nombres.
    """
    # Inicializar lista de ganadores en el evento.
    ganadores = list()
    # Inicio de recorrido por la lista de atletas.
    for cada_atleta in atletas:
        # Definición de datos del atleta actual.
        nombre_actual = cada_atleta['nombre']
        medalla_actual = cada_atleta['medalla']
        evento_actual = cada_atleta['evento']
        # Se verifica si es ganador y si corresponde al evento de interés.
        if medalla_actual != "na" and evento_actual == evento_interes:
            # Se verifica que el atleta no haya sido agregado anteriormente.
            if nombre_actual not in ganadores:
                ganadores.append(nombre_actual)
    return ganadores


# Función 7.
def obtener_atletas_medallas_superiores_a_numero(atletas: list, numero_medallas: int) -> dict:
    """
    Función que genera un diccionario con los atletas que han ganado una cantidad de
     medallas estrictamente superior al número dado por parámetro, en todos los tiempos.
    Parámetros:
        atletas: list de diccionarios con la información de cada atleta.
        numero_medallas: int.
    Retorna:
        ganadores_superiores: {nombre0: int medallas ganadas,
                               ...,
                               nombrei: int medallas ganadas}.
    """
    # Inicializar diccionario de atletas aprobados.
    ganadores_superiores = {}
    # Inicio de recorrido por la lista de atletas.
    for cada_atleta in atletas:
        # Datos del atleta actual.
        nombre_actual = cada_atleta['nombre']
        medalla_actual = cada_atleta['medalla']
        # Se agrega temporalmente la cantidad de medallas total de todos los atletas al diccionario.
        if medalla_actual != "na":
            medallas_atleta = ganadores_superiores.get(nombre_actual, 0)
            ganadores_superiores[nombre_actual] = medallas_atleta + 1
    # Recorrido por diccionario para eliminar a los atletas que no tienen la cantidad de medallas requeridas.
    for cada_atleta in ganadores_superiores:
        medallas_atleta = ganadores_superiores[cada_atleta]
        # Los atletas que tienen medallas estrictamente superiores al parámetro, no serán eliminados.
        if medallas_atleta <= numero_medallas:
            del ganadores_superiores[cada_atleta]
    return ganadores_superiores


# Función 8.
def encontrar_atletas_estrella(atletas: list) -> dict:
    """
    Función que genera un diccionario que representa al atleta estrella
     de todos los tiempos (esto es, el atleta que ha obtenido el mayor
     número de medallas a lo largo de todos los años).
     Si dos o más atletas se encuentran empatados, el diccionario debe incluir
     dos o más llaves con sus respectivos números de medallas.
    Parámetros:
        atletas: list de diccionarios con la información de cada atleta.
    Retorna:
        estrellas: {'nombre': int número de medallas ganadas}.
    """
    # Inicializar diccionario de las estrellas.
    estrellas = {}
    # Definición de variables.
    mas_medallas = 0
    # Inicio de recorrido por la lista de atletas.
    for cada_atleta in atletas:
        # Definición de datos del atleta actual.
        nombre_actual = cada_atleta['nombre']
        medalla_actual = cada_atleta['medalla']
        # Se agrega temporalmente cada atleta y sus medallas al diccionario.
        if medalla_actual != "na":
            medallas = estrellas.get(nombre_actual, 0)
            estrellas[nombre_actual] = medallas + 1
            # Se verifica el país con el máximo número de medallas por el momento.
            if estrellas[nombre_actual] > mas_medallas:
                mas_medallas = estrellas[nombre_actual]
    # Se eliminan todos los atletas que no estén empatados con la estrella.
    for cada_atleta in estrellas:
        if estrellas[cada_atleta] < mas_medallas:
            del estrellas[cada_atleta]
    return estrellas


# Función 9.
def encontrar_pais_destacado_en_evento(atletas: list, evento: str) -> dict:
    """
    Función que retorna el país que ha tenido mejor desempeño en el evento recibido por parámetro.
     Es el país que más medallas de valor ha ganado en un evento determinado, en todos los tiempos.
     Esto se determina por el número y categoría de las medallas. Es decir, que el mejor país es
     aquel que tenga más medallas de oro. En caso de empate con otro país, será mejor el que tenga
     más medallas de plata entre estos, y si el empate persiste, se definirá por
     el número de medallas de bronce.
    Parámetros:
        atletas: list de diccionarios con la información de cada atleta.
        evento: str nombre de evento de interés.
    Retorna:
        pais_destacado = {'nombre': [int gold, int silver, int bronze]}
         Si se encuentran 2 o más países igual de exitosos y que sean el mejor,
         el diccionario debe contenerlos a todos.
    """
    # Inicializar diccionario de las estrellas.
    paises = {}
    # Definición de variables.
    mas_medallas_oro = 0
    mas_medallas_plata = 0
    mas_medallas_bronce = 0
    # Inicio de recorrido por la lista de atletas.
    for cada_atleta in atletas:
        # Se verifica el evento de interés.
        if evento == cada_atleta['evento']:
            # Definición de datos del atleta actual.
            medalla_actual = cada_atleta['medalla']
            pais_actual = cada_atleta['pais']
            # Se agrega la medalla al diccionario de paises en la llave correspondiente.
            if medalla_actual != "na":
                # Si no se ha registrado el país, se inicializa el número de medallas del país en una lista.
                paises[pais_actual] = [0, 0, 0]
                # Se incrementa la medalla en la lista de acuerdo al tipo.
                if medalla_actual == "gold":
                    paises[pais_actual][0] += 1
                elif medalla_actual == "silver":
                    paises[pais_actual][1] += 1
                else:
                    paises[pais_actual][2] += 1
                # Se verifica el país con el máximo número de medallas de oro por el momento.
                if paises[pais_actual][0] > mas_medallas_oro:
                    mas_medallas_oro = paises[pais_actual][0]
    # Desempates plata.
    for cada_pais in paises:
        # Se eliminan todos los países que no estén empatados con el país ganador de oro.
        if paises[cada_pais][0] < mas_medallas_oro:
            del paises[cada_pais]
        else:
            # Se verifica el país con el máximo número de medallas de plata entre los países empatados en oro.
            if paises[cada_pais][1] > mas_medallas_plata:
                mas_medallas_plata = paises[cada_pais][1]
    # Desempates bronce.
    for cada_pais in paises:
        # Se eliminan todos los paises que no estén empatados con el país ganador de plata.
        if paises[cada_pais][1] < mas_medallas_plata:
            del paises[cada_pais]
        else:
            # Se verifica el país con el máximo número de medallas de bronce entre los países empatados en plata.
            if paises[cada_pais][2] > mas_medallas_bronce:
                mas_medallas_bronce = paises[cada_pais][2]
    # Permanece solamente los países empatados en bronce.
    for cada_pais in paises:
        # Se eliminan todos los paises que no estén empatados con el país ganador de bronce.
        if paises[cada_pais][2] < mas_medallas_bronce:
            del paises[cada_pais]
    return paises


# Función 10.
def encontrar_todoterreno(atletas: list) -> str:
    """
    Función que retorna el nombre del atleta más “Todoterreno”. Es decir, aquel que haya participado
     en más eventos diferentes a través de los años. Solo se cuenta una vez cada deporte,
     si un atleta participó en el mismo evento en años diferentes, solo debe contarse como un evento único.
    Parámetros:
        atletas: list de diccionarios con la información de cada atleta.
    Retorna:
        todoterreno: str nombre de atleta todoterreno.
    """
    # Inicializar diccionario del todoterreno.
    todoterreno = {}
    # Definición de variables.
    mas_eventos = 0
    nombre_todoterreno = ""
    # Inicio de recorrido por la lista de atletas.
    for cada_atleta in atletas:
        # Definición de datos del atleta actual.
        nombre_actual = cada_atleta['nombre']
        evento_actual = cada_atleta['evento']
        # Se agrega cada atleta y sus eventos a una lista del diccionario, si no está el evento agregado.
        if evento_actual not in todoterreno[nombre_actual]:
            # Se agrega el evento actual a la lista dentro del diccionario con llave el atleta.
            todoterreno[nombre_actual].append(evento_actual)
            # Se obtiene el número de eventos del atleta
            eventos = todoterreno.get(nombre_actual, [0])[0]
            # Se agrega un evento más a la posición 0 de la lista del atleta
            todoterreno[nombre_actual][0] = eventos + 1
        # Se verifica el atleta todoterreno.
        if todoterreno[nombre_actual][0] >= mas_eventos:
            mas_eventos = todoterreno[nombre_actual][0]
            nombre_todoterreno = nombre_actual
    return nombre_todoterreno


# Función 11.
def obtener_medallistas_por_genero_pais(atletas: list, pais: str, genero: str) -> dict:
    """
    Función que retorna un diccionario con los medallistas del país y género recibidos por parámetro.
    Parámetros:
        atletas: list de diccionarios con la información de cada atleta.
        pais: str nombre del país.
        genero: str “m” o “f”.
    Retorna:
        medallistas: {'nombre': [{'evento': str evento, 'anio': int año, 'medalla': str tipo-medalla},...],...}.
    """
    # Inicializar diccionario para los medallistas del género y país correspondiente.
    medallistas = {}
    # Inicio de recorrido por la lista de atletas.
    for cada_atleta in atletas:
        # Definición de datos del atleta actual.
        anio_actual = cada_atleta['anio']
        nombre_actual = cada_atleta['nombre']
        evento_actual = cada_atleta['evento']
        pais_actual = cada_atleta['pais']
        medalla_actual = cada_atleta['medalla']
        genero_actual = cada_atleta['genero']
        # Se agrega los atletas ganadores del país y género al diccionario.
        if pais == pais_actual and genero == genero_actual:
            if medalla_actual != "na":
                # Diccionario de medalla actual del atleta.
                medalla = {'evento': evento_actual, 'anio': anio_actual, 'medalla': medalla_actual}
                # Obtener lista de medallas del atleta.
                medallas_atleta = medallistas.get(nombre_actual, [])
                # Agregar la medalla actual a la lista de medallas del atleta.
                medallas_atleta.append(medalla)
                # Agregar el diccionario de la medalla a la lista del atleta
                #  dentro del diccionario de todos los medallistas.
                medallistas[nombre_actual] = medallas_atleta
    return medallistas


# Función 12.
def calcular_porcentaje_ganador(atletas: list) -> float:
    """
    Función retorna el porcentaje de atletas que ganaron alguna medalla, en todos los tiempos, con dos decimales de
     aproximación. Cada atleta debe considerarse una sola vez así haya participado en varios eventos o en varios años.
    Parámetros:
        atletas: list de diccionarios con la información de cada atleta.
    Retorna:
        porcentaje_ganadores: float de dos decimales
            Porcentaje Medallistas = Número de Medallistas / Número de Atletas
    """
    # Inicializar variables de conteo y lista para agregar atletas.
    atletas_agregados = []
    medallistas = 0
    atletas_totales = 0
    # Inicio de recorrido por la lista de atletas.
    for cada_atleta in atletas:
        # Definición de nombre y medalla del atleta actual.
        nombre_actual = cada_atleta['nombre']
        medalla_actual = cada_atleta['medalla']
        # Se agrega los atletas ganadores a la lista de conteo.
        if medalla_actual != "na":
            # Si el atleta nunca ha aparecido en la lista, se agrega.
            if nombre_actual not in atletas_agregados:
                atletas_agregados.append(nombre_actual)
                # Se incrementa el número de medallistas.
                medallistas += 1
                # Se incrementa el número de atletas totales.
                atletas_totales += 1
        # Los no ganadores incrementan el número de atletas totales y se agregan a la lista para no repetir.
        elif nombre_actual not in atletas_agregados:
            atletas_agregados.append(nombre_actual)
            atletas_totales += 1
    # Se calcula el porcentaje de medallistas.
    porcentaje_ganadores = round(medallistas / atletas_totales, 2)
    return porcentaje_ganadores

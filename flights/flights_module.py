# -*- coding: utf-8 -*-
"""
@author: alxus27
"""


def cargar_vuelos(ruta_archivo: str) -> dict:
    """
    Esta función carga la información un conjunto de vuelos a partir de un archivo CSV.
    Los valores dentro del archivo deben estar separados por comas y estar en el siguiente orden:
        aerolinea,codigo_vuelo,origen,destino,distancia,salida,duracion,retraso
    La primera línea del archivo debe corresponder a los títulos de las columnas.
    Parámetros:
        ruta_archivo: la ruta del archivo que se quiere cargar
    Retorno:
        Un diccionario con la información de los vuelos.
        Las llaves del diccionario corresponderán a los códigos de los vuelos.
        Los valores del diccionario deben ser también diccionarios con las siguientes llaves:
            aerolinea,origen,destino,distancia,salida,duracion,retraso
    """
    vuelos = {}
    archivo = open(ruta_archivo)
    titulos = archivo.readline().split(",")
    linea = archivo.readline()
    while len(linea) > 0:
        datos = linea.split(",")
        codigo_vuelo = datos[1]
        vuelo = {"aerolinea": datos[0], "origen": datos[2], "destino": datos[3], "distancia": datos[4],
                 "salida": datos[5], "duracion": datos[6], "retraso": datos[7].replace("\n", '')}
        vuelos[codigo_vuelo] = vuelo
        linea = archivo.readline()
    archivo.close()
    return vuelos

    
def vuelos_directos(vuelos: dict, origen: str, destino: str) -> list:
    """
    Esta función busca todos los vuelos directos que van del aeropuerto de origen 
    al aeropuerto de destino.
    Parámetros:
        vuelos (dict): Un diccionario con los vuelos. Las llaves corresponden a 
        los códigos de los vuelos.
        origen (str): El código del aeropuerto origen para el trayecto buscado.
        destino (str): El código del aeropuerto destino para el trayecto buscado.
    Retorno: list
        Lista de diccionarios con toda la información (incluyendo los códigos) de 
        todos los vuelos directos que van del aeropuerto de origen al aeropuerto 
        de destino. Los diccionarios que se añaden en la lista deben tener como 
        llave el código del vuelo y como valor el resto de la información del vuelo.
        
        Si en el diccionario de vuelos que entra por parámetro no hay ningún 
        vuelo para ese trayecto, la función debe retornar una lista vacía.
    """
    lista = []
    if vuelos != {}:
        for cada_vuelo in vuelos:
            if vuelos[cada_vuelo]['origen'] == origen and vuelos[cada_vuelo]['destino'] == destino:
                lista.append({cada_vuelo: vuelos[cada_vuelo]})
    return lista


def vuelos_con_una_escala(vuelos: dict, origen: str, destino: str) -> list:
    """
    Esta función busca todos los vuelos con una escala que van
    del aeropuerto de origen al aeropuerto de destino.
    Parámetros:
        vuelos (dict): Un diccionario con los vuelos. Las llaves corresponden a 
        los códigos de los vuelos.
        origen (str): El código del aeropuerto origen para el trayecto buscado.
        destino (str): El código del aeropuerto destino para el trayecto buscado.
    Retorno: list
        Lista de listas. Estas últimas son listas de dos elementos, que corresponden 
        a los códigos de los 2 vuelos que permiten ir del origen al destino.
        
        Si en el diccionario de vuelos que entra por parámetro no hay ningún 
        vuelo para ese trayecto, la función debe retornar una lista vacía.
    """
    lista = []
    if vuelos != {}:
        codigos_origen = []
        codigos_destino = []
        for cada_vuelo in vuelos:
            diccionario = vuelos[cada_vuelo]
            if diccionario['origen'] == origen and diccionario['destino'] != destino:
                codigos_origen.append(cada_vuelo)
            if diccionario['destino'] == destino and diccionario['origen'] != origen:
                codigos_destino.append(cada_vuelo)
        for codigoX in codigos_destino:
            for codigoY in codigos_origen:
                if vuelos[codigoX]['origen'] == vuelos[codigoY]['destino']:
                    lista.append([codigoY, codigoX])
    return lista


def sugerir_aerolinea(vuelos: dict, origen: str, destino: str) -> str:
    """
    Esta función sugiere cuál aerolínea utilizar para ir entre un par de aeropuertos.
    La aerolínea recomendada será aquella que haya acumulado el menor retraso 
    promedio recorriendo la ruta solicitada.
    Parámetros:
        vuelos (dict): Un diccionario con los vuelos. Las llaves corresponden a los códigos de los vuelos.
        origen (str): El código del aeropuerto origen para el trayecto buscado.
        destino (str): El código del aeropuerto destino para el trayecto buscado.
    Retorno: str
        El nombre de la aerolínea sugerida.
        Si ninguna aerolínea cubre la ruta seleccionada, retorna None
    """
    vuelos_en_ruta = vuelos_directos(vuelos, origen, destino)
    recomendada = 0
    if not vuelos_en_ruta:
        pass
    else:
        recomendada = vuelos_en_ruta[0]
        i = 0
        while i < len(vuelos_en_ruta):
            actual = vuelos_en_ruta[i]
            codigo_actual = " ".join(list(actual.keys()))
            codigo_recomendado = " ".join(list(recomendada.keys()))
            if vuelos[codigo_actual]['retraso'] < vuelos[codigo_recomendado]['retraso']:
                recomendada = actual
            i += 1
        codigo_recomendado = " ".join(list(recomendada.keys()))
        recomendada = vuelos[codigo_recomendado]['aerolinea']
    return recomendada

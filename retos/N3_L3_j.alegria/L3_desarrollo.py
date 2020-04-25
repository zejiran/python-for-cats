# -*- coding: utf-8 -*-
"""
@author: alxus27
"""


# Primer problema: buscar elementos iguales consecutivos.
def buscar_elementos_iguales_seguidos(numeros: list) -> int:
    # Inicializar variables.
    posicion = 0
    posicion_seguidos = -1
    no_ha_encontrado_seguidos = True
    # Inicio de recorrido en la lista.
    while no_ha_encontrado_seguidos and posicion + 1 < len(numeros):
        # Si los numeros en la posición siguiente son iguales a la actual, son seguidos.
        if numeros[posicion + 1] == numeros[posicion]:
            posicion_seguidos = posicion
            no_ha_encontrado_seguidos = False
        # Se aumenta la posición
        posicion += 1
    return posicion_seguidos


# Segundo problema: contar apariciones de una sublista en lista.
def contar_apariciones(numeros: list, subnumeros: list) -> int:
    apariciones = 0
    # Se repite mientras el primer elemento de la sublista este en la lista.
    while subnumeros[0] in numeros:
        # Reseteo de variables
        intercalado = False
        se_paso = False
        i = 0
        # Se encuentra la posición del primer número de la sublista en la lista.
        posicion = numeros.index(subnumeros[0])
        # Inicio de comparación entre listas:
        # Se repite la comparación mientras el contador sea menor que len(sublista),
        # no se ha verificado una posible intercalación,
        # y la posición no se ha salido del rango de la lista.
        while i < len(subnumeros) and not intercalado and not se_paso:
            # Se elimina de la lista el elemento en común.
            if numeros[posicion] == subnumeros[i]:
                del numeros[posicion]
            else:
                intercalado = True
            # Verificar que la posición no esté fuera de rango.
            if posicion >= len(numeros):
                se_paso = True
            # Se aumenta la posición de la sublista.
            i += 1
        # Si al finalizar la comparación no existió una posible intercalación
        # ni se salió del rango, se considera una aparición de la sublista.
        if not intercalado and not se_paso:
            apariciones += 1
    return apariciones


# Tercer problema: ubicación de tiendas para el señor diseñador.
def ubicaciones_viables(ciudades: list, cantidad_minima: int) -> dict:
    # Si la lista de ciudades estaba vacía, se retorna None.
    if not ciudades:
        pass
    else:
        # Se inicializan las listas de retorno vacías.
        viables = []
        inviables = []
        # Cada elemento de ciudades es de la forma: {'nombre': str, 'población': int}.
        for ciudad in ciudades:
            if ciudad['poblacion'] >= cantidad_minima:
                viables.append(ciudad)
            else:
                inviables.append(ciudad)
        # Si ninguna ciudad es viable/inviable se indica con un str en el retorno correspondiente.
        if not viables:
            viables = "Ninguna ciudad es viable"
        if not inviables:
            inviables = "Ninguna ciudad es inviable"
        return {'viables': viables, 'inviables': inviables}

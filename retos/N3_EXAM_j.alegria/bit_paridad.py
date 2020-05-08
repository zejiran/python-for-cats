# -*- coding: utf-8 -*-
"""
Ejercicio de examen nivel 3 - #1: Mecanismo simple bit de paridad.

@author: zejiran/j.alegria.
"""


def calcular_bit_paridad(grupos_bits: list, paridad: int) -> dict:
    """
    Función que obtiene un diccionario con el valor de bit de paridad correspondiente
     a cada grupo de bit de la lista recibida por parámetro.
    Parámetros:
        grupo_bits: list que contiene grupos de 8 bits representados como strings.
        paridad: int paridad a usar, ya sea 0-par o 1-impar.
    Retorno:
        paridad_de_grupos: dict {'grupo_8_bits': bit_paridad_correspondiente}.
    """
    # Se define el diccionario de retorno.
    paridad_de_grupos = dict()
    # Inicio de recorrido
    for cada_grupo in grupos_bits:
        # Inicializar variable de conteo de bits-1.
        bits_1 = 0
        # Contar número de bits-1 en grupo.
        for cada_bit in cada_grupo:
            if cada_bit == '1':
                bits_1 += 1
        # Verificar paridad seleccionada.
        # Paridad par.
        if paridad % 2 == 0:
            # Agregar bit de paridad de acuerdo al total de bits_1.
            if bits_1 % 2 == 0:
                paridad_de_grupos[cada_grupo] = '0'
            else:
                paridad_de_grupos[cada_grupo] = '1'
        # Paridad impar.
        else:
            # Agregar bit de paridad de acuerdo al total de bits_1.
            if bits_1 % 2 != 0:
                paridad_de_grupos[cada_grupo] = '0'
            else:
                paridad_de_grupos[cada_grupo] = '1'
    return paridad_de_grupos

# Prueba.
# print(calcular_bit_paridad(['01010000', '00000001', '00000000'], 1))

# -*- coding: utf-8 -*-
"""
@author: zejiran
"""


def crear_amigo(nombre: str, anio_conocimiento: int, pareja: bool, presupuesto_semanal: float,
                adicional_semanal: float, licor_tomado: int, vegano: bool, carro: bool, salidas_semanales: int) -> dict:
    amigo = {"nombre": nombre, "anio conocimiento": anio_conocimiento, "pareja": pareja,
             "presupuesto semanal": presupuesto_semanal, "adicional semana": adicional_semanal,
             "licor tomado": licor_tomado, "vegano": vegano, "carro": carro, "salidas semanales": salidas_semanales}
    return amigo


def calcular_gastos_semanales(amigo: dict) -> float:
    gastos = 0
    if amigo["carro"]:
        gastos += 45000
        gastos = gastos + ((amigo["salidas semanales"]) * 9000)
    if amigo["pareja"]:
        gastos /= 2
    # comida
    if amigo["vegano"]:
        gastos += (110000 * 1.15)
        gastos += amigo["salidas semanales"] * (25000 * 1.15)
    else:
        gastos += 110000
        gastos += amigo["salidas semanales"] * 25000
    if not amigo["carro"]:
        gastos = amigo["licor tomado"] * 15600
    gastos = round(gastos, 2)
    return gastos


def conocido(amigo: dict, anio_actual: int) -> bool:
    tiempo_conocidos = anio_actual - amigo["anio conocimiento"]
    if tiempo_conocidos >= 1:
        es_conocido = True
    else:
        es_conocido = False
    return es_conocido


def calcular_ahorro(amigo: dict, gastos) -> float:
    ahorro = amigo["presupuesto semanal"] + amigo["adicional semana"] - gastos
    return ahorro


def diccionario_final(a1: dict, a2: dict, a3: dict, a4: dict) -> dict:
    final = {}
    amigo_valido(a1, final)
    amigo_valido(a2, final)
    amigo_valido(a3, final)
    amigo_valido(a4, final)
    return final


def amigo_valido(amigo: dict, final: dict) -> None:
    gastos = calcular_gastos_semanales(amigo)
    es_conocido = conocido(amigo, 2020)
    ahorro = calcular_ahorro(amigo, gastos)
    if es_conocido and ahorro >= 45000:
        final[amigo["nombre"]] = ahorro

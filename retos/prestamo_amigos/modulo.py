# -*- coding: utf-8 -*-
"""
@author: alxus27
"""


def crear_amigo(nombre: str, anio_conocimiento: int, pareja: bool, presupuesto_semanal: float,
                adicional_semanal: float, licor_tomado: int, vegano: bool, carro: bool, salidas_semanales: int) -> dict:
    amigo = {"nombre": nombre, "anio conocimiento": anio_conocimiento, "pareja": pareja,
             "presupuesto semanal": presupuesto_semanal, "adicional semana": adicional_semanal,
             "licor tomado": licor_tomado, "vegano": vegano, carro: "carro", "salidas semanales": salidas_semanales}
    return amigo


def calcular_gastos_semanales(amigo: dict) -> float:
    gastos = 0
    if amigo["carro"]:
        gastos += 45000
        gastos = gastos + ((amigo["salidas semanales"]) * 9000)
    if amigo["pareja"]:
        gastos /= 2
    #comida
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

def calcular_ahorro(gastos: float, amigo: dict) -> float:
    ahorro = amigo["presupuesto_semanal"] + amigo["adicional_semana"] - gastos
    return ahorro

def diccionario_final(amigo: dict, ahorro: float) -> dict:
    diccionario = {"amigo": amigo["nombre"], "gastos": gastos}
    return diccionario

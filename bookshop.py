# -*- coding: utf-8 -*-
"""
@ created by zejiran
"""


def crear_libro(nom: str, cod: str, autor: int, adp: int, cant: int, pdv: float, cpu: float) -> dict:
    dic_libro = {"nombre": nom,
                 "codigo": cod,
                 "autor": autor,
                 "añoPublicacion": adp,
                 "cantidad": cant,
                 "precio": pdv,
                 "costoProduccion": cpu}
    return dic_libro


def mayor_ganancia(libro1: dict, libro2: dict, libro3: dict, libro4: dict) -> dict:
    ganancia1 = libro1["precio"] - libro1["costoProduccion"]
    ganancia2 = libro2["precio"] - libro2["costoProduccion"]
    ganancia3 = libro3["precio"] - libro3["costoProduccion"]
    ganancia4 = libro4["precio"] - libro4["costoProduccion"]
    mayor_ganancia = ganancia1
    if mayor_ganancia < ganancia2:
        libro_mas_ganancia = libro2
    if mayor_ganancia < ganancia3:
        libro_mas_ganancia = libro3
    if mayor_ganancia < ganancia4:
        libro_mas_ganancia = libro4
    if mayor_ganancia == ganancia1:
        libro_mas_ganancia = libro1
    return libro_mas_ganancia


def hacer_pedido(nom_lib: str, libro1: dict, libro2: dict, libro3: dict, libro4: dict) -> bool:
    if nom_lib == libro1["nombre"]:
        if 50 >= libro1["cantidad"] > 100:
            pedido_verificado = True
        else:
            pedido_verificado = False
    elif nom_lib == libro2["nombre"]:
        if 50 >= libro2["cantidad"] > 100:
            pedido_verificado = True
        else:
            pedido_verificado = False
    elif nom_lib == libro3["nombre"]:
        if 50 >= libro3["cantidad"] > 100:
            pedido_verificado = True
        else:
            pedido_verificado = False
    elif nom_lib == libro4["nombre"]:
        if 50 >= libro4["cantidad"] > 100:
            pedido_verificado = True
        else:
            pedido_verificado = False
    else:
        pedido_verificado = False
    return pedido_verificado


def publicacion_antes_anio(anio: int, libro1: dict, libro2: dict, libro3: dict, libro4: dict) -> dict:
    libros_antes_anio = {}
    if anio > libro1["añoPublicacion"]:
        libros_antes_anio[libro1["nombre"]] = libro1["añoPublicacion"]
    if anio > libro2["añoPublicacion"]:
        libros_antes_anio[libro2["nombre"]] = libro2["añoPublicacion"]
    if anio > libro3["añoPublicacion"]:
        libros_antes_anio[libro3["nombre"]] = libro3["añoPublicacion"]
    if anio > libro4["añoPublicacion"]:
        libros_antes_anio[libro4["nombre"]] = libro4["añoPublicacion"]
    # if libros_antes_anio == {}:
    # return "No hay libros antes del año seleccionado"
    return libros_antes_anio


def ganancias_venta_libro(nom_lib: str, cant_vender: int, libro1: dict, libro2: dict, libro3: dict,
                          libro4: dict) -> dict:
    if nom_lib == libro1["nombre"]:
        ganancia = cant_vender * (libro1["precio"] - libro1["costoProduccion"])
    elif nom_lib == libro2["nombre"]:
        ganancia = cant_vender * (libro2["precio"] - libro2["costoProduccion"])
    elif nom_lib == libro3["nombre"]:
        ganancia = cant_vender * (libro3["precio"] - libro3["costoProduccion"])
    elif nom_lib == libro4["nombre"]:
        ganancia = cant_vender * (libro4["precio"] - libro4["costoProduccion"])
    else:
        ganancia = 0
    # else:
    # return "No tenemos ese libro"
    return {"nombre": nom_lib, "ganancias": ganancia}


def venta_por_mayor(nom_lib: str, cant_vender: int, libro1: dict, libro2: dict, libro3: dict, libro4: dict) -> dict:
    nom_lib = nom_lib.title()
    if nom_lib == libro1["nombre"]:
        ganancia = cant_vender * (libro1["precio"] - libro1["costoProduccion"])
        if cant_vender > (0.25 * libro1["cantidad"]) and cant_vender < (0.5 * libro1["cantidad"]):
            descuento = 0.1 * ganancia
        elif cant_vender > (0.5 * libro1["cantidad"]) and cant_vender < (0.75 * libro1["cantidad"]):
            descuento = 0.2 * ganancia
        elif cant_vender > (0.75 * libro1["cantidad"]):
            descuento = 0.3 * ganancia
    elif nom_lib == libro2["nombre"]:
        ganancia = cant_vender * (libro2["precio"] - libro2["costoProduccion"])
        if (0.25 * libro2["cantidad"]) < cant_vender < (0.5 * libro2["cantidad"]):
            descuento = 0.1 * ganancia
        elif (0.5 * libro2["cantidad"]) < cant_vender < (0.75 * libro2["cantidad"]):
            descuento = 0.2 * ganancia
        elif cant_vender > (0.75 * libro2["cantidad"]):
            descuento = 0.3 * ganancia
    elif nom_lib == libro3["nombre"]:
        ganancia = cant_vender * (libro3["precio"] - libro3["costoProduccion"])
        if (0.25 * libro3["cantidad"]) < cant_vender < (0.5 * libro3["cantidad"]):
            descuento = 0.1 * ganancia
        elif (0.5 * libro3["cantidad"]) < cant_vender < (0.75 * libro3["cantidad"]):
            descuento = 0.2 * ganancia
        elif cant_vender > (0.75 * libro3["cantidad"]):
            descuento = 0.3 * ganancia
    elif nom_lib == libro4["nombre"]:
        ganancia = cant_vender * (libro4["precio"] - libro4["costoProduccion"])
        if (0.25 * libro4["cantidad"]) < cant_vender < (0.5 * libro4["cantidad"]):
            descuento = 0.1 * ganancia
        elif (0.5 * libro4["cantidad"]) < cant_vender < (0.75 * libro4["cantidad"]):
            descuento = 0.2 * ganancia
        elif cant_vender > (0.75 * libro4["cantidad"]):
            descuento = 0.3 * ganancia
    # else:
    # return "No tenemos ese libro"
    return venta_por_mayor


# PROGRAMA PRINCIPAL
libro1 = crear_libro("Harry Potter y la piedra filosofal", "HPJK1997", "J.K. Rowling", 1997, 200, 25000, 9000)
libro2 = crear_libro("Los Juegos del Hambre", "JHSC2008", "Suzanne Collins", 2008, 100, 27000, 12000)
libro3 = crear_libro("El Hobbit", "EHJR1937", "J.R.R tolkien", 1937, 50, 35000, 15000)
libro4 = crear_libro("Hamlet", "HWS1589", "William Shakespeare", 1589, 20, 26000, 13000)

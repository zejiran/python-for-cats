# -*- coding: utf-8 -*-
"""
@author: alxus27
"""


def cargar_automovil(ruta_archivo: str) -> list:
    # Lista vacía y carga de archivo.
    automoviles = []
    archivo = open(ruta_archivo, "r")
    # Omitir línea de títulos.
    archivo.readline()
    # Agregar datos a lista.
    linea = archivo.readline()
    while len(linea) > 0:
        datos = linea.split(";")
        auto = {'registro': datos[0], 'antiguedad': datos[1], 'clase': datos[2],
                'departamento': datos[3], 'marca': datos[4], 'servicio': datos[5].replace("\n", '')}
        automoviles.append(auto)
        linea = archivo.readline()
    # Cierre de archivo.
    archivo.close()
    return automoviles


def cantidad_marca_departamento(automoviles: list, departamento: str) -> None:
    # Carga de archivo y diccionario vacío para añadir cantidad de autos por marca.
    reporte = open('reporte.txt', "w")
    autos_por_marca = dict()
    # Buscar autos en departamento y sumar cantidad por marca.
    for auto in automoviles:
        if departamento == auto['departamento']:
            cantidad = autos_por_marca.get(auto['marca'], 0)
            autos_por_marca[auto['marca']] = cantidad + 1
    # Escritura de archivo
    reporte.write('Cantidad de vehículos por marca en el departamento ' + departamento + '\n')
    reporte.write('----------------------------------\n')
    for marca in autos_por_marca:
        reporte.write(marca.capitalize() + ": " + str(autos_por_marca[marca]) + "\n")
    reporte.write('----------------------------------\n')
    reporte.close()

# Línea para probar las funciones.
# cantidad_marca_departamento(cargar_automovil('./Parque_Automotor_2017.csv'), 'Valle del Cauca')


def clase_mas_comun(lista: list) -> str:
    dicc_clases = {}
    mayor_numerico = 0
    mas_comun = ""
    for datos in lista:
        clase = datos["clase"]
        if clase not in dicc_clases:
            dicc_clases[clase] = 0
        dicc_clases[clase] += 1
        if dicc_clases[clase] > mayor_numerico:
            mayor_numerico = dicc_clases[clase]
            mas_comun = clase
    return mas_comun


def depto_menos_camiones(carros: list) -> str:
    # dict {'departamento': 0}.
    camiones_depto = dict()
    # Contadores.
    menor_cantidad = -1
    depto_menos = ""
    # Recorrido.
    for carro in carros:
        departamento = carro['departamento']
        clase = carro['clase']
        # Añadir número de camiones en el departamento al diccionario.
        if departamento not in camiones_depto and clase == 'CAMIONETA':
            camiones_depto[departamento] = 0
        if clase == 'CAMIONETA':
            camiones_depto[departamento] += 1
    for depto in camiones_depto:
        if camiones_depto[depto] >= menor_cantidad or camiones_depto == -1:
            depto_menos = depto
            menor_cantidad = camiones_depto[depto]
    return depto_menos


def cant_servicio_por_depto(carros: list) -> dict:
    depto = {}
    for cada_carro in carros:
        departamento = cada_carro["depto"]
        servicio = cada_carro["servicio"]
        servicios_depto = depto.get(departamento, {})
        if servicio not in servicios_depto:
            servicios_depto[servicio] = 1
        else:
            servicios_depto[servicio] += 1
        depto[departamento] = servicios_depto
    return depto

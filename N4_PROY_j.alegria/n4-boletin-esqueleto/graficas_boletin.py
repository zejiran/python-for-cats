# -*- coding: utf-8 -*-
"""
Ejercicio nivel 4: Boletin Estadistico
Consola de Visualizacion.

Temas:
* Recorridos de Matrices.
* Librerias de Matplotlib.
@author: Cupi2


"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import boletin as be

def mostrar_menu():
    """Imprime las opciones de ejecucion disponibles para el usuario."""
    
    print("\nOpciones")
    print("1. Cargar archivos")
    print("2. Graficar los 5 dobles programas mas comunes de un programa")
    print("3. Graficar el histograma de autocubrimiento")
    print("4. Graficar las estadisticas del PGA")
    print("5. Graficar la poblacion de profesores")
    print("6. Graficar la distribucion de estudiantes")
    print("7. Salir de la aplicacion")
    
def ejecutar_cargar_matriz_dobles() -> list:
    """Solicita al usuario que ingrese el nombre de un archivo CSV con los datos de
    la matriz de dobles programas y la carga.
    Retorno: list
        La matriz de los dobles programas entre las carreras.
    """
    dobles = list()
    archivo = input("Por favor ingrese el nombre del archivo CSV con la matriz de dobles programas: ")

    #TODO llame a la funcion que usted mismo implemento para cargar la matriz de dobles programas
    #Guarde el retorno en una variable llamada dobles

    if len(dobles) == 0:
        print("El archivo seleccionado no es valido. No se pudo cargar la matriz de dobles programas")
    else:
        print("Se cargo la matriz de las dobles programas")
    return dobles 

def ejecutar_cargar_matriz_estadisticas() -> list:
    """Solicita al usuario que ingrese el nombre de un archivo CSV con los datos de
    la matriz estadisticas de facultades y la carga.
    Retorno: list
        La matriz de estadisticas de las facultades.
    """
    estadisticas = list()
    archivo = input("Por favor ingrese el nombre del archivo CSV con la matriz de estadisticas: ")
    estadisticas = be.cargar_matriz_estadisticas(archivo)
    if len(estadisticas) == 0:
        print("El archivo seleccionado no es valido. No se pudo cargar la matriz de estadisticas")
    else:
        print("Se cargo la matriz de estadisticas")
    return estadisticas    

def ejecutar_cargar_matriz_puestos() -> list:
    """Solicita al usuario que ingrese el nombre de un archivo CSV con los datos de
    la matriz de los puestos estudiante.
    Retorno: list
        La matriz de los puestos estudiante.
    """
    puestos = list()
    archivo = input("Por favor ingrese el nombre del archivo CSV con la matriz de los puestos estudiante: ")
 
    puestos = be.cargar_matriz_puestos(archivo)

    if len(puestos) == 0:
        print("El archivo seleccionado no es valido. No se pudo cargar la matriz de puestos estudiante")
    else:
        print("Se cargo la matriz de puestos estudiante")
    return puestos     

 
def graf_1(dobles:list) -> None:
    """En esta funcion se utiliza el diccionario de los dobles
    de un programa, para armar una grafica que muestre los dobles
    programas mas comunes de un programa dado
    """
    programa = input('Ingrese el programa a consultar: ')
    dc = {}

    #TODO llame a la funcion 7 que usted mismo implemento (la que retorna todos los 
    #programas dobles de un programa dado)
    #Guarde el retorno en una variable llamada dc
    
    if len(dc)>0:
        #En primer lugar convertimos el diccionario a DataFrame de Pandas
        df = pd.DataFrame(dc,index=['Estudiantes'])
        df = df.transpose()
        #Ahora lo filtramos para que solo nos queden los 5 de mayor numero
        df = df.sort_values(by='Estudiantes',ascending=False)
        df = df.head(5)
        #Luego procedemos a crear la grafica de barras
        plt.figure()
        ax = df.plot.bar()
        #Se ponen los titulos de la grafica
        plt.title("Doble Carrera mas comun para "+programa,fontsize=13)
        plt.xlabel("Carrera")
        plt.ylabel("Numero de Estudiantes")
        #Este ciclo permite poner el numero de cada barra
        for p in ax.patches: 
            ax.annotate(round(p.get_height(),2), (p.get_x()+p.get_width()/2., p.get_height()), ha='center', va='center', xytext=(0, 5), textcoords='offset points')
        #La grafica del programa se guarda en un archivo png
        plt.savefig('graficas/'+programa+'.png',bbox_inches='tight')
        #Esta grafica nos muestra de manera facil los 5 programas que mas aparecen
        #como doble programa para el programa escogido en cuestion
        print("La grafica de",programa,"se ha guardado en la carpeta de \"graficas\"")
    else:
        print("No se ha encontrado este programa")
 
       
def graf_2(puestos:list,estadisticas:list)->None:
    """En esta funcion se utiliza la columna calculada de autocubrimiento
    de cada facultad, para construir un histograma que lo represente.
    """
    m = []
    #TODO llame a la funcion 5 que usted miso implementó (la que añade la columna de porcentaje de autocubrimiento)
    #Guarde el retorno en una variable llamada m 
    
    if len(m)>0:
        #Construimos un diccionario con esta columna y los nombres
        #de cada facultad
        dc = {}
        for i in range(1,len(estadisticas)):
            fila = estadisticas[i]
            dc[fila[0]] = fila[-1]        
        #Convertimos el diccionario a DataFrame de Pandas
        df = pd.DataFrame(dc,index=['Cubrimiento'])
        df = df.transpose()
        #Con esto creamos una grafica de tipo histograma
        #El xlim nos permite delimitar el rango de la grafica
        plt.figure()
        df.plot.hist(bins=5)
        plt.xlim(0,100)
        #Se ponen los titulos de la grafica
        plt.title("Distribucion de autocubrimiento de puestos",size=13)
        plt.xlabel("Porcentaje autocubrimiento")
        plt.ylabel("Numero de Facultades")
        #La grafica de las facultades se guarda en un archivo png
        plt.savefig('graficas/cubrimiento.png',bbox_inches='tight')
        print("La grafica de cubrimiento se ha guardado en la carpeta de \"graficas\"")
    else:
        print("No se ha cargado la matriz")
        
def graf_3(estadisticas:list)->None:
    """En esta funcion se utilizan las estadisticas del PGA de las facultades
    para representar la distribucion de los mismos.
    """
    l=[]
    #TODO llame a la funcion 8 que usted mismo implementó (la que obtiene las estadisticas del PGA)
    #Guarde el retorno en una variable llamada l
    
    if len(l)>0:
        #Primero extraemos todos los demas PGAs, pues los utilizaremos
        #para la graficas
        pgas = []
        for i in range(1,len(estadisticas)):
            fila = estadisticas[i]
            pgas.append(float(fila[6]))
        #Ordenamos los pgas
        pgas.sort()
        #Con esto creamos una grafica de linea sencilla, que mostrara los
        #PGAs de todas las carreras
        plt.figure()
        plt.plot(pgas)
        #Procedemos a poner como puntos el mayor, el menor y la mediana
        puntos = [l[0][1],l[1][1],l[2][1]]
        ubicacion = [10,0,5]
        plt.plot(ubicacion,puntos,"ro")
        #Ponemos los nombres de las facultades extremo en los puntos que 
        #corresponden, las sumas y restas responden a ajustes visuales para 
        #que se puedan leer mejor los titulos
        plt.text(ubicacion[0]-2.5, puntos[0]-0.02, l[0][0])
        plt.text(ubicacion[1]-0.2, puntos[1]+0.02, l[1][0])
        #Se ponen los titulos de la grafica
        plt.title("PGAs de las Facultades",size=13)
        plt.ylabel("PGA")
        #La grafica de las facultades se guarda en un archivo png
        plt.savefig('graficas/pga.png',bbox_inches='tight')
        print("La grafica de estadisticas del PGA se ha guardado en la carpeta de \"graficas\"")
    else:
        print("No se ha cargado la matriz")
        

def graf_4(estadisticas:list)->None:
    """En esta funcion se utiliza la matriz de estadisticas
    para construir un diagrama que muestre la distribucion de 
    la poblacion de profesores por genero
    """

    if len(estadisticas)>0:
        #Extraemos las estadisticas de poblacion de profesores de cada facultad
        hombres = []
        mujeres = []
        titulos = []
        for i in range(1,len(estadisticas)):
            fila = estadisticas[i]
            titulos.append(fila[0])
            hombres.append(int(fila[1]))
            mujeres.append(int(fila[2]))
        #Con esto creamos una grafica de barras apiladas sobre la otra
        plt.figure()
        width = 0.6 
        ind = np.arange(len(hombres))  
        p1=plt.bar(ind,hombres, width,color='lightskyblue')
        p2=plt.bar(ind, mujeres, width,color='lightcoral',
             bottom=hombres)
        #Se ponen los titulos de la grafica
        plt.title("Distribucion de Profesores por genero y facultad",size=13)
        plt.xlabel("Facultades")
        plt.ylabel("Numero de Profesores")
        plt.xticks(ind, titulos,rotation=90)
        plt.legend((p1[0], p2[0]), ('Hombres', 'Mujeres'))
        #La grafica de las facultades se guarda en un archivo png
        plt.savefig('graficas/profesores.png',bbox_inches='tight')
        print("La grafica de poblacion de profesores se ha guardado en la carpeta de \"graficas\"")
    else:
        print("No se ha cargado la matriz")
        
def graf_5(estadisticas:list)->None:
    """En esta funcion se utiliza la matriz de estadisticas
    para construir un diagrama que muestre la distribucion de 
    la poblacion estudiantil
    """

    if len(estadisticas)>0:
        #Primero construimos una lista con los valores de poblacion estudiantil
        # y otra con los nombres de las facultades
        estudiantes = []
        facultades = []
        #Estos parametros nos permitiran cambiar el color y la apariencia de la
        #grafica
        explode = []
        colors = ['#1b77b0','#7eb704','#8c0045','#f25b04']
        #Este ciclo nos permite llenar las listas de la informacion que necesitamos
        for i in range(1,len(estadisticas)):
            fila = estadisticas[i]
            facultades.append(fila[0])
            estudiantes.append(int(fila[3])+int(fila[4]))
            explode.append(0.1)
        #Con esto creamos un diagrama de pastel, con la informacion recolectada
        plt.figure()
        plt.pie(estudiantes,labels=facultades,explode=explode,colors=colors)
        #Se ponen los titulos de la grafica
        plt.title("Distribucion de estudiantes por facultad",size=13)
        #La grafica de las facultades se guarda en un archivo png
        plt.savefig('graficas/estudiantes.png',bbox_inches='tight')
        print("La grafica de poblacion de estudiantes se ha guardado en la carpeta de \"graficas\"")
    else:
        print("No se ha cargado la matriz")
	
def iniciar_aplicacion():
    """Ejecuta el programa para el usuario."""
    continuar = True
    dobles = list()
    estadisticas = list()
    puestos = list()
    while continuar:
        mostrar_menu()
        opcion_seleccionada = input("Por favor seleccione una opcion: ")
        if opcion_seleccionada == "1":
            dobles=ejecutar_cargar_matriz_dobles()
            estadisticas=ejecutar_cargar_matriz_estadisticas()
            puestos=ejecutar_cargar_matriz_puestos()
        elif opcion_seleccionada == "2":
            graf_1(dobles)
        elif opcion_seleccionada == "3":
            graf_2(puestos,estadisticas)
        elif opcion_seleccionada == "4":
            graf_3(estadisticas)      
        elif opcion_seleccionada == "5":
            graf_4(estadisticas)  
        elif opcion_seleccionada == "6":
            graf_5(estadisticas)  
        elif opcion_seleccionada == "7":
            continuar = False
        else:
            print("Por favor seleccione una opcion valida.")

#PROGRAMA PRINCIPAL
iniciar_aplicacion()
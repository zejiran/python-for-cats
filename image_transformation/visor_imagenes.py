# -*- coding: utf-8 -*-
"""
Ejemplo Nivel 4: Visor de imágenes

Temas:

* Matrices

@author: zejiran
"""
import matplotlib.image as mpimg
import matplotlib.pyplot as plt


def cargar_imagen(ruta_imagen: str) -> list:
    """ Carga la imagen que se encuentra en la ruta dada.
    Parámetros:
        ruta_imagen (str) Ruta donde se encuentra la imagen a cargar.
    Retorno:
        list: Matriz (M,N,3) con la imagen cargada.
    """
    imagen = mpimg.imread(ruta_imagen).tolist()
    return imagen


def visualizar_imagen(imagen: list) -> None:
    """ Muestra la imagen recibida
    Parámetros:
        imagen (list) Matriz (M,N,3) con la imagen a visualizar.
    """
    plt.imshow(imagen)
    plt.show()


def convertir_negativo(imagen: list) -> list:
    """  Convierte la imagen en negativo.
    El negativo se calcula cambiando cada componente RGB, tomando el valor absoluto de restarle al componente 1.0.
    Parámetros:
        imagen (list) Matriz (M,N,3) con la imagen a convertir a negativo.
    """
    alto = len(imagen)
    ancho = len(imagen[0])

    for i in range(alto):
        for j in range(ancho):
            for k in range(3):
                nuevo = abs(imagen[i][j][k] - 1)
                imagen[i][j][k] = nuevo
    return imagen


def reflejar_imagen(imagen: list) -> list:
    """  Refleja la imagen.
    Consiste en intercambiar las columnas enteras de la imagen, de las finales a la iniciales.
    Parámetros:
        imagen (list) Matriz (M,N,3) con la imagen a reflejar.
    """
    alto = len(imagen)
    ancho = len(imagen[0])

    for i in range(alto):
        for j in range(int(ancho / 2)):
            temp = imagen[i][j]
            imagen[i][j] = imagen[i][-j - 1]
            imagen[i][-j - 1] = temp
    return imagen


def binarizar_imagen(imagen: list, umbral: float) -> list:
    """ Binariza la imagen.
    Consiste en llevar cada pixel de una imagen a negro o blanco.
    Para ello se requiere un umbral: si el promedio de los componentes RGB del pixel está por
    encima o igual se lleva a blanco y si está por debajo se lleva a negro.
    Parámetros:
        imagen (list) Matriz (M,N,3) con la imagen a binarizar.
        umbral (float) Umbral de la binarización.
     """
    alto = len(imagen)
    ancho = len(imagen[0])

    for i in range(alto):
        for j in range(ancho):
            promedio_pixel = 0
            for k in range(3):
                promedio_pixel += imagen[i][j][k]
            promedio_pixel /= 3
            if promedio_pixel >= umbral:
                imagen[i][j] = [255, 255, 255]
            else:
                imagen[i][j] = [0, 0, 0]
    return imagen


def convertir_a_grises(imagen: list) -> list:
    """ Convierte la imagen a escala de grises.
    Para ello promedia los componentes de cada pixel y crea un nuevo color donde cada componente (RGB) tiene el valor de dicho promedio.
    Parámetros:
        imagen (list) Matriz (M,N,3) con la imagen a convertir a grises.
    """
    return imagen


def convolucion_imagen(imagen: list) -> list:
    """ Opera la imagen con la matriz de convolución dada por el usuario.
    Parámetros:
        imagen (list) Matriz (M,N,3) con la imagen a convolucionar.
    """

    convolucion = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    return imagen

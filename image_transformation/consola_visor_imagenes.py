# -*- coding: utf-8 -*-
"""
Ejemplo Nivel 4: Visor de imágenes

Temas:

* Matrices

@author: zejiran
"""
import visor_imagenes


def imprimir_menu_principal():
    # Imprime los items del menú principal de la aplicación.
    print("\nVisor de imágenes\n")
    print("(1) Cargar imagen")
    print("(2) Negativo")
    print("(3) Reflejar")
    print("(4) Binarizar")
    print("(5) Escala de grises")
    print("(6) Convolución")
    print("(7) Salir")


def cargar_imagen() -> list:
    # Muestra las opciones para cargar una imagen y carga la imagen seleccionada por el usuario.
    ruta = input("Ingrese el nombre del archivo que contiene la imagen: ")
    image = visor_imagenes.cargar_imagen(ruta)
    visor_imagenes.visualizar_imagen(image)
    return image


def ejecutar_binarizar_imagen(image: list) -> list:
    """ Pide al usuario el umbral deseado y binariza la imagen recibida por parámetro.
    Parámetros:
        imagen (list) Matriz (M,N,3) con la imagen a binarizar.
    """
    umbral = float(input("Ingrese el umbral (valor entre 0 y 1):"))
    print("Calculando imagen...")
    image = visor_imagenes.binarizar_imagen(image, umbral)
    visor_imagenes.visualizar_imagen(image)
    return image


def ejecutar_convolucionar_imagen(image: list) -> list:
    """ Aplica la convolución a la imagen recibida por parámetro.
    Parámetros:
        imagen (list) Matriz (M,N,3) con la imagen a convolucionar.
    """
    print("Calculando imagen...")
    image = visor_imagenes.convolucion_imagen(image)

    visor_imagenes.visualizar_imagen(image)
    return image


def ejecutar_convertir_negativo(image: list) -> list:
    print("Calculando imagen...")
    image = visor_imagenes.convertir_negativo(image)
    visor_imagenes.visualizar_imagen(image)
    return image


def ejecutar_reflejar_imagen(image: list) -> list:
    print("Calculando imagen...")
    image = visor_imagenes.reflejar_imagen(image)
    visor_imagenes.visualizar_imagen(image)
    return image


def ejecutar_convertir_a_grises(image: list) -> list:
    print("Calculando imagen...")
    image = visor_imagenes.convertir_a_grises(image)
    visor_imagenes.visualizar_imagen(image)
    return image


salir = False
while not salir:
    imprimir_menu_principal()
    opcion = int(input("Ingrese la opción deseada: "))

    if opcion == 1:
        image = cargar_imagen()
    elif opcion == 2:
        image = ejecutar_convertir_negativo(image)
    elif opcion == 3:
        image = ejecutar_reflejar_imagen(image)
    elif opcion == 4:
        image = ejecutar_binarizar_imagen(image)
    elif opcion == 5:
        image = ejecutar_convertir_a_grises(image)
    elif opcion == 6:
        image = ejecutar_convolucionar_imagen(image)
    elif opcion == 7:
        salir = True
    else:
        print("El valor ingresado no es válido.")

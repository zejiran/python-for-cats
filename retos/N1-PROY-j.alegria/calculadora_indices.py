# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 10:49:23 2020

@author: j.alegria
"""


def calcular_IMC(peso: float, altura: float) -> float:
    """ Calcula el índice de masa corporal de una persona a partir de la ecuación definida anteriormente.
    Parámetros:
        peso (float) Peso de la persona en kg. Número decimal positivo.
        altura (float) Altura de la persona en m. Número decimal positivo.
    Retorno:
        float: Índice de masa corporal redondeado a dos decimales.
    """

    imc = peso * (altura ** 2)

    return imc


def calcular_porcentaje_grasa(imc: float, edad: int, valor_genero: float) -> float:
    """ Calcula el porcentaje de grasa corporal.
    Parámetros:
        imc (float) Índice de masa corporal redondeado a dos decimales.
        edad (float) Edad de la persona en años. Número entero positivo.
        valor_genero (float) Masculino 10.8. Femenino 0. Decimal
    Retorno:
        float: Porcentaje de grasa corporal. Número dividido entre 100 al ser un porcentaje.
    """

    pgc = (1.2 * imc) + (0.23 * edad) - 5.4 - valor_genero

    return pgc


def calcular_calorias_en_reposo(peso: float, altura: float, edad: int, valor_genero: float) -> float:
    """ Calcula la cantidad de calorías que una persona quema estando en reposo 
        (esto es, su tasa metabólica basal), a partir 
        de la ecuación definida anteriormente. 
    Parámetros:
        peso (float) Peso de la persona en kg. Decimal
        altura (float) Altura de la persona en cm. Número decimal positivo
        edad (int) Edad de la persona en años. Número entero positivo.
        valor_genero (float) Masculino 5. Femenino -161. Número entero.
    Retorno:
        float: Tasa metabólica. La cantidad de calorías que la persona quema en reposo.
    """

    tmb = (10 * peso) + (6.25 * altura) - (5 * edad) + valor_genero

    return tmb


def calcular_calorias_en_actividad(tmb: float, valor_actividad: float) -> float:
    """ Calcula la tasa metabólica basal según la actividad física.
    Parámetros:
        tmb (float) Tasa metabolica entera. Número de calorías necesarias para vivir.
        valor_actividad (float) Número de acuerdo a lo siguiente:
            1.2: poco o ningún ejercicio 
            1.375: ejercicio ligero (1 a 3 días a la semana) 
            1.55: ejercicio moderado (3 a 5 días a la semana) 
            1.72: deportista (6 -7 días a la semana) 
            1.9: atleta (entrenamientos mañana y tarde) 
    Retorno:
       float: Tasa metabólica según actividad física. La cantidad de calorías 
       que una persona quema, al realizar algún tipo de actividad física semanalmente.
    """

    tmbsaf = tmb * valor_actividad

    return tmbsaf


def consumo_calorias_recomendado_para_adelgazar(tmb: float) -> str:
    """ Calcula el rango de calorías recomendado, que debe consumir una persona 
    diariamente en caso de que desee adelgazar, a partir de la ecuación definida 
    anteriormente. 
    Parámetros:
        tmb (float) Tasa metabolica. Número de calorías necesarias para vivir.
    Retorno:
        str: Una cadena indicando el rango de calorías que una persona 
        debe consumir si desea adelgazar. 
        El formato de la cadena debe ser:  "Para adelgazar es recomendado que 
        consumas entre: XXX y ZZZ calorías al día.". Siendo XXX el rango 
        inferior y ZZZ el rango superior.
    """

    adelgazo_inferior = tmb * 0.8
    adelgazo_superior = tmb * 0.85
    calorias_adelgazo = ["Para adelgazar es recomendado que consumas entre:", str(round(adelgazo_inferior, 2)), "y", str(round(adelgazo_superior, 2)), "calorías al día."]

    return calorias_adelgazo

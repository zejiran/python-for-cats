# -*- coding: utf-8 -*-
"""
@author: zejiran

En la isla del Edén vive una gran cantidad de hormigas
que se reproducen a una tasa del 40% mensual; en la isla
existe además un oso hormiguero que se come 7000 hormigas
al final de cada mes (o todas las hormigas que haya, si es que hay menos de 7000).
Cuando la población de hormigas de la isla sobrepasa el máximo de 28000,
comienza a haber problemas de alimentación, lo que hace que se reduzca
la tasa de crecimiento al 31% mensual. El muestreo de la población se hace mensualmente.
Escriba una función que reciba como parámetro el número de hormigas que hay en un momento
dado en la isla y un número X, y calcule la población de hormigas después de esos X meses.
"""


def hormigas(numero_hormigas: int, meses: int) -> int:
    iteraciones = 0
    print("Número de hormigas inicial: " + str(numero_hormigas))
    # Inicio del ciclo
    while meses > iteraciones and numero_hormigas > 0:
        # Tasa de crecimiento
        if numero_hormigas >= 28000:
            crecimiento = 0.31
        else:
            crecimiento = 0.40
        # Reproducción de las hormigas
        numero_hormigas += numero_hormigas * crecimiento
        # Oso hormiguero
        if numero_hormigas <= 7000:
            numero_hormigas = 0
        else:
            numero_hormigas -= 7000
        # Centinela
        iteraciones += 1
        # Print de la cantidad en cada mes que pasa
        print("Luego del mes {0} hay {1} hormigas".format(iteraciones, int(numero_hormigas)))
    return numero_hormigas


hormigas(2120000, 2000)

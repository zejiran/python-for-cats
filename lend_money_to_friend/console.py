# -*- coding: utf-8 -*-
"""
@author: zejiran.
"""

import friend_module as md


def iniciar_aplicacion() -> None:
    amigo1 = md.crear_amigo("Juan", 2010, False, 100000, 135000, 0, False, True, 1)
    amigo2 = md.crear_amigo("Jsuan", 2010, False, 100000, 100000, 0, False, True, 1)
    amigo3 = md.crear_amigo("Jauan", 2010, False, 100000, 100000, 0, False, True, 0)
    amigo4 = md.crear_amigo("Juaan", 2010, False, 100000, 100000, 0, False, True, 0)
    print(md.diccionario_final(amigo1, amigo2, amigo3, amigo4))


iniciar_aplicacion()

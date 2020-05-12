# -*- coding: utf-8 -*-
"""
@author: zejiran
"""


def es_primo_o_no(x: int) -> bool:
    primo = True
    for i in range(2, x):
        if x % i == 0:
            primo = False
    print(primo)
    return primo


es_primo_o_no(1028)

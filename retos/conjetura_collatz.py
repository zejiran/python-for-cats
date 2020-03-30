# -*- coding: utf-8 -*-
"""
@author: alxus27
"""

import random


def collatz() -> None:
    x = random.randint(0, 10000)
    while x != 1:
        if x % 2 == 0:
            x /= 2
        else:
            x = (x * 3) + 1
        print(x)


collatz()

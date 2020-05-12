# -*- coding: utf-8 -*-
"""
@author: zejiran
"""

# Programa para calcular el costo de la orden realizada en un restaurante

# Preguntar al usuario su valor de compra bruto

# Salto de línea
print("")

# Saludo
print("¡Hola! A continuación, procederemos a calcular el total de su compra incluyendo su IVA y propina.")
bruto = float(input("¿Cuál es el valor de su compra en bruto? "))

# Cálculo de IVA y propina

iva = bruto * 0.08
propina = bruto * 0.1

# Suma valores

total = round(bruto + iva + propina, 2)

# Salto de línea
print("")

# Muestra del gran total

print("Para la compra realizada," +
      " el valor que corresponde al IVA es de", str(round(iva, 2)), "pesos" +
      " y la propina es de", str(round(propina, 2)), "para" +
      " un gran total de", str(total), "pesos")

# Fin

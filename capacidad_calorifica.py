# Programa para calcular la energía necesaria para cambiar la temperatura de una masa de agua

### Salto de línea
print("")
###

# Recibir masa de agua y cambio de temperatura deseado
print("¡Hola! Ahora, vamos a calcular la energía necesaria para cambiar la temperatura de una masa de agua")

masa_agua = float(input("¿Cuál es la masa de agua en gramos? "))

### Salto de línea
print("")
###

cambio_temperatura = float(input("¿Cuál es el cambio de temperatura deseado en Celsius? "))

### Salto de línea
print("")
###

# Definimos la capacidad calorífica del material
capacidad_calorifica = 4.186

# Cálculo de energía
energia = masa_agua * capacidad_calorifica * cambio_temperatura

# Redondeo resultado y conversión a string
energia = str(round(energia, 2))

# Muestra del resultado
print("Para realizar lo deseado, necesitas agregar", energia,"Joules. Si esta respuesta tiene signo negativo, significa que se deberá remover energía")

# Segunda fase del programa
energia = masa_agua * capacidad_calorifica * cambio_temperatura

### Salto de línea
print("")
###

# Conversión Joules a Kilowatt
energia_kilowatt = energia / 3600000

# Cálculo de costo
costo = energia_kilowatt * 8.9

# Redondeo resultado y conversión a string
costo = str(round(costo, 7))

print("Por último, el costo de calentar agua es " + costo + " centavos.")

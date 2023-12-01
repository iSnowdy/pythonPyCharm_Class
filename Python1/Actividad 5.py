# Actividad 5 - Cargamos la librería Math para tener el valor exacto de pi. Pidiendo el radio de un círculo, calcule el área de este. Muestre por pantalla el resultado.

from math import pi
print(pi)

r = float(input('Inserte el radio del círculo: '))
print('Una vez sabemos el radio, procederemos a calcular el área de un círculo')

A = pi * r**2
print('El área del círculo con radio', r, 'es', A)

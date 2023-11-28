# Actividad 21 - Escribir un programa que pregunte si se quiere calcular el área de un círculo o de un
# triángulo. En base a lo que se conteste, se piden las variables correspondientes para calcular el área.

from math import pi
print(pi)

base_T = 0
altura_T = 0
A_T = 0
r_C = 0
A_C = 0

if str(input('Seleccione el cálculo del área de la siguiente figura geométrica:'
             ' \nA) Triángulo \nB) Círculo \nEscriba A o B')) == 'A':
    base_T = float(input('Dígame la base del triángulo del que desea calcular el área: '))
    altura_T = float(input('Dígamo la altura del triángulo del que desea calcular el área: '))
    A_T = (base_T * altura_T)/2
    print('El área de su triángulo es', A_T)
else:
    r_C = float(input('Dígame el radio del círculo del que desea calcular el área: '))
    A_C = pi * r_C**2
    print('El área de su círculo es', A_C)

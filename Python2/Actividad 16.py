# Actividad 16 - Escribir un programa que pida dos números enteros y que calcule su división.
# También queremos saber si la división es exacta o no.

dividendo = 0
divisior = 0
cociente = 0
resto = 0

print('Para calcular una división necesitamos el dividendo y el divisor. Por favor, introdúzcalos continuación')

dividendo = int(input('Dividendo (número entero): '))
divisor = int(input('Divisor (número entero): '))

cociente = dividendo/divisor
resto = dividendo % divisor

if dividendo % divisor == 0:
    print('La división es exacta. El cociente es', cociente)

else:
    print('Su división no es exacta. El cociente es', cociente, 'con resto', resto)


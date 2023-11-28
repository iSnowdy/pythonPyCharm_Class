# Actividad 20 - Escribir un programa y que imprima por pantalla si es bisiesto o no.

año = 0

año = int(input('Introduzca un año y le diré si es bisiesto o no: '))

if año % 100 == 0 and año % 400 == 0:
    print('Su año es bisiesto')

else:
    print('Su año no es bisiesto')
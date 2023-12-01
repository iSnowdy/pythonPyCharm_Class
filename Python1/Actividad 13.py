# Actividad 13 - Pediremos un número al usuario. Vemos si este número es par o impar y dependiendo de lo que sea lo mostramos en pantalla.

número = 0
comprobar = 0

número = float(input('Introduzca un número: '))
comprobar = número % 2

if comprobar == 0:
    print('Su número es par')

else:
    print('Su número es impar')

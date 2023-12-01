# Actividad 17 - Escribir un programa que pida dos números. Queremos saber cuál es el menor y cuál
# es el mayor o si son iguales.

número_1 = 0
número_2 = 0

número_1 = float(input('Por favor introduzca un número: '))
número_2 = float(input('Por favor introduzca un segundo número: '))

if número_1 != número_2:
    print('Sus números son diferentes. Procederemos a ver cuál es el mayor y cuál el menor')

else:
    print('Sus números son iguales')

if número_1 > número_2:
    print('El mayor es', número_1, 'y el menor es', número_2)

if número_1 < número_2:
    print('El mayor es ', número_2, 'y el menor es', número_1)



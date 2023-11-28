# Actividad 18 - Escribir un programa que pida dos números enteros. Queremos saber si el mayor es
# múltiple del menor.

número_1 = 0
número_2 = 0
t = 0

número_1 = int(input('Por favor introduzca un número: '))
número_2 = int(input('Introduzca un segundo número: '))

if número_2 > número_1:
    t = número_1
    número_1 = número_2
    número_2 = t

if número_1 % número_2 == 0:
    print(número_1, 'es múltiplo de ', número_2)
else:
    print(número_1, 'no es múltiplo de', número_2)
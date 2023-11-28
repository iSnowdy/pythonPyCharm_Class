# Actividad 19 - Escribir un programa que pida 3 números. Queremos saber si: (1) los tres son iguales
# , (2) si hay dos diferentes o (3) si los tres son diferentes.

número_1 = 0
número_2 = 0
número_3 = 0

número_1 = float(input('Por favor introduzca un número: '))
número_2 = float(input('Por favor introduzca un segundo número: '))
número_3 = float(input('Por favor introduzca un tercer número: '))

if número_1 == número_2 == número_3:
    print('Sus tres números son iguales')

elif número_1 != número_2 != número_3:
    print('Los tres números son diferentes')

elif número_1 != número_2 == número_3:
    print('Dos de sus números son iguales')

elif número_1 == número_2 != número_3:
    print('Dos de sus números son iguales')

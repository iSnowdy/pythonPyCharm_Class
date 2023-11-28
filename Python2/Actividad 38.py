# Actividad 38 - Escribir un programa que pida 2 valores y muestre la suma desde el primero hasta el segundo.

número_1 = 0
número_2 = 0
número_3 = 0
i = 0

número_1 = int(input('Escriba un número: '))
número_2 = int(input(f'Escriba un número mayor que {número_1} :'))


while número_1 > número_2:
    número_2 = int(input(f'Error. Ha de introducir un número mayor que {número_1} :'))

for i in range(número_1, número_2+1):
    número_3 = i + número_3

print('La suma desde', número_1, 'a', número_2, 'es:', número_3)
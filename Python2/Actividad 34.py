# Actividad 34 - Escribir un programa que te pida dos números. Generar una lista de
# números consecutivos que hay entre esos dos números. Ordenarla de menor a mayor.

número_1 = 0
número_2 = 0

lista = []

número_1 = int(input('Dígame un número: '))
número_2 = int(input('Dígame un segundo número cualquiera: '))
print(f'A continuación crearemos una lista que comprenda los números entre {número_1} y {número_2} ordenados de menor a '
      f'mayor')

if número_1 < número_2:
    lista = list(range(número_1+1, número_2, 1))

if número_2 < número_1:
    lista = list(range(número_2+1, número_1, 1))

print(lista)

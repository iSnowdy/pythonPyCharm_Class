# Actividad 31 - Escribir un programa que te pida un número y escriba una lista
# de números consecutivos del 0 al valor dado:

número = 0
lista = []

número = int(input('Dígamo un número: '))

if número > 0:  # En función de si el número es positivo o negativo el incremento será de una forma u otra.
    lista = list(range(0, número+1, 1))
else:
    lista = list(range(0, número-1, -1))

print(lista)

# Actividad 35 - Escribir un programa que pida dos números. El primer número será el valor
# inicial y el segundo la cantidad de valores de la lista.

valor_inicial = 0
tamaño = 0

lista = []

valor_inicial = int(input('Dígame el valor inicial de la lista de números que desea: '))
tamaño = int(input('¿Cuántos números quiere que tenga la lista? '))

if 0 > tamaño:
    tamaño = int(input('Por favor, introduzca un número mayor que 0: '))

lista = list(range(valor_inicial, tamaño+valor_inicial, 1))
print(lista)

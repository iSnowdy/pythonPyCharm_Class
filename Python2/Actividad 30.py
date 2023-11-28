# Actividad 30 - Escribir un programa que te pida un número positivo. Luego, queremos
# que se creen diversas listas de números consecutivos.

número = 0
lista = []


número = int(input('Dígame un número positivo: '))
while 0 > número:
    número = int(input('Ha de ser un número positivo. Inténtelo nuevamente: '))

lista = list(range(0, número+1, 1))
print(lista)

lista = list(range(número, -1, -1))
print(lista)

lista = list(range(1, número, +1))
print(lista)

lista = list(range(número-1, 0, -1))
print(lista)

lista = list(range(0, número+1, 1)) + list(range(número-1, -1, -1))
print(lista)

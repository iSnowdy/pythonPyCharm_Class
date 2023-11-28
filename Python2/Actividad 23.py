# Actividad 23 - Escribe un programa que te pida números y los guarde en una lista. Para que pare de
# introducir números, introduzca un 0. Finalmente imprima una lista de números.

lista = []
número = 0
número = float(input('Introduzca un número. Si quiere detener la lista, introduzca 0: '))

while número != 0:
    lista.append(número)
    número = float(input('Introduzca un número. Si quiere detener la lista, introduzca 0: '))

print(lista)

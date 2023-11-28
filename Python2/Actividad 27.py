# Actividad 27 - Escribir un programa que te pida un primer número. Dicho número lo estableceremos como
# el máximo. Después, queremos pedir n números hasta que la suma de ellos supere el máximo. Finalmente, imprimir.

límite = 0
número = 0
lista = []

límite = float(input('Escriba un número. Este será el máximo: '))

while sum(lista) < límite:
    número = float(input('Escriba un número: '))
    lista.append(número)
else:
    print('La suma de sus números a superado al límite inicial establecido')
    print('La lista resultante es', lista)


import random

'''
def imprimir_tablerito():
    tablerito = []
    for i in range(10):
        tablerito.append(0)

    tablerito[random.randint(0,5)] = 'X'
    print(tablerito)

imprimir_tablerito()

def imprimir_tablero(filas, columnas):

    for i in range(filas):
        print()
        for j in range(columnas):
            print(j, end=' ')
    print()

imprimir_tablero(3, 4)

'''

tablero = []
print(tablero)

def crear_tablero(filas, columnas):
    for i in range(filas):
        row = []
        valor = 0
        for j in range(columnas):
            row.append(valor)
        tablero.append(row)

crear_tablero(5, 5)

minas = 5
contador = 0
while contador < minas:
    fila = random.randrange(0, 5)
    columna = random.randrange(0, 5)
    tablero[fila][columna] = 'X'
    contador += 1


print(tablero)


'''
tablero de 6x5
minas = 3 (beta; luego input)

input('Cuántos minas quiere)

while 'poner minas': # poner minas es: mientras minas sea =/ 0, ir poniendo minas y luego se actualiza
    random(i,j)
    tablero(i,j) -> poner minas

pintar tablero --> for con for. minas son x, lo demas puntos.

---
i = 0
altura = 0
ancho = 0
árbol = '*'

ancho = int(input('Dígame el ancho del rectángulo que quiere: '))
altura = int(input('Dígame la altura del rectángulo que quiere: '))

print('¡Ahora crearemos un rectángulo con los valores que ha proporcionado!')

while len(árbol) < ancho:
    árbol = árbol + '*'

for i in range(altura):
    print(árbol)



import random

minas = 0
circulo = 'O'
tablero = 'O'
tamaño = 31

minas = int(input('¿Cuántas minas quiere? '))

while minas > 15:
    minas = input('El número de minas ha de ser menor de 15. Inténtelo otra vez: ')

tablero = [0, 0, 0, 0, 0, 0]

tablerito = []


def minador():
    contador = 0
    while contador < minas:
        mina = random.randrange(1, 30)
        tablerito[mina] = 'X'
        contador += 1


for i in range(1, 7):
    tablerito.append(0)
    for j in range(1, 7):
        print('{:2}'.format(0), end=' ')
        tablerito.append(0)
    print()

import numpy as np

matriz = np.array([[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])
print(matriz)

contador = 0
while contador < minas:
    mina = random.randrange(1, 30)
    tablerito[mina] = 'X'
    contador += 1

print(tablerito)
'''
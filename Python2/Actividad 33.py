# Actividad 33 - Escribir un programa que te pida dos números. Luego imprimir una lista
# de los números comprendidos entre ellos en orden creciente o decreciente.

número_1 = 0
número_2 = 0
swap = 0

lista_crec = []
lista_decr = []

número_1 = int(input('Escriba el número inicial: '))
número_2 = int(input('Escriba el número final: '))

if número_1 < número_2:
    lista_crec = list(range(número_1, número_2+1, 1)) # Si el primer valor es menor que el segundo, se crea
    # una lista decreciente desde el rango menor al mayor, incluido.
    print(lista_crec)
else:
    swap = número_2
    número_2 = número_1
    número_1 = swap # Pero si el número mayor es el segundo, hay que hacerla decreciente. Para ello hago un swap
    # para tener el número menor como comienzo de la lista, y le ordendo que la vaya disminuyendo en vez de
    # incrementar.
    lista_decr = list(range(número_2, número_1-1, -1))
    print(lista_decr)

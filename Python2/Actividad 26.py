# Actividad 26 - Escribir un programa que te pida dos números. El primero siendo un mínimo y el
# segundo un máximo. Luego queremos introducir números situados entre ellos. Para terminar el loop,
# escribiremos un número que no esté dentro de esos dos números iniciales. Finalmente, imprimir la lista.

lista = []
mínimo = float(0)
máximo = float(0)
número = float(0)

mínimo = float(input('Escriba un número. Este será el mínimo: '))
máximo = float(input('Escriba un número. Este será el máximo, y por tanto, ha de ser mayor que el anterior: '))

while mínimo >= máximo: # Obligamos a que el máximo sea mayor que el mínimo.
    máximo = float(input('Ha de ser mayor. Inténtelo de nuevo:'))

número = float(input(f'Escriba el primer número comprendido entre, {mínimo} y {máximo}. \nDe lo contrario, '
                     f'se interrumpirá la lista: '))

if máximo > mínimo:

    lista.append(número)
    while mínimo < número < máximo:

        número = float(input(f'Escriba un número comprendido entre, {mínimo} y {máximo}. \nDe lo contrario, '
                             f'se interrumpirá la lista: '))
        if lista[-1] < número:
            lista.append(número)
        else:
            break

if mínimo > lista[-1] or máximo < lista[-1]:
    lista = []

print('La lista ha terminado. Su lista es:', lista)

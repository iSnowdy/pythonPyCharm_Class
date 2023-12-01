# Actividad 25 - Escribir un programa que te pida números cada vez más grandes y los introduzca en una
# lista. Para finalizar el loop se escribe un número que no sea mayor al anterior. Finalmente, imprimir.

lista = []
número = 0

número_1 = float(input('Introduzca un número: '))
número_2 = float(input('Introduzca un número mayor al anterior: '))

if número_2 > número_1:
    while número_2 > número_1:
        lista.append(número_1)
        lista.append(número_2)
        número_1 = float(input('Introduzca un número. Cada vez que quiera guardar uno, debe ser mayor al anterior.'
                   ' De lo contrario, se finalizará la lista: '))

        if número_1 > número_2:
            lista.append(número_1)

        else:
                break
        número_2 = float(input('Introduzca un número. Cada vez que quiera guardar uno, debe ser mayor al anterior.'
                           ' De lo contrario, se finalizará la lista: '))
        if número_2 > número_1:
                lista.append(número_2)

        else:
                break

else:
    lista.append(número_1)

print(lista)

# Actividad 24 - Escriba un programa que te pida notas y las vaya guardando en una lista. Para terminar
# el bucle, escriba una nota que no esté entre 0 y 10. Finalmente, imprimir la lista.

lista = []
nota = 0
nota = float(input('Introduzca la nota que desea guardar en una lista. '
                   '\nPara finalizar, escriba un número que no esté entre 0 y 10: '))

while nota > 0 and nota < 11:
    lista.append(nota)
    nota = float(input('Introduzca la nota que desea guardar en una lista. Si quiere terminar la operación,'
                       'escriba un número que no esté entre 0 y 10: '))
print(lista)

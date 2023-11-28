# Actividad 41 - Escribir un programa que te pida cuántos números se quieren introducir. Luego, queremos mostrar
# el valor más pequeño, el más grande y el promedio.

i = 0
lista = []
número_inicial = 0
número_x = 0
número_suma = 0
número_pequeño = 0
número_grande = 0

número_inicial = int(input('Dígame cuántos números quiere analizar: '))

for i in range(número_inicial):
    número_x = int(input(f'Dime el número {i+1}: '))
    lista.append(número_x)
    número_suma = número_suma + número_x

lista.sort()
número_pequeño = lista[0]
número_grande = lista[-1]

print('El número más pequeño de los que ha introducido es', número_pequeño)
print('El número más grande de los que ha introducido es', número_grande)
print('Finalmente, la media de todos los números introducidos es', número_suma/número_inicial)

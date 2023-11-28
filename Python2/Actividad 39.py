# Actividad 39 - Escribir un programa que te pida cuántos números se quieren introducir. Calcula su suma.

número_inicial = 0
número_x = 0
número_suma = 0
i = 0

número_inicial = int(input('Dime cuántos números quieres escribir: '))

for i in range(número_inicial):
    número_x = int(input(f'Dime el número {i+1}: '))
    número_suma = número_suma + número_x

print('Ahora sumaremos los números que has introducido')
print('La suma de sus números es', número_suma)

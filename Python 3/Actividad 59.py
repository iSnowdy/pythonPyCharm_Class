# Actividad 59 - Escribir un programa que pregunte al usuario cuántos números quiere ingresar.
# Luego se le pide que ingrese los datos uno por uno. Finalmente, que salga por pantalla cuántos de los datos
# son mayores que el promedio.

número_inicial = 0
número_x = 0
número_suma = 0
número_promedio = 0
lista = []


número_inicial = int(input('Dime cuántos datos quieres escribir: ')) # Cuántos números quiere escribir

for i in range(número_inicial):
    número_x = float(input(f'Dime el número {i+1}: ')) # Pedimos número por número. i nos da el índice
    lista.append(número_x)  # Añadimos cada número a una lista para luego poder hacer el promedio

print(lista) # Mostramos por pantalla los números insertados por el usuario
# print(len(lista))
promedio = sum(lista)/número_inicial
print(promedio)

count = 0
for i in range(número_inicial):
    if lista[i] > promedio: # Siempre y cuando los números sean mayores que el promedio ...
        print(f'El numero en el índice {i} es mayor que', promedio) # Indicamos qué índice tienen esos números > prom
        count += 1 # Los contamos

print(count, 'datos son mayores que', promedio)

'''
6.5
2.1
2.0
2.2
6.1
'''

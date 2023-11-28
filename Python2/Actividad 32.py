# Actividad 32 - Escribir un programa que le pida al usuario dos números. El segundo
# ha de ser mayor que el primero. Luego escribir diversas listas en base a esos números.

menor = 0
mayor = 0
lista = []

menor = int(input('Dígame un número: '))
mayor = int(input(f'Dígame un número mayor que {menor}: '))

while menor > mayor:
    mayor = int(input(f'¡Mayor que {menor}!: '))

lista = list(range(menor, mayor+1, 1))
print(lista)
lista = list(range(mayor-1, menor-1, -1))
print(lista)
lista = list(range(menor+1, mayor+2, 1))
print(lista)
lista = list(range(mayor-1, menor-1, -1))
print(lista)
lista = list(range(menor, mayor+1, 1)) + list(range(mayor-1, menor-1, -1))
print(lista)

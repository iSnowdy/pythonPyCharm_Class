# Actividad 43 - Escribe un programa que te pida la altura de un triángulo y lo dibuje de la forma
# indicada.

i = 0
altura = 0
árbol = '*'

altura = int(input('Dígame la altura del triángulo: '))

print('Ahora creamos un árbol de navidad con altura', altura, ':')

for i in range(altura):
    print(árbol)
    árbol = árbol + '*'

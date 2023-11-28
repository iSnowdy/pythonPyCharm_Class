# Actividad 42 - Escribir un programa que pida el ancho y altura de un rectángulo y lo dibuje de la
# forma indicada.

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

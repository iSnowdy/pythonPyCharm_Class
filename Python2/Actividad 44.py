# Actividad 44 - Escribir un programa que te pida la altura de un triángulo y lo dibuje de la forma
# indicada.

altura = 0
árbol = '*'

altura = int(input('Indica la altura deseada para su triángulo: '))
árbol = árbol * altura

while len(árbol) > 0:
    print(árbol)
    altura = altura - 1
    árbol = '*'
    árbol = árbol * altura

print('Y con la función "for"')

árbol = '*'
altura = int(input('Indica la altura deseada para su triángulo: '))

for i in range(altura-1, -1, -1):
    print(árbol + str(i * '*'))
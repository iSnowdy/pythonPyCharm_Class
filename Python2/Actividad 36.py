# Actividad 36 - Escribir un programa que te pida dos números. Escribir una lista con los
# números pares que hay entre ellos.

valor_inicial = 0
valor_final = 0

lista = []

valor_inicial = int(input('Dígame el valor inicial. Ha de ser menor que el final: '))
valor_final = int(input('Dígame el valor final de su lista: '))

while valor_inicial > valor_final:
    valor_inicial = int(input('Si primer valor ha de ser menor que su valor final: '))
    valor_final = int(input(f'Ha de ser mayor que {valor_inicial}: '))

print(f'Procederemos a generar una lista que comprenda los valores entre {valor_inicial} y {valor_final} y dichos '
      f'números serán sólo los pares')

if valor_inicial % 2 == 0:
    lista = list(range(valor_inicial, valor_final+1, 2))
else:
    lista = list(range(valor_inicial+1, valor_final+1, 2))

print(lista)
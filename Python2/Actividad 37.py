# Actividad 37 - Escribir un programa que te pida tres números. Generar una lista de números
# múltiples del tercer número introducido por el usuario y que estén entre los dos primeros.

valor_inicial = 0
valor_final = 0
múltiplos = 0

lista = []

valor_inicial = int(input('Dígame un valor inicial para su lista de números: '))
valor_final = int(input('Dígame un valor final para su lista de números: '))

while valor_inicial > valor_final:
    valor_final = int(input(f'¡Mayor que {valor_inicial}!: '))

múltiplos = int(input('¿De qué número quiere los múltiplos? '))

print(f'Procederemos a generar una lista comprendida entre {valor_inicial} y {valor_final} y que los números '
      f'comprendidos sean múltiplos de {múltiplos}')

if valor_inicial % múltiplos == 0:  # Hacemos una comprobación para ver si el valor inicial es múltiplo del valor seleccionado como múltiplo.
    lista = list(range(valor_inicial, valor_final+1, múltiplos))

else: # Si no lo es, tenemos que encontrar el primer valor inicial que sea múltiplo del múltiplo deseado.
    if valor_inicial < múltiplos: # Si el valor inicial está por debajo del primer múltiplo, habrá que incrementarlo hasta llegar a él.
        while valor_inicial % múltiplos != 0:
            valor_inicial = valor_inicial + 1
            print(valor_inicial)
            lista = list(range(valor_inicial, valor_final+1, múltiplos))

    else:
        while valor_inicial % múltiplos != 0: # Pero si está por encima, habrá que reducirlo.
            valor_inicial = valor_inicial - 1
            print(valor_inicial)
            lista = list(range(valor_inicial, valor_final+1, múltiplos))

print(lista)

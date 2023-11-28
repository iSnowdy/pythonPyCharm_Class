# Actividad 40 - Escribir un programa que pida cuántos números se quieren introducir. Escribir cuántos números
# negativos se han introducido.

i = 0
número_inicial = 0
número_x = 0
número_negativo = 0
lista = []


número_inicial = int(input('¿Cuántos números quiere analizar? '))

for i in range(número_inicial):
    número_x = int(input('Escriba un número: '))
    if número_x < 0:
        lista.append(número_x)

print('Procederemos a contar cuántos números negativos ha introducido previamente')
print('Ha introducido un total de', len(lista), 'números negativos')

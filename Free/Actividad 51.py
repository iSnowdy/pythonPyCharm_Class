# Actividad 51 - Escribir un programa que cuente cuántas palabras componen una frase. Se puede o bien usar
# la función split() u otro método deseado.

text = 'string'
x = []

text = str(input('Escriba una frase y le diré de cuántas palabras está compuesta: '))

x = text.split() # Separa todas las palabras y las introduce en una lista.

print('Su frase escrita está compuesta por', len(x), 'palabras')
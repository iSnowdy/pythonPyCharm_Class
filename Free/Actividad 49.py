# Haz un programa que te diga la cantidad de vocales que hay dentro de un texto determinado.
'''
print('Hay', frase.count('a'),'a en la frase')
print('Hay', frase.count('e'),'e en la frase')
print('Hay', frase.count('i'),'i en la frase')
print('Hay', frase.count('o'),'o en la frase')
print('Hay', frase.count('u'),'u en la frase')
'''


frase = str(input('Introduzca una frase cualquiera y le diré cuántas vocales tiene: '))

def contador_vocales (vowels):
    print('¿Funciona?')
    contador = 0
    for letra in vowels:
        if letra.lower() in 'aeiouáéíóúäëïöüàèìòù': # Obligamos a que lo que haya en la frase se ponga en minus.
            contador += 1 # Contador. Es lo mismo que hacer i = i + 1
    return contador # Si no se hace un return no se completa la función.

cantidad = contador_vocales(frase)

print('En la frase introducida hay', cantidad, 'vocales')

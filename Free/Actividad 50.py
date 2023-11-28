# Actividad 50 - Escribir un programa que borre todas las vocales que haya dentro de un texto.

frase = str(input('Introduzca una frase cualquiera y eliminaré las vocales: '))

def borrador_vocales (frase):
    texto = ''
    for letra in frase:
        if letra.lower() not in 'aeiouáéíóúäëïöüàèìòù':
            texto += letra # Te va añadiendo cada cosa que no esté incluida en esas vocales a la variable texto.
    return texto # Luego te saca la variable texto.

sin_vocales = borrador_vocales(frase)
print(sin_vocales)

# print('Su frase introducida sin vocales es tal que:', sin_vocales)

# Actividad 60 - Escribir una función que retorne un diccionario que asocie cada letra a la cantidad de veces
# que aparece en la oración. Mayúsculas y minúsculas han de ser consideradas como iguales. Ignorar espacios.

sentence = str()

sentence = str(input('Escriba una frase y contaré las letras: '))


def letter_counter(oracion):
    d = {}
    oracion = oracion.lower() # Pasamos a minusculas
    oracion = oracion.replace(' ', '') # Quitamos espacios
    print(oracion)
    for letters in oracion:
        if letters not in d:
            d[letters] = 1 # Decimos que si el caracter de oracion no está ya en d, lo inicie a valor 1
        else:
            d[letters] += 1 # Y en caso de que lo esté, se vaya sumando
    d = dict(sorted(d.items())) # Ordenamos los elementos clave alfabéticamente

    return(d)


print(letter_counter(sentence))

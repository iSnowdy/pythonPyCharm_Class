# Actividad 61 - Escribir una función que retorne un diccionario que asocie cada letra a la cantidad de veces
# que aparece al principio de cada palabra. Mayúsculas y minúsculas han de ser consideradas como iguales.
# Ignorar espacios.

sentence = str()
sentence = str(input('Escriba una frase y contaré las letras iniciales de cada palabra: '))


def initial_counter(oracion):

    oracion = ''.join([words[0] for words in sentence.split()])
    # Hacemos una nueva lista con la primera letra de cada palabra en una lista que separamos por palabra
    d = {}
    oracion = oracion.lower() # Pasamos a minusculas
    for letters in oracion:
        if letters not in d:
            d[letters] = 1 # Decimos que si el caracter de oracion no está ya en d, lo inicie a valor 1
        else:
            d[letters] += 1 # Y en caso de que lo esté, se vaya sumando

    d = dict(sorted(d.items())) # Ordenamos los elementos clave alfabéticamente

    return d

print(initial_counter(sentence))


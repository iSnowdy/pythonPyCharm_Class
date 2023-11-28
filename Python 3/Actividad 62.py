# Actividad 62 - Obtener el largo de una oracion en forma de diccionario.

sentence = str()
sentence = str(input('Escriba una frase y contaré las letras de las palabras en ella: '))


def words_letter_counter(oracion):

    oracion = oracion.lower()
    oracion = oracion.split()
    d = {}

    for letters in oracion:
        if letters not in d:
            d[letters] = len(letters)  # Llave [letters] y como valor la longitud. Y no nos interesa repetir

    d = dict(sorted(d.items()))  # Ordenamos los elementos clave alfabéticamente

    return d


print(words_letter_counter(sentence))

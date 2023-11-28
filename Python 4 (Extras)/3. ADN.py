# Se mantienen dos listas de información. Una primera lista contiene el nombre de las personas registradas en la
# región (por nombre y apellido). La segunda lista contiene un cromosoma representativo del ADN de cada una de
# esas personas.

# Consideramos que un cromosoma es una cadena de 0's y '1s de largo 20.

# El método con el que se determina el sospechoso es el siguiente:
# 1. Se obtiene una muestra del cromosoma del autor del delito. Ha de tener 20 caracteres.
# 2. Se busca en la lista que tenemos de cromosomas el más *parecido* a la muestra tomada. Definimos como el más
# parecido al cromosoma que tiene más genes iguales a la muestra.
# 3. Al terminar la búsqueda, se muestra el nombre de la persona cuyo cromosoma es sospechoso junto con el porcentaje
# de parentesoc.

# Los datos de las listas han de ser ingresados por el programador. Sin embargo la secuencia a comparar ha de ser
# ingresada por el usuario; es la muestra encontrada en la escena del crimen.

personas = [
    'Pedo Dominguez', 'Juan Perez', 'Diego San Joan',
    'Dawud Nicholson', 'Jemma Erickson', 'Faye Oneal',
    'Lorna Howell', 'Rosanna Roth', 'Kingsley Underwood'
]

DNA_sequence = [

    '00000101010101010101', '00101010101101110111', '00100010010000001001',
    '11001111010011011101', '00111010010111001101', '01011001001111001010',
    '01110000011011101111', '00111001111000010111', '10111000111000110011'
]

'''
01010101000011001100
'''


testing_sequence = str(input('Ingrese la secuencia de DNA: '))

while len(testing_sequence) > 20 or len(testing_sequence) < 20:
    testing_sequence = str(input('La secuencia de DNA está compuesta por 20 caracteres. Inténtelo nuevamente: '))

'''

print(testing_sequence[0])
print(testing_sequence[1])

print('---------------')

print('Hi', testing_sequence.count('0'))
print('Bye', DNA_sequence[0].count('0'))
'''

indice = 0

def DNA_comparison(sample, comparison):

    coincidences = 0
    ceros = 0
    unos = 1
    sample_ceros = 0
    sample_unos = 0

    sample_ceros = sample.count('0')
    sample_unos = sample.count('1')

    print('En sample hay: ', sample_ceros, 'y', sample_unos)

    for i in range(len(DNA_sequence)):
        ceros = DNA_sequence[i - 1].count('0')
        unos = DNA_sequence[i - 1].count('1')
        print(f'Ceros en posición {i+1}', ceros)
        print(f'Unos en posición {i+1}', unos, '\n')





print(DNA_comparison(testing_sequence, DNA_sequence))






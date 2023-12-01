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


'''
01010101000011001100
'''


def DNA_comparison(muestra, nombres, cromosomas):

    mejor_coincidencia = 0
    sospechoso = ""

    for i in range(len(cromosomas)):
        coincidencias = 0

        for j in range(len(muestra)):
            coincidencias += muestra[j] == cromosomas[i][j]

        if coincidencias > mejor_coincidencia:
            mejor_coincidencia = coincidencias
            sospechoso = nombres[i]

    porcentaje_coincidencia = (mejor_coincidencia / len(muestra)) * 100

    return sospechoso, porcentaje_coincidencia


suspects = [
    'Pedo Dominguez', 'Juan Perez', 'Diego San Joan',
    'Dawud Nicholson', 'Jemma Erickson', 'Faye Oneal',
    'Lorna Howell', 'Rosanna Roth', 'Kingsley Underwood'
]

DNA_sequence = [

    '00000101010101010101', '00101010101101110111', '00100010010000001001',
    '11001111010011011101', '00111010010111001101', '01011001001111001010',
    '01110000011011101111', '00111001111000010111', '10111000111000110011'
]


sample = input("Ingrese la muestra de ADN encontrada en la escena del crimen (20 caracteres 0/1): ")


sospechoso, porcentaje = DNA_comparison(sample, suspects, DNA_sequence)



print(f"\nSospechoso encontrado: {sospechoso}")
print(f"Porcentaje de parentesco: {porcentaje}%")



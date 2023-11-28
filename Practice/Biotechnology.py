'''

Un grupo de bio-tecn ´ologos externos a la USM, tienen demasiado trabajo analizando
cadenas de ADN. El trabajo lo realizan a mano ya que no tuvieron un buen ramo de
programación. Por esto, le piden a los estudiantes de el ramo de Programaci ´on IWI-131 que les
ayuden. Las cadenas de ADN est ´an compuestas por 4 bases nitrogenadas (A: Adenina, C: Citosina,
G: Guanina y T: Timina) agrupadas en bloques de 4. Ahora usted debe ayudar en las siguientes
operaciones:

a) Escriba la funci ´on valida(cadena) que reciba un string con una cadena de ADN y retorne
True si la cadena es v ´alida o False si no lo es. Una cadena no es v ´alida cuando aparecen bases
nitrogenadas distintas a las antes descritas.

b) Escriba la funci ´on cantidad(cadena, base) que reciba un string con una cadena de ADN
y una base nitrogenada. La funci ´on debe retornar la cantidad de apariciones de la base en la
cadena.
Nota: no puede utilizar el m´etodo count de procesamiento de texto.

c) Los cient´ıficos encontraron un patr ´on de clasificaci ´on, que se deduce de la cantidad mayoritaria
de un cierto par de bases. Si la suma de las cantidades de Citosina y Guanina es mayor a la de
Adenina y Timina, es una especie vegetal, en caso contrario es una especie animal. Escriba un
programa que pregunte la cantidad de cadenas de ADN a evaluar, luego solicite las cadenas y
finalmente muestre las cantidades de cada especie y cadenas no v´alidas.

'''

# a)


def valida(cadena):

    cadena = cadena.replace(' ', '')
    cadena.upper()
    i = 0
    while i < len(cadena):
        if cadena[i] != 'C' and cadena[i] != 'A' and cadena[i] != 'G' and cadena[i] != 'T':
            return False
        i += 1
    return True

print(valida('CTGA CTGA AATT GGGC CTGG CCCC'))
print(valida('CTGA XCGA CGAT GGTA ACCC CCPC TTAA'))


# b)

def cantidad(cadena, base):

    cadena = cadena.replace(' ', '')
    cadena.upper()
    i = 0
    match = 0
    while i < len(cadena):
        if base == cadena[i]:
            match += 1
        i += 1

    return match

print(cantidad('CTGA CTGA AATT GGGC CTGG CCCC', 'A'))
print(cantidad('CTGA CTGA AATT GGGC CTGG CCCC', 'C'))


# c)

cantidad_cadenas = int(input('¿Cuántas cadenas de ADN desea analizar? '))
i = 1
animales = 0
vegetales = 0
no_validas = 0

while i <= cantidad_cadenas:
    cadena = str(input(f'Ingrese la cadena {i} de ADN:'))
    if valida(cadena):
        cant_C = cantidad(cadena, 'C')
        cant_G = cantidad(cadena, 'G')
        cant_T = cantidad(cadena, 'T')
        cant_A = cantidad(cadena, 'A')

        if cant_C + cant_G > cant_A + cant_T:
            vegetales += 1
        else:
            animales += 1

    else:
        no_validas += 1

    i += 1

print('Cantidad de animales: ', animales,
      '\nCantidad de vegetales: ', vegetales,
      '\nCantidad de cadenas no válidas: ', no_validas)
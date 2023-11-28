'''

La CONFECH, en su af´an de agilizar el proceso de recuento de las votaciones, le ha
encargado el desarrollo de un programa de registro de votaci ´on por universidades.

Primero, el programa debe solicitar al usuario in-
gresar la cantidad de universidades que partici-
pan en el proceso.

Luego, para cada una de las universidades, el
usuario debe ingresar el nombre de la universi-
dad y los votos de sus alumnos, que pueden ser:
aceptar (A), rechazar (R), nulo (N) o blanco (B). El
t´ermino de la votaci ´on se indica ingresando una
X, tras lo cual se debe mostrar los totales de votos
de la universidad, con el formato que se muestra
en el ejemplo.

Finalmente, el programa debe mostrar el resulta-
do de la votaci ´on, indicando la cantidad de uni-
versidades que aceptan, que rechazan y en las
que hubo empate entre estas dos opciones.

'''

aceptan_c = 0
rechazan_c = 0
empate_c = 0

loop = False

while not loop:

    try:

        n_unis = int(input('Número de universidades que votarán: '))

    except ValueError:

        print('Ha de ser un número')

    else:

        loop = True



for i in range(n_unis):


    voto = ''
    voto_L = []
    aceptan = 0
    rechazan = 0
    blancos = 0
    nulos = 0



    universidad = str(input(f'Indique el nombre de la universidad {i+1}: '))

    while 'X' not in voto:

        voto = str(input('Voto: '))

        if 'A' in voto:
            aceptan += 1
        elif 'R' in voto:
            rechazan += 1
        elif 'B' in voto:
            blancos += 1
        elif 'N' in voto:
            nulos += 1

    if aceptan > rechazan:

        aceptan_c += 1

    elif rechazan > aceptan:

        rechazan_c += 1

    else:

        empate_c += 1

    print(universidad + ': ', aceptan, 'aceptan,', rechazan,'rechazan',blancos,'en blanco y', nulos,'nulos')
    print(aceptan_c)
    print(rechazan_c)
    print(empate_c)


print('Universidades que aceptan: ', aceptan_c)
print('Universidades que recahzan: ', rechazan_c)
print('Universidades con empate: ', empate_c)
import random


def word():

    palabra = ''
    guess = str(input('Ingrese la palabra a adivinar: ')).lower()
    print('La palabra a adivinar tiene una longitud de', len(guess))

    return guess



def adivinar():

    guess = word()
    palabra = ''

    for i in range(len(guess)):

        palabra = palabra + '_'

    incorrecto = 0
    intentos_maximos = 6

    letra_l = []
    pierde = ['pierna derecha', 'pierna izquierda', 'cuerpo', 'brazo derecho', 'brazo izquierdo']

    while incorrecto < intentos_maximos:

        print('Palabra oculta: ' + ' '.join(palabra))
        letra = str(input('Ingrese una letra: ')).lower()

        if letra in letra_l:

            print('Ya has intentado esa letra antes! Intente otra')
            letra_l = letra_l + [letra.lower()]

        elif letra in guess:

            print('Correcto! La letra', letra, 'está en la palabra')
            letra_l = letra_l + [letra]
            for i in range(len(palabra)):

                if guess[i] == letra:
                    palabra = palabra[:i] + letra + palabra[i+1:]

        else:

            print('¡Incorrecto! La letra', letra, 'no está en la palabra')

            if incorrecto < 5:

                perdio = random.choice(pierde)
                pierde.remove(perdio)
                print('El muñeco ha perdido ', perdio)

            letra_l = letra_l + [letra]
            incorrecto += 1
            print('Te quedan', intentos_maximos - incorrecto, 'intentos')

        if palabra == guess:
            print('¡Felicidades! Has ganado. La palabra era', palabra)
            incorrecto = 6

    if palabra != guess:

        print('¡El muñeco ha muerto! Perdió la cabeza')
        print('Te has quedado sin intentos! La palabra era' + ' ' + guess)


    again = str(input('¿Quieres intentarlo nuevamente? Y/N ')).lower()

    if again == 'y':

        menu()


def menu():

    print('----------------------------------\n'
          'Bienvenido al Juego del Ahorcado!\n'
          '\n'
          'Se introducirá una palabra y usted debe intentar adivinarla. Tendrá como pista'
          ' la longitud.\n\n'
          'Tiene 6 intentos. Con cada error el personaje pierde una parte de su cuerpo x.x \n\n'
          '¡Buena suerte!\n'
          '----------------------------------\n\n')

    adivinar()


menu()
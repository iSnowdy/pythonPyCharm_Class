# Proyecto 4: Calculadora evolutiva 2


def Numbers(text):

    leido = False

    while not leido:

        try:
            number = float(input(text))

        except ValueError:
            print('Error. You must introduce a number')

        else:
            leido = True

    return number

def addition():

    number_1 = Numbers(f'Type in number 1: ')
    number_2 = Numbers(f'Type in number 2: ')

    print('The result of your addition is ', number_1 + number_2)


def subtract():

    number_1 = Numbers(f'Type in number 1: ')
    number_2 = Numbers(f'Type in number 2: ')

    print('The result of your addition is ', number_1 - number_2)


def multiply():

    number_1 = Numbers(f'Type in number 1: ')
    number_2 = Numbers(f'Type in number 2: ')

    print('The result of the multiplication is ', number_1 * number_2)


def division():

    number_1 = Numbers('Dividend: ')
    number_2 = Numbers('Divider: ')

    try:
        result = number_1 / number_2

    except ZeroDivisionError:
        print('Error. You cannot divide by 0')
    else:
        print('The result of the division is ', result)

def ShowMenu():

    asteriscos = '************'
    print(asteriscos)
    print('Calculator')
    print(asteriscos)

    print('Menu\n'
          '1) Addition\n'
          '2) Subtraction\n'
          '3) Multiply\n'
          '4) Division\n'
          '5) Show Menu\n'
          '6) Exit\n'
          )


def Calculator():

    loop = False
    ShowMenu()

    while not loop:

        choice = Numbers('Type in your choice: ')

        if choice == 1:
            addition()
        if choice == 2:
            subtract()
        if choice == 3:
            multiply()
        if choice == 4:
            division()
        if choice == 5:
            ShowMenu()
        if choice == 6:
            loop = True


Calculator()
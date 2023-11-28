# Proyecto 2: Calculadora evolutiva


asteriscos = '************'
print(asteriscos)
print('Calculator')
print(asteriscos)

print('Menu\n'
      '1) Addition\n'
      '2) Subtraction\n'
      '3) Multiply\n'
      '4) Division\n'
      '5) Exit\n'
      )


def calculator ():

    loop = False

    while not loop:

        print('Choose what would you like to do by typing a number')
        choice = int(input('Type 1-5 accordingly to the menu: '))

        if choice == 1:
            addition()
        if choice == 2:
            subtract()
        if choice == 3:
            multiply()
        if choice == 4:
            division()
        if choice == 5:

            print('Goodbye!')
            loop = True



def addition ():

    amount = int(input('How many numbers would you like to add? '))
    number_add = 0
    for i in range(amount):
        number_1 = float(input(f'Type in number {i + 1}: '))
        number_add = number_1 + number_add
    print('The result of your addition is ', number_add)
    choice_2 = str(input('Would you like to do another operation? Yes/No '))
    if 'Yes' in choice_2:
        calculator()
    elif 'No' in choice_2:
        print('Type 5')
        calculator()
    else:
        print('I did not understand you. Program will restart')
        calculator()

def subtract ():

    amount = int(input('How many numbers would you like to subtract? '))
    number_sub = None
    for i in range(amount):
        number_1 = float(input(f'Type in number {i + 1}: '))
        if number_sub is None:
            number_sub = number_1
        else:
            number_sub = (number_sub) - (number_1)
    print('The result of your subtraction is', number_sub)
    choice_2 = str(input('Would you like to do another operation? Yes/No '))
    if 'Yes' in choice_2:
        calculator()
    elif 'No' in choice_2:
        print('Type 5')
        calculator()
    else:
        print('I did not understand you. Program will restart')
        calculator()

def multiply ():

    amount = int(input('How many numbers would you like to multiply? '))
    number_multiply = 1
    for i in range(amount):
        number_1 = float(input(f'Type in number {i + 1}: '))
        number_multiply = number_multiply * number_1
    print('The result of your multiplication is ', number_multiply)
    choice_2 = str(input('Would you like to do another operation? Yes/No '))
    if 'Yes' in choice_2:
        print('Type 5')
        calculator()
    elif 'No' in choice_2:
        print('Type 5')
    else:
        print('I did not understand you. Program will restart')
        calculator()

def division ():

    number_1 = float(input(f'Type in the dividend: '))
    number_2 = float(input(f'Type in the divider: '))
    numbers_division = number_1 / number_2
    print('The result of your division is ', numbers_division)
    choice_2 = str(input('Would you like to do another operation? Yes/No '))
    if 'Yes' in choice_2:
        calculator()
    elif 'No' in choice_2:
        print('Type 5')
        calculator()
    else:
        print('I did not understand you. Program will restart')
        calculator()

def quitting():

    loop = True


calculator()
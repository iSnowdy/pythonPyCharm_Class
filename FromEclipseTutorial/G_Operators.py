'''
Created on 25 oct 2023

CESUR - Python Tutorial
@author: Tomeu Sabater
'''

#--- PYTHON OPERATORS #########################################################
#-- To perform operations on variables and values

#--  Python Arithmetic Operators ###############################


def ArithmeticFuncion(int_valor_1, int_valor_2):

    int_suma = int(int_valor_1 + int_valor_2)
    print(int_suma)

    int_resta = int(int_valor_1 - int_valor_2)
    print(int_resta)

    int_multiplica = int(int_valor_1 * int_valor_2)
    print(int_multiplica)

    float_divide = float(int_valor_1 / int_valor_2)
    print(float_divide)

    int_modulo = int(int_valor_1 % int_valor_2) #-- Es el resto de la división 
    print(int_modulo)

    int_potencia = float(int_valor_1 ** int_valor_2)#-- Es primer valor elevado al segundo valor
    print(int_potencia)

    int_division_entera = int(int_valor_1 // int_valor_2) #-- División entera, redondea hacia abajo el resultado
    print(int_division_entera) 

# ArithmeticFuncion(5,-3)
# ArithmeticFuncion(-3,5)
ArithmeticFuncion(5,3)

#--  Python Assignment Operator ###############################

int_numero = int(5)
print(int_numero)

int_numero += 1 # int_numero = int_numero + 1 
print(int_numero)

int_numero += int_numero # int_numero = int_numero + int_numero
print(int_numero)

int_numero -= 1 # int_numero = int_numero - 1
print(int_numero)

int_numero *= 3 # int_numero = int_numero * 3
print(int_numero)





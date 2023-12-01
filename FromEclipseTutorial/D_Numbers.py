'''
Created on 17 oct 2023

CESUR
Python Numbers

@author: Tomeu Sabater
'''

#-- Números Enteros
var_int = int(-123456789)  # Número entero, positivo o negativo

print(var_int)
print(type(var_int))

#-- Números reales 
var_float = float(-222.8875)    # Variable real, positivo o negativo con parte entera y parte decimal
var_floate = float(35e3)        # Variable real, notación base10
var_floatE = float(53E3)        # Variable real, notación base 10
var_floatSC = float(-87.7e100)  # Variable real, notación científica

print(var_float)
print(type(var_float))
print(var_floate)
print(type(var_floate))
print(var_floatE)
print(type(var_floatE))
print(var_floatSC)
print(type(var_floatSC))

#-- Números complejos
var_complex = complex(-3+5j) # Variable compleja, con "j" es la parte imaginaria
print(var_complex)
print(type(var_complex))

#-- Type Conversion
print("#-- Type Conversion")
x_int = int(10)         # Definimos e inicializamos un entero
y_float = float(3.14)    # Definimos e inicializamos un real 
z_complex = complex(1j) # Definimos e inicializamos un complejo 

#convert from int to float
a_float = float(x_int) # Parte decimal será 0, no existe en enteros
print(a_float)
print(type(a_float))

#convert from float to int
b_int = int(y_float) # Parte decimal se pierde, enteros no la poseen
print(b_int)
print(type(b_int))

#convert from int to complex:
c_complex = complex(x_int) # Parte imaginaria será 0, no existe en enteros
print(c_complex)
print(type(c_complex))

#-- Random Numbers
#-- Python has not a random generator, 
#-- Python has a built-in module called random that can be used to make random numbers

print("#-- Random Numbers")

import random  #-- First, you need to import the built-in module to use it

print(random.randrange(1, 10)) #-- Range for random number will be [1,10), the 10 is excluded
print(random.randrange(1, 10))
print(random.randrange(1, 10))
print(random.randrange(1, 10))
print(random.randrange(1, 10))
print(random.randrange(1, 10))
print(random.randrange(1, 10))
print(random.randrange(1, 10))
print(random.randrange(1, 10))
print(random.randrange(1, 10))

random_number_1_9 = int(random.randrange(1, 10)) #-- Of course, you can assign the generated random number to a variable
print(random_number_1_9)


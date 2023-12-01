'''
Created on 17 oct 2023

CESUR
Python Strings

@author: Tomeu Sabater
'''


#--- STRINGS #########################################

#-- How to  the characters ' and " in strings 
print("#-- Scape symbols in strings")
print("Hello it's a good new")  # You can write ' between "
print('My name starts with "T"') # You can write " between '
print("You can print \"") # You can scape a symbol using \
print("You can scape with the \"\\\" symbol")

#-- Assign String to variable
print("#-- Assign strings to variables")
x_string = str("Hello it's a good new")
print(x_string)
print(type(x_string))

#-- Assign multiple String to variables can be done using ''' or """"
a_longString = str(''' 
Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.
''')
print(a_longString)

another_longString = str(""" 
Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.
""")
print(another_longString)

#-- Strings, as many other programming languages, are arrays of characters
mi_nombre = str("Tomeu Sabater") #-- Define and initialize
print(mi_nombre[0])
print(mi_nombre[1])
print(mi_nombre[2])
print(mi_nombre[3])
print(mi_nombre[4])
print(mi_nombre[5])
print(mi_nombre[6])

#--- Looping through string ################################
#-- You can create an automatic loop throug strings
print("#-- String loop")
for letra in mi_nombre:
    print(letra)

#-- String length
print("#-- String length")
print(len(mi_nombre)) #-- Prints the string lenght

length_mi_nombre = int(len(mi_nombre)) #-- Another example of string lenght
print(length_mi_nombre)

#-- Check if a certain phrase or character is present in a string
print("#-- Check for certain phrase or character")
print("Tomeu" in mi_nombre)  #-- Must print True
if "Tomeu" in mi_nombre:
    print("\"Tomeu\" sí está en mi_nombre")

#-- To check if a certain phrase or character is NOT present in a string
print("Juan" in mi_nombre) #-- Must print False
if "Juan" not in mi_nombre:
    print("Juan no está en mi_nombre")


#--- SLICING STRINGS ###################################################
print("#-- Slicing Strings")
print(mi_nombre[6:13])  # From position 6 to position 13 (not included) 
mi_nombre_pila = str(mi_nombre[0:5]) # From first position to position 5 (not included) 
mi_nombre_apellido = str(mi_nombre[6:13]) # From position 6 to position 13 (not included)
print("mi nombre es : " + mi_nombre_pila)
print("mi apellido es: " + mi_nombre_apellido)

#-- Slice from start / end
print(mi_nombre[:5]) #-- Slice from start to position 5 (not included) 
print(mi_nombre[6:]) #-- Slice from position 6 the end

#-- You can slice using combinations
print(mi_nombre[len(mi_nombre)-1:]) #-- Slice the last character

#-- MODIFY STRINGS ###################################################################################
print("#-- Modifying Strings")
#-- Uppder and lower case
print(mi_nombre.upper()) #-- This prints the string in upper case
print(mi_nombre.lower()) #-- This prints the string in lower case

MI_NOMBRE_UPPER = str(mi_nombre.upper()) #-- Transform to upper case
mi_nombre_lower = str(mi_nombre.lower()) #-- Transform to lower case
print(MI_NOMBRE_UPPER)
print(mi_nombre_lower)

#-- Remove Whitespaces
mi_nombre_spaces = str("     Tomeu    Sabater     ")
print(mi_nombre_spaces)
mi_nombre_no_spaces = str(mi_nombre_spaces.strip()) #-- Remove whitespace before and/or after the text
print(mi_nombre_no_spaces) #-- Only removes whitespaces before and/or after, not inside the text

#--- Replace 
mi_nombre_oficial = mi_nombre.replace("Tomeu","Bartolomé")
print(mi_nombre)
print(mi_nombre_oficial)

mi_nombre_oficial_no_tildes = mi_nombre_oficial.replace('é','e')
print(mi_nombre) 
print(mi_nombre_oficial) 
print(mi_nombre_oficial_no_tildes) 

#--- Split
mi_nombre_split = mi_nombre.split(" ") #-- Split in two strings, after/before the whitespace
print(mi_nombre_split) 
print(type(mi_nombre_split)) #-- The result is a list of strings

mi_nombre_completo = "Tomeu Sabater Bosch" #-- Split in three strings
mi_nombre_completo_split = mi_nombre_completo.split(" ")
print(mi_nombre_completo_split) 


#--- STRING CONCATENATION  ######################################################################

#-- To concatenate, or combina two string you can use the '+' operator

mi_nombre_completo = "Tomeu" + "Sabater" + "Bosch"
print(mi_nombre_completo)
mi_nombre_completo = "Tomeu" + " " + "Sabater" + " " + "Bosch"
print(mi_nombre_completo)

#--- FORMAT STRINGS  ######################################################################

mi_edad = int(50) #-- Define and initialize integer variable
# mi_nombre_y_edad = mi_nombre+ mi_edad # This is ilegal because variables are different type

#-- You can combine numbers and strings using format()
mi_nombre_y_edad = "Tomeu Sabater {}"
print(mi_nombre_y_edad.format(mi_edad))

#-- You also can use the cast str() to trasform the number in string
print(mi_nombre + ' ' + str(mi_edad))

#-- format() method takes unlimited number of arguments
mi_nombre_pila = str("Tomeu")
mi_primer_apellido = str("Sabater")
mi_segundo_apellido = str("Bosch")
mis_datos = str("Mi nombre es {} y mis apellidos {} {} y tengo {} años")
print(mis_datos.format(mi_nombre_pila, mi_primer_apellido, mi_segundo_apellido, mi_edad))

#-- Best option is put an index to be sure the arguments are in the order desired
mis_datos = str("Mis apellidos son {1} {2} y mi nombres es {0} y tengo {3} años")
print(mis_datos.format(mi_nombre_pila, mi_primer_apellido, mi_segundo_apellido, mi_edad))


#--- ESCAPE CHARACTERS ######################################################################

# mi_texto = str("La "A" es la primera vocal") # This is illegal
mi_texto = str("La 'A' es la primera vocal")
print(mi_texto)
mi_texto = str('la "A" es la primera vocal')
print(mi_texto)
mi_texto = str("Los caracteres \" \' y \\ se escapean con el caracter \\")
print(mi_texto)

#---  escape characters used in Python:
# \'
# \"
# \\
# \n -> New line
# \r -> Carriage Return
# \t -> Tab
# \b -> BackSpace
# \f -> From Feed
# \000 -> Octal value
# \xhh -> Hexadecimal value

print("Hola que tal\ncómo te va?")

#---- STRING METHODS ######################################################################

#-- Built-in methods than you can use. 
#-- We will check some of them

#-- capitalize() Upper case the first letter
#-- lower() Converts a string into lower case

mi_nombre_pila = mi_nombre_pila.lower() #-- converts into lower case
mi_primer_apellido = mi_primer_apellido.lower() 
mi_segundo_apellido = mi_segundo_apellido.lower()
mis_datos = str("Mis apellidos son {1} {2} y mi nombres es {0}")
print(mis_datos.format(mi_nombre_pila, mi_primer_apellido, mi_segundo_apellido))

mi_nombre_pila = mi_nombre_pila.capitalize() #-- Upper case the first letter
mi_primer_apellido = mi_primer_apellido.capitalize()
mi_segundo_apellido = mi_segundo_apellido.capitalize()
print(mis_datos.format(mi_nombre_pila, mi_primer_apellido, mi_segundo_apellido))


#--- isnumeric() Check if all the characters in the text are numeric
es_numero = str("10")   
if es_numero.isnumeric():   
    es_numero = int(es_numero)  #-- Cast to integer
    print(es_numero + es_numero)
else:
    print("no es número")

#-- count() Return the number of times a value appears in the string
#-- replace() method replaces a specified phrase with another specified phrase.
mi_nombre_pila = str("Bartolomé")
if mi_nombre_pila.count("é") > 0 :
    print(mi_nombre_pila.count("é"))
    mi_nombre_pila = str(mi_nombre_pila.replace('é','e')) 
print(mi_nombre_pila)       

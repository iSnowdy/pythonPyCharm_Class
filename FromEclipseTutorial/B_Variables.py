'''
Created on 17 oct 2023

CESUR
Python Variables

@author: Tomeu Sabater
'''

x = 5       # x es de tipo entero
y = "Tomeu" # y es de tipo string
print(x)
print(y)

# Podemos especificar el tipo de variable cuando se define
# La operación se denomina Casting

x = str(3) # x es un entero y vale 3
y = int(3) # y contiene el carácter 3
z = float(3) # z contiene el número real 3.0

print(x)
print(y)
print(z)

# También podemos consultar el tipo de una variable
print(type(x))
print(type(y))
print(type(z))

# Las cadenas de carácters se pueden escribir con comillas simples o compuestas
x = 'Tomeu Sabater'
print(x)
x = "Tomeu Sabater"
print(x)
x = "Ca'n Nadal"
print(x)
x = "La \"x\" sueler ser una variable"
print(x)

# Los nombres de la variables son Case-Sensitive
a = int(5) # a minúscula no es A
A = int(15) # A mayúscula no es a
print(a)
print(A)

# Y tendremos cuidado porque los nombres de la variables son diferentes
# por tanto, las variables son diferentes
Total = int(5)
Total = 10
print(Total)
total = 0 # total != Total, no son la misma variable 
print(Total)

# Nombres de las Variables en Python
# Se recomienda nombrarlas tal que describan su contenido
# Conjunto de carácteres permitido para definir variables es: (A-z, 0-9, and _ )
Variable = int(5)
_Variable = int(10)
Total_sin_descuento = int(0) # Nombre de variable descriptivo
Total_con_descuento = int(0) # Nombre de variable descriptivo
# 9Variable = int(0) # Nombre de variable ilegal, no puede comenzar con un número 
Variable_1 = int(20) # Variables pueden contener "_" y números
# print = int(20) # Ilegal una variable no puede ser una palabra reservada  
# $Total = int(10) # Ilegal, no puede comenzar con un símbolo  

print(Variable)
print(_Variable)
print(Variable_1)
print(Total_sin_descuento)
print(Total_con_descuento)

#Recomendación para los nombres de la variables
#DEBEN ser descriptivas de su contenido
Totalsindescuento = int(0) # Válido pero no es la mejor opción 
Total_sin_descuento = int(20) # Buen ejemplo con Snake Case
TotalConDescuento = int(30) # Otro buen ejemplo fácil de leer con Pascal Case

print(Totalsindescuento)
print(Total_sin_descuento)
print(TotalConDescuento)

# Asignación múltiple de variables
x, y, z = 1, 2, 3 # Asignación de 3 valores a 3 variables 
x, y ,z = int(1), int(2), int(3) # Asignación de 3 valores a 3 variables

print(x)
print(y)
print(z)

x = y = z = int(99) # Asignación de un unico valor a varias variables
print(x)
print(y)
print(z)

# Desempaquetar una colección / se verán las colecciones más adelante
# Es otro ejemplo de asignación múltiple
frutas = ["manzana", "naranja", "pera"] # Creamos la colección
fruta_1, fruta_2, fruta_3 = frutas # Asignamos el contenido de la colección a las variables
print(fruta_1)
print(fruta_2)
print(fruta_3)

# Print de multiple variables
print(fruta_1, fruta_2, fruta_3) # Imprime cada una de las variables
print(fruta_1 + fruta_2 + fruta_3) # Imprimer las variables concatendas
print(fruta_1 + ' ' + fruta_2 + ' ' + fruta_3) # Imprime las variables concatenadas con un espacio

# Print con + en variables numéricas es la operación matemática de suma 
x = y = z = int(100)
print(x + y + z) # Imprime la suma no la concatenación, porque son 3 variables enteras

x = int(0) # Number 0
y = str('0') # Caracter '0' 
# print(x + y) # Dará un error puesto que son 2 tipos distintos
print(x,y)

# GLOBAL VARIABLES ####################################################################################

# Definimos e inicializamos una variable global de tipo string
mi_string = str("Tomeu es increiblemente malo") # Variable global 

# Definimos una función 
def myFuncion():
    mi_string = str("Tomeu es increiblemente bueno") # Definimos una variable local, no afecta a una igual pero global
    print(mi_string) # Imprime la variable local 
    
myFuncion() # Llamamos a la función 
print(mi_string) # Imprimimos el valor de la variable global 

# Definimos una función con una variable global
mi_otro_string = str("No me gusta la programación")

def myFuncion2():
    global mi_otro_string  # Ahora la definimos como global, afectará a otra igual global
    mi_otro_string = str("Si que me gusta programar") # La inicializamos
    print(mi_otro_string) # La imprimimos

myFuncion2() # llamamos a myFuncion2
print(mi_otro_string) # Imprimimos la variable gobal, es nueva definida en la función 


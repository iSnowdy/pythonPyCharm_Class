'''
Created on 17 oct 2023

CESUR
Python Data Types

@author: Tomeu Sabater
'''

# -- Text type
print("# -- Text Types")
text_type = str("Hola Mundo")   # Definimos e inicializamos
print(text_type)                # Mostramos su valor
print(type(text_type))          # Mostramos el tipo de la variable

# -- Numeric Types
print("# -- Numeric Types")

int_type = int(10) # Tipo entero 
float_type = float(10.5) # Tipo real
complex_type = complex(10j) # Tipo complejo

print(int_type)
print(type(int_type))

print(float_type)
print(type(float_type))

print(complex_type)
print(type(complex_type))

#-- Sequence Types
print("#-- Sequence Types")

list_type = list(["manzana","pera","melón"]) # Tipo lista
tuple_type = tuple(("manzana","pera","melón")) # Tipo tupla
range_type = range(10)

print(list_type) 
print(type(list_type))

print(tuple_type)
print(type(tuple_type))

print(range_type)
print(type(range_type))

#-- Mapping Types
print("#-- Mapping Types")

mapping_type = dict(nombre="Tomeu", altura=1.78, age=50) # Tipo mapping

print(mapping_type)
print(type(mapping_type))

#-- Set Types
print("#-- Set Types")

set_type = set(("manzana","pera","melón")) # Tipo set
frozenset_type = frozenset(("manzana","pera","melón")) # Tipo frozenset

print(set_type)
print(type(set_type))

print(frozenset_type)
print(type(frozenset_type))

#-- Boolean Types
print("#-- Boolean Types")

boolean_type = bool(True) # Tipo booleano

print(boolean_type)
print(type(boolean_type))

#-- Binary Types
print("#-- Binary Types")

binary_type = bytes(5) # Tipo bytes
bytearray_type = bytearray(5) # Tipo array binario 
memoryview_type = memoryview(bytes(5)) # Tipo 

print(binary_type)
print(type(binary_type))

print(memoryview_type)
print(type(memoryview_type))

#-- None Types
print("#-- None Types")

none_type = None # Tipo sin tipo 
print(none_type)
print(type(none_type))


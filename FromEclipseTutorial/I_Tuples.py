'''
Created on 25 oct 2023
CESUR - Python Tutorial
@author: Tomeu Sabater
'''

#--- PYTHON TUPLES #############################################
print("#--- PYTHON TUPLES #############################################")
# Tuples are used to store multiple items in a single variable: List, Tuples, Set, and Dictionary, 
#     all with different qualities and usage.
# A TUPLE is a collection which is ordered and unchangeable.
# Tuples are written with round brackets.

mi_tupla = tuple(["uno", "dos", "tres"]) 
print(mi_tupla)


# Tuple items are Ordered, Unchangeable, and allow Duplicate values.
# Tuple items are indexed, the first item has index [0], the second item has index [1] etc.
# Ordered: it means that the items have a defined order, and that order will not change.
# Unchangeable: we cannot change, add or remove items after the tuple has been created.
# Duplicates allowed: they can have multiple items with the same value


mi_tupla = tuple(("uno", "dos", "tres", "dos", "uno"))
print(mi_tupla)


#-- Tuple length
print("mi_tupla tiene " + str(len(mi_tupla)) + " elementos")


#-- It is allowed to create an empty tuple
#-- Remember, name of the tuple is a pointer, with an emtpy tuple we can create a pointer to be used
mi_tupla_vacia = tuple((""))
print("mi_tupla_vacia tiene " + str(len(mi_tupla_vacia)) + " elementos")


#-- It is allowed to crete a tuple with only one item, 
#--- in this case you need add a comma after the item
mi_tupla_un_item = tuple(("un elemento")) #-- This is not only one item
print(mi_tupla_un_item)
print("mi_tupla_un_item tiene " + str(len(mi_tupla_un_item)) + " elementos")


mi_tupla_un_item = tuple(("uno",)) #-- This is only one item
print(mi_tupla_un_item)
print("mi_tupla_un_item tiene " + str(len(mi_tupla_un_item)) + " elementos")


#-- The items can be of any datatype and mixed type
esto_es_una_lista = list([3,2,1])
print(type(esto_es_una_lista))
print(esto_es_una_lista)

mi_tupla_mezcla = tuple(("Tomeu", 34, True, 40.0, False, "a", "Sabater", esto_es_una_lista))
print(mi_tupla_mezcla)


#-- Tuples are objects in Python
print(type(mi_tupla_mezcla)) 


#--- ACCESS TUPLES #############################################
print("#--- ACCESS TUPLES #############################################")
print(mi_tupla_mezcla)
#-- You can access tuple items by referring to the index number, inside square brackets:
print(mi_tupla_mezcla[0]) #-- First element
print(mi_tupla_mezcla[1]) #-- Second element
print(mi_tupla_mezcla[2]) #-- And so on 
print(mi_tupla_mezcla[7])#-- This elementi is a list 

mi_tupla_mezcla[7].sort() #-- You can apply some action to some element of the tuple by its index
print(mi_tupla_mezcla)
print(mi_tupla_mezcla[7][0]) 


#-- Negative indexing means start from the end.
#-- -1 refers to the last item, -2 refers to the second last item etc.
print("in reverse order")
print("last element :" + str(mi_tupla_mezcla[-1]))
print("penultimate element :" + str(mi_tupla_mezcla[-2]))
print("antepenultimate element :" + str(mi_tupla_mezcla[-3]))


#-- You can specify a range of indexes by specifying where to start and where to end the range.
#-- In this case, the return value will be a new tuple with the specified items.
print("----------------")
print("mi_tupla_mezcla contains : " + str(len(mi_tupla_mezcla)) + " elements")
print(mi_tupla_mezcla)
print(mi_tupla_mezcla[2:5]) #-- Print a range, returns a new tuple, last index is excluded
print(mi_tupla_mezcla[0:len(mi_tupla_mezcla)]) #-- Print the tuple
print(mi_tupla_mezcla[:2]) #-- Print the first and second element
print(mi_tupla_mezcla[3:]) #-- Print from the fourth element
print(mi_tupla_mezcla[:]) #-- Print all the tuple
print(mi_tupla_mezcla[-4:-1]) #-- Print the last 3 elements (-3, -2, -1)
print(mi_tupla_mezcla[0:8])

#-- Check if item exists
#-- To determine if a specified item is present in a tuple use the "in" keyword

busca_item = list([1,2,3])
if busca_item in mi_tupla_mezcla: #-- Check for "Tomeu" in mi_tupla_mezcla tuple
    print("Yes, '" + str(busca_item) + "' is in the mi_tupla_mezcla")
else:
    print("No, '" + str(busca_item) + "' is NOT in the mi_tupla_mezcla")



#--- UPDATE TUPLES #############################################
print("#--- UPDATE TUPLES #############################################")
#-- Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.
#-- But there are some workarounds.

#-- Once a tuple is created, you cannot change its values. 
#-- Tuples are unchangeable, or immutable as it also is called.
#-- Workaround: You can convert the tuple into a list, change the list, and convert the list back into a tuple.
print(mi_tupla_mezcla)


mi_lista_mezcla = list(mi_tupla_mezcla) #-- Step1: Converts the tuple to list containing the same elements
print("this is a list :" + str(mi_lista_mezcla)) 

mi_lista_mezcla[5] = mi_lista_mezcla[5].upper() #-- Step2: Update the list, updating some value
print("this is a list :" + str(mi_lista_mezcla)) 

mi_tupla_mezcla = tuple(mi_lista_mezcla) #-- Step3: Converts the list to tuple 
print("this is a tuple :" + str(mi_tupla_mezcla))

mi_tupla_copia = mi_tupla_mezcla 
print(mi_tupla_copia)
print(mi_tupla_mezcla)

del mi_tupla_copia
print(mi_tupla_mezcla)

del mi_lista_mezcla #-- Removes the list, it is no longer necessary


#-- Since tuples are immutable, they do not have a built-in append() method, 
#-- but there are other ways to add items to a tuple.
print("--------- Ways to add items to a tuple ---- ")

# 1. Convert into a list, add the item(s), and convert it back into a tuple.

mi_lista_mezcla = list(mi_tupla_mezcla) #-- Convert to list
mi_lista_mezcla.append("Nuevo Item") #-- Add the item
mi_tupla_mezcla = tuple(mi_lista_mezcla) #-- Convert to tuple
del mi_lista_mezcla #-- Delete the list, it is no longer necessary
print(mi_tupla_mezcla)


#2. Add tuple to a tuple, create a new tuple with the item(s), and add it to the existing tuple
nueva_tupla = tuple(("b", False, 2)) #-- New tuple
mi_tupla_mezcla = mi_tupla_mezcla + nueva_tupla #-- Create a new tuple from two different tuples
print(nueva_tupla)
print(mi_tupla_mezcla)


mi_tupla_A = tuple(mi_tupla_mezcla[:7] + mi_tupla_mezcla[8:]) #-- Create a new tuple from a tuple
print(mi_tupla_A)


#-- Since tuples are immutable, You cannot remove items in a tuple.
#-- Tuples are unchangeable, so you cannot remove items from it, 
# -- but you can use the same workaround as we used for changing and adding tuple items
print("--- Workaround for removing elements from the tuple -----")


print(mi_tupla_mezcla) 
mi_lista_mezcla = list(mi_tupla_mezcla) #-- Creates a list from the tuple
mi_lista_mezcla.remove(34) #-- Remove an item from the list
mi_tupla_mezcla = tuple(mi_lista_mezcla) #-- Creates a tuple from the list
del mi_lista_mezcla #-- Remove the list, is is no longer necessary 
print(mi_tupla_mezcla)


#-- You can delete the tuple completely
print(mi_tupla_A)
del mi_tupla_A
# print(mi_tupla_A) #-- Raises an error, the tuple does not exist


#--- UNPACK TUPLES #############################################
print("#--- UNPACK TUPLES #############################################")

#-- When we create a tuple we assign values, this is the "packing"
mi_tupla_packing = tuple(("Manzana", "Pera", "Naranja", "Melón", "Plátano", "Sandía", "Aguacate")) #-- This is packing
(Manzana, Pera, *Varios) = mi_tupla_packing #-- the "*" collects the rest of the values, this is unpacking

print(Manzana)
print(Pera)
print(Varios) 

print("********************")
(tomeu, Ainara, *Varios, Sandia) = mi_tupla_packing #-- the "*" collects the rest of the values

print(mi_tupla_packing)
print(tomeu)
print(Ainara)
print(Varios) 
print(Sandia)

#--- LOOP TUPLES #############################################
print("#--- LOOP TUPLES #############################################")

#-- You can loop through the tuple items by using a for loop.
print("####using for in")
for fruta in mi_tupla_packing:
    print(fruta)

#-- You can also loop through the tuple items by referring to their index number.
print("####Using for with an index")
for i in range(len(mi_tupla_packing)):
    print(mi_tupla_packing[i])

#-- You can loop through the tuple items by using a while loop.
print("#####Using while")
i = 0 
while i < len(mi_tupla_packing):
    print(mi_tupla_packing[i])
    i+=1


#--- JOIN TUPLES #############################################
print("#--- JOIN TUPLES #############################################")

print(mi_tupla_mezcla)
print(mi_tupla_packing)

mi_tupla_total = tuple(mi_tupla_mezcla + mi_tupla_packing) 
print(mi_tupla_total)


#-- You can multiply tuples
mi_tupla_triple = tuple(mi_tupla_packing * 3) 
print(mi_tupla_triple)


#--- TUPLE METHODS #############################################
print("#--- TUPLE METHODS #############################################")

#-- Python has two built-in methods that you can use on tuples.
#-- count() and index()

#-- count() Returns the number of times a specified value occurs in a tuple
print("En mi_tupla_double 'Pera' aparece " + str(mi_tupla_triple.count('Pera')) + " veces")

#-- index() Searches the tuple for a specified value and returns the position of where it was found
print("Y 'Pera' está en la posición " + str(mi_tupla_triple.index('Pera')) + " la primera vez") 


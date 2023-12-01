'''
Created on 25 oct 2023

CESUR - Python Tutorial
@author: Tomeu Sabater
'''
#--- PYTHON LISTS #############################################
print("#--- PYTHON LISTS #############################################")
#-- List is a data type in Python.
#-- Lists are used to store multiple items in a single variable.
#-- List items can be of any data; str, int, boolean.  
#-- List is a collection which is ordered and changeable (change the value of any item). 
#-- List allows duplicate members.

mi_lista_texto = list(["manzana","pera","melón"]) # Create a list of values of type 'str'
print(mi_lista_texto)

mi_lista_numeros = list([1,2,3,4,5]) # Create a list of values of type 'int'
print(mi_lista_numeros)

mi_lista_mezcla = list([False,"a",1,"e",2,"i",3, True]) # Create a list of different type of values
print(mi_lista_mezcla)

print(type(mi_lista_mezcla)) #-- Prints the type of the list

#--- ACCESS Item ##################################
print("#--- ACCESS Item ##################################")
#-- List items are indexed and you can access them by referring to the index numer
print("#-- ACCESS specific Item")
print(mi_lista_texto)
print(mi_lista_texto[0])
print(mi_lista_texto[1]) #-- The index starts by 0, this prints the second element

print(mi_lista_texto)
print(mi_lista_texto[-1]) #-- Negative index means starts by the end
print(mi_lista_texto[-2])
print(mi_lista_texto[-3])

#-- You can specify a Range of indexes
#-- Specifiying a Range the result is a new list
print(mi_lista_mezcla)
print(mi_lista_mezcla[3:5]) #-- Last index is excluded. 
print(mi_lista_mezcla[3:]) #-- From the index 3 to the end
print(mi_lista_mezcla[:5]) #-- Until the index 5 excluded
print(mi_lista_mezcla[-4:-1]) #-- Remember, last item in a range is excluded 
print(mi_lista_mezcla[-4:]) #-- Remember, last item in a range is excluded 
print(mi_lista_mezcla[0:3])
print(mi_lista_mezcla[len(mi_lista_mezcla)-1]) #-- The last element / returns one element
print(mi_lista_mezcla[-1:10])
print("xxxxxxxxxxx")
print(mi_lista_mezcla[0:len(mi_lista_mezcla)]) #-- From first to the last element
print("xxxxxxxxxxx")

#-- List length
print("mi_lista_mezcla tiene " + str(len(mi_lista_mezcla)) + " elementos")

#--- CHECK for an Item ##################################
print("#--- CHECK for an Item ##################################")
#-- The index of the Item is not returned

fruta = str("MANZANA") #-- Check with pera, naranja, piña, etc. 
if (fruta.lower() in mi_lista_texto):
    print(fruta + " existe en la lista")
else:
    print(fruta + " no existe en la lista")

#--- CHANGE list Items ############################
print("#--- CHANGE list Items ############################")

#-- Change item value 
print(mi_lista_texto)
mi_lista_texto[2] = "naranja" #-- Change item value
print(mi_lista_texto)

#-- Change a range of item values
mi_lista_texto[0:2] = ["melocotón","piña"] #-- Change a range of items
print(mi_lista_texto)

#-- You can change and insert items at the same time
mi_lista_texto[0:1] = ["melicotó","pera"] #-- Change and insert items
print(mi_lista_texto)

#-- You can change and renove items at the same time
mi_lista_texto[1:3] = ["pera y piña"] #-- Change and remove items
print(mi_lista_texto)

#--- INSERT items in the list ############################
print("#--- INSERT items in the list ############################")
#-- we can use the insert() method.
print("#--INSERT List Items")
print(mi_lista_texto)
mi_lista_texto.insert(3, "watermelon")
print(mi_lista_texto)

mi_lista_texto.insert(0, "Guacamole")
print(mi_lista_texto)
print("xxxxxxxxxxxxxxxxxxxxxxxx")
mi_lista_texto.insert(-1, "manzanaxxxx")
print(mi_lista_texto)
print("xxxxxxxxxxxxxxxxxxxxxxxx")

#--- ADD list Items ############################
#To add an elemento to the end of the list we can use the .append()
print("#-- ADD List Items")
mi_lista_texto.append("plátano")
print(mi_lista_texto)

#--- REMOVE List Items ############################
print("#--- REMOVE List Items ############################")
print(mi_lista_texto)
mi_lista_texto.remove("pera y piña") #-- remove this element from the list
print(mi_lista_texto)
# mi_lista_texto.remove("pera y piña") #-- If elemento doesn't exist raises an error

mi_lista_texto.append("plátano") # Add platano at the end
print(mi_lista_texto)
mi_lista_texto.remove("plátano") # Remove first occurrence
print(mi_lista_texto)

#-- Remove from specified index 
print("#-- pop")
mi_lista_texto.pop(0) #-- Remove first element from the list
print(mi_lista_texto)

mi_lista_texto.pop(len(mi_lista_texto)-1) #-- Remove last element from the list
print(mi_lista_texto)

mi_lista_texto.pop() #-- Remove last elemento from the list
print(mi_lista_texto)

#-- The "del" keyword also removes the specified index
print("#--- del")
del mi_lista_texto[2]
print(mi_lista_texto)

# -- The del keyword can also delete the list completely.
del mi_lista_texto #-- Removes the list
# print(mi_lista_texto) #-- Raises an error because the list doesn't exist

#-- The clear() method empties the list.
print("#--- clear()")
print(mi_lista_numeros)
mi_lista_numeros.clear() #-- Empties the list
print(mi_lista_numeros) #-- List exists, is empy


#--- LOOP Lists ############################
#-- You can loop through the list items by using a for loop
print("#--- LOOP Lists ############################")
for elemento in mi_lista_mezcla:
    print(elemento)

#-- You can also loop through the list items by referring to their index number.
print("Range of \'mi_lista_mezcla\' is " + str(range(len(mi_lista_mezcla)))) #-- Show the range
for i in range(len(mi_lista_mezcla)):
    print(mi_lista_mezcla[i])

#-- Loop using a While Loop 
print("#------Using a While")
indice = int(0) #-- Index creation
while indice < len(mi_lista_mezcla):
    print(mi_lista_mezcla[indice])
    indice += 1

#--- LIST COMPREHENSION ############################
   
#-- Loop using List Comprehension 
#-- This system offers the shortest syntax for looping throug lists
print("#----- Using List Comprehension")
[print(elemento) for elemento in mi_lista_mezcla]

#-- You can create another list filtering the original list
nueva_lista_numerica = list([]) #-- Create an empty list 
nueva_lista_booleana = list([])
nueva_lista_other = list([])

for elemento in mi_lista_mezcla:
        if str(elemento).isnumeric(): #-- Check if the element is numeric
            nueva_lista_numerica.append(elemento)
        elif (elemento == True or elemento == False): #-- Check if the element is boolean
            nueva_lista_booleana.append(elemento)
        else:
            nueva_lista_other.append(elemento)
                       
print(nueva_lista_numerica)
print(nueva_lista_booleana)
print(nueva_lista_other)

#-- Let's do the same thing with one line of code using List Comprehension
#-- Syntax of List Comprehension is
#-- newlist = [(expression) for (item) in (iterable) if (condition == True)]
#-- The CONDITION is like a filter that only accepts the items that valuate to True.
#-- The ITERABLE can be any iterable object, like a list, tuple, set etc.
#-- The EXPRESION is the current ITEM in the iteration, but it is also the outcome, 
#    which you can manipulate before it ends up like a list item in the new list:

nueva_lista_numerica.clear() #-- Emtpies the list 
nueva_lista_booleana.clear()
nueva_lista_other.clear() 

nueva_lista_numerica = [(elemento * 10) for elemento in mi_lista_mezcla if str(elemento).isnumeric()]
nueva_lista_booleana = [elemento for elemento in mi_lista_mezcla if (elemento == True or elemento == False)] #-- I get a "bug"
nueva_lista_booleanaNot = list([not(elemento) for elemento in mi_lista_mezcla if (elemento == True or elemento == False)]) #-- I get a "bug"
nueva_lista_other = [elemento for elemento in mi_lista_mezcla if not(str(elemento).isnumeric())]


print("#--- List comprehension")
print(mi_lista_mezcla)
print(nueva_lista_numerica)
print(nueva_lista_booleana)
print(nueva_lista_booleanaNot)
print(nueva_lista_other)

def quitaTildes(fruta):
    #-- Swap vocal con tilde a vocal sin tilde
    fruta = fruta.replace('á','a')
    fruta = fruta.replace('é','e')
    fruta = fruta.replace('í','i')
    fruta = fruta.replace('ó','o')
    fruta = fruta.replace('ú','u')
    return(fruta)

lista_frutas = list(['pera','manzana','melón', "limón","sandía"])
nueva_lista_frutas = list([quitaTildes(fruta).upper() for fruta in lista_frutas])

print(lista_frutas)
print(nueva_lista_frutas)


#--- SORT LIST ############################
print("#--- SORT LIST ############################")
# List objects have a sort() method that will sort the list alphanumerically, ascending, by default:

lista_frutas.sort()
print(lista_frutas) #-- print the list sorted ascending

#-- Create 100 random numbers and order them, numbers from 0..99

import random  #-- First, you need to import the built-in module to use it

mi_lista_100 = list([]) #-- Crate the list
for i in range(100):
    mi_lista_100.append(int(random.randrange(1, 1000)))

print("La lista tiene : " + str(len(mi_lista_100)) + " elementos")
print(mi_lista_100) #-- Original list
mi_lista_100.sort()
print(mi_lista_100) #-- list ordered ASC

#-- Order in descendig
mi_lista_100.sort(reverse = True) #-- Reverse flag 
print(mi_lista_100) #-- list ordered DES


#-- Case Sensitive
#-- By default the sort() method is case sensitive, 
#-- resulting in all capital letters being sorted before lower case letters:
#-- Luckily we can use built-in functions as key functions when sorting a list.

#-- First we will update some items 

#-- Let analyze how to transform the first character to uppercase
nueva_fruta = str("naranja")

# nueva_fruta[0] = nueva_fruta[0].upper() #-- No funciona
nueva_fruta = nueva_fruta[0].upper() + nueva_fruta[1:]
print(nueva_fruta) 

#-- para un elemento específico de una lista de elementos
print(lista_frutas)
nueva_fruta = lista_frutas[2][0].upper() + lista_frutas[2][1:]
print(nueva_fruta)


#-- Lo mismo, o similar, pero para todos los elementos de una lista
#-- Utilizando un loop de la lista
nueva_lista_frutas_1M = list([])
for i in range(len(lista_frutas)):
    nueva_lista_frutas_1M.append(lista_frutas[i][0].upper() + lista_frutas[i][1:])
print(nueva_lista_frutas_1M)

#-- ahora lo haremos mediante comprehension 

#-- primero la recorremos sin alterar los elementos
nueva_lista_frutas_1M = list([fruta for fruta in lista_frutas])
print(nueva_lista_frutas_1M)

#-- ahora manipulamos el elemento para que la genere como deseamos
nueva_lista_frutas_1M = list([(fruta[0].upper() + fruta[1:].lower()) for fruta in lista_frutas])
print(nueva_lista_frutas_1M)

#-- Y ahora concatenamos las dos listas
nueva_lista_frutas_mezcla = list([])
nueva_lista_frutas_mezcla = lista_frutas #-- No funciona, son la misma lista "OBJETOS", se ve en breve

nueva_lista_frutas_mezcla = list([fruta for fruta in lista_frutas]) #-- Así sí funciona
print(nueva_lista_frutas_mezcla)

nueva_lista_frutas_mezcla = list(lista_frutas) #-- Así también funciona
print(nueva_lista_frutas_mezcla)
# nueva_lista_frutas_mezcla.append([fruta for fruta in nueva_lista_frutas_1M]) # No funciona
[nueva_lista_frutas_mezcla.append(fruta) for fruta in nueva_lista_frutas_1M] #-- Así, sí que funciona
print(nueva_lista_frutas_mezcla)

#-- Ahora ya podemos ordenarlo sin tener en cuenta las Mayúsculas / Minúsculas
nueva_lista_frutas_mezcla.sort(key = str.lower)
print(nueva_lista_frutas_mezcla)

#-- Reverse order
nueva_lista_frutas_mezcla.reverse()
print(nueva_lista_frutas_mezcla)


#--- COPY LIST ############################ A
print('#--- COPY LIST ############################')
#-- You can not copy a list by list1 = list2, 
# because the name of the list is not the list, is a pointer to the list (OBJECT)
# The list is  placed in memory and the name of the list is a pointer to the memory when the list is

#-- Example
mi_lista_copy = nueva_lista_frutas_mezcla #-- Now, both name list point to the same list (Object)
print(mi_lista_copy)
print(nueva_lista_frutas_mezcla)


# mi_lista_copy.clear() #-- This will empty the list which "mi_lista_copy" points
print(mi_lista_copy) 
print(nueva_lista_frutas_mezcla)


#-- Copy a list by generatign a new list 
print("----------------")
mi_lista_copy = nueva_lista_frutas_mezcla.copy()
print(mi_lista_copy)
mi_lista_copy.clear() #-- Empties the list 
print(mi_lista_copy)
print(nueva_lista_frutas_mezcla)


#-- Another way to make a copy is to use the built-in method list().
mi_lista_copy = list(nueva_lista_frutas_mezcla)
print(mi_lista_copy)
mi_lista_copy.clear()
print(mi_lista_copy)
print(nueva_lista_frutas_mezcla)


#--- JOIN LIST ############################
print("#--- JOIN LIST ############################")
#-- There are several ways to join, or concatenate, two or more lists in Python.

#-- One of the easiest ways are by using the + operator.
print(lista_frutas)
print(nueva_lista_frutas_1M)

lista_concat = list(lista_frutas + nueva_lista_frutas_1M) 
print(lista_concat)


# Another way to join two lists is by appending all the items from list2 into list1, one by one:
lista_concat.clear() #-- Empties the list 
print(lista_concat)

for fruta in lista_frutas:
    lista_concat.append(fruta)
for fruta in nueva_lista_frutas_1M:
    lista_concat.append(fruta)
    
print(lista_concat)


#-- Or you can use the extend() method, 
#   where the purpose is to add elements from one list to another list
print(lista_frutas)
print(nueva_lista_frutas_1M)


lista_frutas.extend(nueva_lista_frutas_1M)
print(lista_frutas)
print(nueva_lista_frutas_1M)


#--- LIST METHODS SUMMARY ############################
print('''
append()   Adds an element at the end of the list
clear()    Removes all the elements from the list
copy()    Returns a copy of the list
count()    Returns the number of elements with the specified value
extend()    Add the elements of a list (or any iterable), to the end of the current list
index()    Returns the index of the first element with the specified value
insert()    Adds an element at the specified position
pop()    Removes the element at the specified position
remove()    Removes the item with the specified value
reverse()    Reverses the order of the list
sort()    Sorts the list
''')

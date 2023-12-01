'''
Created on 10 nov 2023
CESUR - Python Tutorial
@author: Tomeu Sabater 
'''

#--- PYTHON SETS #############################################
print("#--- PYTHON SETS #############################################")
# Sets are used to store multiple items in a single variable.
# Set is one of 4 built-in data types in Python used to store collections of data: 
# List, Tuple, Set and Dictionary 
# A set is a collection which is unordered, unchangeable*, and unindexed.
# *Set items are unchangeable, but you can remove items and add new items.

mi_set = set({"Windows", "Linux", "MacOS"})#-- set creation 
print(mi_set) #-- Sets are unordered, so you cannot be sure in which order the items will appear.
print(mi_set)
print(mi_set)
print(mi_set)


#-- Set items are unordered, unchangeable, and do not allow duplicate values.

# Unordered means that the items in a set do not have a defined order, therefore
# Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

# Unchangeable, meaning that we cannot change the items after the set has been created.
# Once a set is created, you cannot change its items, but you can remove items and add new items.

# Duplicates Not Allowed, Sets cannot have two items with the same value.
# Duplicate values will be ignored:
mi_set = set({"Windows", "Windows", "Linux", "Linux", "MacOS", "Windows", "MacOS"})#-- set creation with duplicates
print(mi_set)

mi_set_boolean = set({0, str(int(1)), True, int(1), True, 1, False, int(0), False}) #-- O/False, 1/True are the same value 
print(mi_set_boolean)


#--- SET LENGTH #############################################
#-- Getting the lenght of the set
#-- To determine how many items a set has, use the len() function.
print("#--- SET LENGTH #############################################")
print("mi_set_boolean has : " + str(len(mi_set)) + " elements")
print(len(mi_set))



#--- SET CONTENT #############################################
#-- Set items can be of any datatype
print("#--- SET CONTENT #############################################")
mi_set_mezcla = set({True, False, 0, 1, "Hola", 2.0, 'a'})
print(mi_set_mezcla)


#-- Set is an object
print(type(mi_set_mezcla))


#--- ACCESS SET ITEMS / LOOP SETS #############################################
print("#--- ACCESS SET ITEMS / LOOP SETS #############################################")

# You cannot access items in a set by referring to an index or a key, because they are unordered
# But you can loop through the set items using a for loop, or ask if a specified value is present in a set, 
# by using the "in" keyword.

for elemento in mi_set: #-- Loop through the set items
    print(elemento)

mi_so = str("Windows") 
if (mi_so in mi_set): #-- Ask for specified value in the set 
    print("Yes \"" + mi_so + "\" is in mi_set")


#--- ADD SET ITEMS #############################################
print("#--- ADD SET ITEMS #############################################")

#-- Once a set is created, you cannot change its items, but you can add new items.
#-- To add one item to a set use the add() method.
print(mi_set)
mi_set.add("Android") #-- Add new item, the position is unknown
print(mi_set)

#-- You can add items from another set of items as concatenation has no sense in sets. 
#-- Resulting set contains no dupplicate values. 
mi_set_SO = set({"Chrome OS", "Solaris", "CP/M", "Windows"})
print(mi_set_SO)
print(mi_set)
mi_set_SO.update(mi_set)
print(mi_set_SO)

#-- You can add (with .update()) any iterable set

#-- Create a set of 100 random elements 
import random 
mi_lista_100 = list([]) #-- Crates the list empty
for i in range(100):
    mi_lista_100.append(int(random.randrange(1, 100))) #-- add 100 random elements to the list
print(mi_lista_100) #-- With duplicates

mi_set_100 = set({}) #-- Creates de set empty
mi_set_100.update(mi_lista_100) #-- Transform to set, and removes duplicates
print(mi_set_100)
print("mi_set_100 with no duplicates has " + str(len(mi_set_100)) + " elements") 


#--- REMOVE SET / REMOVE SET ITEMS / LOOP THE SET #############################################
print("#--- REMOVE SET ITEMS #############################################")
#-- Remove Set Items 
#-- To remove an item in a set, use the remove(), or the discard() method.

'''
for elemento in mi_set_100:
    if ((elemento % 2) == 0): #-- Even number
        mi_set_100.remove(elemento)


'''
for elemento in range(10, 100, 10): #-- 10, 20, 30, etc.
    if elemento in mi_set_100:
        mi_set_100.remove(elemento) #-- If the item to remove does not exist, remove() will raise an error.
print(mi_set_100)
print("mi_set_100 with no duplicates has " + str(len(mi_set_100)) + " elements") 

for elemento in range(0, 100, 2): #-- 2, 4, 6, 8, etc.
        mi_set_100.discard(elemento) #-- If the item to remove does not exist, remove() will NOT raise an error.

print(mi_set_100)
print("mi_set_100 with no even numbers has " + str(len(mi_set_100)) + " elements") 

#-- Clear method empties the set 
#-- The "del" keyword will delete the set completely:

mi_set_100.clear()
print(mi_lista_100)
print("mi_set_100 has " + str(len(mi_set_100)) + " elements") 


del mi_set_100 #-- Deletes de set. 
# print(mi_set_100) #-- This will raise an error as the set does not exist anymore 



#--- LOOP SETS #############################################
print("#--- LOOP SETS #############################################")
#-- You can loop through the set items by using a for loop:

print(mi_set) #-- This is the set to print
for elemento in mi_set:
    print(elemento)


#--- JOIN SETS #############################################
print("#--- JOIN SETS #############################################")
#-- There are several ways to join two or more sets in Python
#-- union() method that returns a new set containing all items from both sets
#-- update() method that inserts all the items from one set into another
#-- As the set does not contain any duplicate, both union() and update() will exclude any duplicate items.

mi_set1 = set({"a", "b" ,"c", 1}) #-- set creation
mi_set2 = set({1, 2, 3})  #-- set creation

mi_set3 = set(mi_set1.union(mi_set2)) #-- returns a new set containing all items. Original sets are untouched
print(mi_set1)
print(mi_set2)
print(mi_set3)


mi_set1.update(mi_set2) #-- inserts all the items from one set into another
print(mi_set1) #-- mi_set1 now contains the elements from both sets. 


#-- Keep ONLY the Duplicates
#-- The intersection() method will return a new set, that only contains the items that are present in both sets.
#-- The intersection_update() method will keep only the items that are present in both sets.
print("Keep ONLY the Duplicates")
mi_lista_100_1 = list([]) #-- Crates the first list empty
for i in range(100):
    mi_lista_100_1.append(int(random.randrange(1, 100)))
    
mi_set_100_1 = set({}) #-- Creates de set empty
mi_set_100_1.update(mi_lista_100_1) #-- Transform to set, and removes duplicates
print(mi_set_100_1)

mi_lista_100_2 = list([]) #-- Crates the second list empty
for i in range(100):
    mi_lista_100_2.append(int(random.randrange(1, 100)))
    
mi_set_100_2 = set({}) #-- Creates de set empty
mi_set_100_2.update(mi_lista_100_2) #-- Transform to set, and removes duplicates
print(mi_set_100_2)

mi_set_100_3 = mi_set_100_1.intersection(mi_set_100_2) #-- Only the items in both sets
print(mi_set_100_3) 

mi_set_100_1.intersection_update(mi_set_100_2) #-- Only the items present in both sets
print(mi_set_100_1)


#-- Keep All, But NOT the Duplicates
#-- The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.
#-- The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.
print("Keep All, But NOT the Duplicates")

mi_lista_100_1 = list([]) #-- Crates the first list empty
for i in range(100):
    mi_lista_100_1.append(int(random.randrange(1, 100)))
mi_set_100_1 = set({}) #-- Creates de set empty
mi_set_100_1.update(mi_lista_100_1) #-- Transform to set, and removes duplicates
print(mi_set_100_1)

mi_lista_100_2 = list([]) #-- Crates the second list empty
for i in range(100):
    mi_lista_100_2.append(int(random.randrange(1, 100))) #-- Transform to set, and removes duplicates 
mi_set_100_2 = set({}) #-- Creates de set empty
mi_set_100_2.update(mi_lista_100_2) #-- Transform to set, and removes duplicates
print(mi_set_100_2)

mi_set_100_3 = mi_set_100_1.symmetric_difference(mi_set_100_2) #-- Only the items NOT in both sets
print(mi_set_100_3) 

mi_set_100_1.symmetric_difference_update(mi_set_100_2)
print(mi_set_100_1) 

#-- Note: The values True and 1 are considered the same value in sets, and are treated as duplicates

mi_set_x = {0, "apple", "banana", "cherry", True}
mi_set_y = {"google", 1, "apple", 2, False}

mi_set_z = mi_set_x.symmetric_difference(mi_set_y)
print(mi_set_z)

#--- SETS METHODS #############################################
print("#--- SET METHODS #############################################")

#-- Python has a set of built-in methods that you can use on sets.

print('''
add()      Adds an element to the set
clear()    Removes all the elements from the set
copy()     Returns a copy of the set
difference()           Returns a set containing the difference between two or more sets
difference_update()    Removes the items in this set that are also included in another, specified set
discard()         Remove the specified item
intersection()    Returns a set, that is the intersection of two other sets
intersection_update()    Removes the items in this set that are not present in other, specified set(s)
isdisjoint()    Returns whether two sets have a intersection or not
issubset()      Returns whether another set contains this set or not
issuperset()    Returns whether this set contains another set or not
pop()       Removes an element from the set
remove()    Removes the specified element
symmetric_difference()           Returns a set with the symmetric differences of two sets
symmetric_difference_update()    inserts the symmetric differences from this set and another
union()    Return a set containing the union of sets
update()   Update the set with the union of this set and others
''') 


'''
Created on 23 nov 2023
CESUR - Python Tutorial
@author: Tomeu Sabater 
'''
#--- PYTHON DICTIONARIES #############################################
print("#--- PYTHON DICTIONARIES #############################################")
# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
# As of Python version 3.7, dictionaries are ordered. 
# In Python 3.6 and earlier, dictionaries are unordered.
# Dictionaries are written with curly brackets, and have keys and values:

# Dictionary Example
my_car = dict({
  "brand": "Ford", #-- You can put here a comment
  "model": "Fiesta",
  "year": 2015,
  "manual": False
}) 
print(my_car)

#--- DICTIONARY ITEMS #############################################
print("#--- DICTIONARY ITEMS #############################################")
# Dictionary items are ordered, changeable, and does not allow duplicates.
# Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

print(my_car["brand"])
print(my_car["model"])
print(my_car["year"])
print(my_car["manual"])


#--- DUPLICATES #############################################
print("#--- DUPLICATES #############################################") 
# Duplicates are not allowed in Dictionaries

my_car = dict({
  "brand": "Ford", #-- You can put here a comment
  "model": "Fiesta",
  "year": 2015,
  "manual": False,
  "brand": "Renault",
  "model": "clio",
  "year": 2020,
  "manual": True
}) 
print(my_car)


#--- DICTIONARY LENGTH #############################################
print("#--- DICTIONARY LENGTH #############################################")
# To determine how many items a dictionary has, use the len() function

print("my_car dictionary has : " + str(len(my_car)) + " elements")


#--- DICTIONARY ITEM DATA TYPE #############################################
# The values in dictionary items can be of any data type

my_car = dict({
  "brand": "Ford", 
  "model": "Fiesta",
  "year": 2015,
  "manual": False,
  "color" : list(["black", "white"])
}) 
print(my_car)

#-- The dictiorany is an object
print(type(my_car))



print('''
Python Collections (Arrays)
There are four collection data types in the Python programming language:

- List is a collection which is ordered and changeable. Allows duplicate members.
- Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
- Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
- Dictionary is a collection which is ordered** and changeable. No duplicate members.
*Set items are unchangeable, but you can remove and/or add items whenever you like.
**As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
''') 


#--- DICTIONARY ACCESS ITEMS #############################################
print("DICTIONARY ACCESS ITEMS #############################################")
# You can access the items of a dictionary by referring to its key name, inside square brackets:

print(my_car["brand"])
print(my_car["model"])
print(my_car["year"])
print(my_car["manual"])
print(my_car["color"])
print(my_car["color"][0])


#-- There is also a method called get() that will give you the same result:
print(my_car.get("model")) 
print(my_car.get("year")) 

#-- The keys() method will return a list of all the keys in the dictionary.
print(my_car.keys())


#-- Get Items
#-- The items() method will return each item in a dictionary, as tuples in a list.

print(my_car.items())

#-- Check if Key Exists
#  To determine if a specified key is present in a dictionary use the "in" keyword:

if "model" in my_car:
    print("Yes, 'model' is one of the keys in the my_car dictionary")


#--- DICTIONARY CHANGE ITEMS #############################################
print("DICTIONARY CHANGE ITEMS #############################################")

#-- You can change the value of a specific item by referring to its key name:
my_car["year"] = 2021
print(my_car)


#-- The update() method will update the dictionary with the items from the given argument.
#-- The argument must be a dictionary, or an iterable object with key:value pairs.
my_car.update({"year": 2020})
print(my_car)

#--- DICTIONARY ADD ITEMS #############################################
print("DICTIONARY ADD ITEMS #############################################")

print(my_car)
my_car["seats"] = 5 #-- Add a new elemento 
print(my_car)


#-- The update() method will update the dictionary with the items from a given argument. 
#-- If the item does not exist, the item will be added.

my_car.update({"year":2015})
print(my_car)

my_car.update({"abc":22222})
print(my_car)

print(my_car["color"][0])
my_car["color"][0] = "Red"
print(my_car)


#my_car.update({["color"][0]:"Andy"})
#print(my_car)
#my_car.update({ "color"[0]  : "Yellow"})
#print(my_car)

#print(my_car["color"][0])

#--- DICTIONARY REMOVE ITEMS #############################################
print("DICTIONARY REMOVE ITEMS #############################################")
#-- There are several methods to remove items from a dictionary

#-- The pop() method removes the item with the specified key name:
print(my_car)
my_car.pop("year")
print(my_car)

#-- The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
print(my_car)
my_car.popitem() #-- Removes the last inserted item
print(my_car)


#-- The del keyword removes the item with the specified key name:
print(my_car)
del my_car["color"]
print(my_car)

#-- The clear() method empties the dictionary:
my_car.clear() #-- Empties de dictionary
print(my_car)


#-- The del keyword can also delete the dictionary completely:
del my_car #-- Deletes the dictionary
# print(my_car)


#--- DICTIONARY LOOP #############################################
print("DICTIONARY LOOP #############################################")

#-- You can loop through a dictionary by using a for loop.
#-- When looping through a dictionary, the return value are the keys of the dictionary, 
#-- but there are methods to return the values as well.

my_car = dict({
  "brand": "Ford", 
  "model": "Fiesta",
  "year": 2015,
  "manual": False,
  "color" : list(["black", "white"])
}) 
print(my_car)

for elemento in my_car:
    print(elemento) #-- prints the keys
    
for elemento in my_car:
    print(my_car[elemento]) #-- prints the items

for elemento in my_car.values(): 
    print(elemento) #-- prints the items

for elemento in my_car.keys(): 
    print(elemento) #-- prints the keys

for elemento in my_car.items(): 
    print(elemento) #-- prints the keys and values


#--- COPY DICTIONARIES #############################################
print("DICTIONARY COPY #############################################")

#-- You cannot copy a dictionary simply by typing dict2 = dict1, 
#-- because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.

my_car2 = my_car #-- copy pointer to the same object
my_car2["year"] = 1111 #-- We update the year value
print(my_car)
print(my_car2)

# del my_car #-- Deletes the pointer
print(my_car2)  #-- Pointer to the original object, so we're not copying the object


#-- There are ways to make a copy, one way is to use the built-in Dictionary method copy().
my_car2 = my_car.copy() #-- Now we've two different objects
my_car2.pop("year")
print(my_car) 
print(my_car2)


#-- Another way to make a copy is to use the built-in function dict().
my_car3 = dict(my_car) #-- We've two different objects 
my_car.pop("brand")
my_car2.popitem()
print(my_car)
print(my_car2)
print(my_car3)


#--- NESTED DICTIONARIES #############################################
print("NESTED DICTIONARIES #############################################")

my_cars = {
    "car1" : {
            "brand": "Ford", 
            "model": "Fiesta",
            "year": 2015,
            "manual": False,
            "color" : list(["black", "white"])
            },
    "car2" : {
            "brand": "Renault", 
            "model": "Clio",
            "year": 2020,
            "manual": True,
            "color" : list(["red", "white"])
            },
    "car3" : {
            "brand": "Opel", 
            "model": "Astra",
            "year": 2021,
            "manual": False,
            "color" : list(["black", "yellow"])
            }
} 
print(my_cars)


#-- Another way is the creation of dictionaries and add them to a new one. 
coche1 = {
        "brand": "Ford", 
        "model": "Fiesta",
        "year": 2015,
        "manual": False,
        "color" : list(["black", "white"])
        }

micoche2 =  {
        "brand": "Renault", 
        "model": "Clio",
        "year": 2020,
        "manual": True,
        "color" : list(["red", "white"])
        }

miotrocoche = {
        "brand": "Opel", 
        "model": "Astra",
        "year": 2021,
        "manual": False,
        "color" : list(["black", "yellow"])
        }


my_cars = {
    "car1": coche1,
    "car2": miotrocoche,
    "car3": micoche2
}
print(my_cars)

#-- Access Items in Nested Dictionaries
print(my_cars["car3"]["model"]) #-- The model value of car3
print(my_cars["car2"]["color"][1]) #-- Firts color of car2


#--- DICTIONARY METHODS #############################################
print("DICTIONARY METHODS #############################################")


print('''
clear()   Removes all the elements from the dictionary
copy()    Returns a copy of the dictionary
fromkeys()    Returns a dictionary with the specified keys and value
get()    Returns the value of the specified key
items()  Returns a list containing a tuple for each key value pair
keys()   Returns a list containing the dictionary\'s keys
pop()    Removes the element with the specified key
popitem()       Removes the last inserted key-value pair
setdefault()    Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()    Updates the dictionary with the specified key-value pairs
values()    Returns a list of all the values in the dictionary
''')


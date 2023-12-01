'''
Created on 24 oct 2023

CESUR - Python Tutorial
@author: Tomeu Sabater
'''

#--- PYTHON BOOLEANS #########################################################

#-- Booleans are one of two values: True / False
print(5 > 3) #-- This is True
print(5 < 3) #-- This is False
print(5 < 5) #-- This is False
print (5 == 5) #-- Thi is True

#-- In IF statements, python returns True o False
if (5 > 3):
    print("True: 5 > 3")
else:
    pass

if (5 < 3):
    pass
else:
    print("False: 5 < 3")

#-- Evaluate values and Variables
print(bool("Tomeu")) #-- This is True
print(bool(10)) #-- This is True
print(bool(0)) #-- This is False
print(bool(False)) #-- This is False
print(bool("")) #--This is False

mi_variable_string = str("") #-- Valor vacío a una variable. 
if (bool(mi_variable_string)):
    pass
else:
    print("Error, no puede contener un valor vacío")

#-- Functions can return True/False

def myFunction():
    return True

print(myFunction())

if myFunction():
    print("YES")
else:
    pass

    



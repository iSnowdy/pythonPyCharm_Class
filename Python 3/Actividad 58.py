# Actividad 58 - Sin usar el ordenador, indica cuál es el resultado y el tipo de las siguientes expresiones.
# Luego verifica las respuestas con la consola o el IDE:

a = (2, 10, 1991)
b = (25, 12, 1990)
c = ('Donald', True, b)
x, y = ((27, 3), 9)
z, w = x
v = (x, a)

'''
1. a < b ---> True B
2. y + w ---> 12 B
3. x + a ---> 27, 3, 2, 10, 1991 B
4. len(v) ---> 2 B
5. v[1][1] ---> 10 B
6. c[0][0] ---> Donald X
7. z, y ---> 27, 9 B
8. a + b[1:5] ---> (2,10,1991), (12, 1990) X  
9. (a + b)[1:5] --->  X
10. str(a[2]) + str(b[2]) ---> 19911990
11. str(a[2] + b[2]) ---> '2' + 1990 X sumas
12. str((a + b)[2]) ---> 1991 B
13. str(a + b)[2] ---> X es la ,
'''

print('Resultados\n')


print(a < b)
print(y + w)
print(x + a)
print(len(v))
print(v[1][1])
print(c[0][0])
print(z, y)
print(a + b[1:5])
print((a + b)[1:5])
print(str(a[2]) + str(b[2]))
print(str(a[2] + b[2]))
print(str((a + b)[2]))
print(str(a + b)[2])

print('\nPruebas\n')

print(str(a+b)[0])
print(str(a+b)[1])
print(str(a+b)[2])

'''
prueba = str(a + b)[0]
print(prueba)
prueba = str(a + b)[2]
print(prueba)
'''

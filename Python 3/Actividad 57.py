# Actividad 57 - Sin usar el ordenador, indica el resultado. Luego comprueba.

a = [5, 1, 4, 9, 0]

# b = range(3, 10) + range(20, 23)

c = [[1, 2], [3, 4, 5], [6, 7]]

d = ['perro', 'gato', 'jirafa', 'elefante']

e = ['a', a, 2 * a]

'''
1. a[2] ---> 4 B
2. b[9] ---> B
3. c[1][2] ---> 2 X 
4. e[0] == e[1] ---> False B 
5. len(c) ---> 3 B
6. len(c[0]) ---> 2  B
7. len(e) ---> 3 B
8. c[-1] ---> [6, 7] B
9. c[-1][+1] ---> 7 B
10. c[2:] + d[2:] ---> 6, 7 + jirafa y elefante B 
11. a[3:10] ---> [9, 0] B
12. a[3:10:2] --->  X
13. d.index('jirafa') ---> 2 B 
14. e[c[0][1]].count(5) ---> 0  X
15. sorted(a)[2] ---> [0, 4, 9] X
16. complex(b[0], b[1]) --->  X
'''

print('Respuestas')

print(a[2])
# print(b[9])
print(c[1][2])
print(e[0] == e[1])
print(len(c))
print(len(c[0]))
print(len(e))
print(c[-1])
print(c[-1][+1])
print(str(c[2:]) + d[2])
print(a[3:10])
print(a[3:10:2])
print(d.index('jirafa'))
print(e[c[0][1]].count(5))
print('Hola', sorted(a)[2])
# print(complex(b[0], b[1]))

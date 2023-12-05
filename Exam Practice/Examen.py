

1.

# R: p = 20

2.

x = input()
if x == 4:
    print('Hola')
else:
    print('Adios')

# R: Adios

3.

x = 26
if x % 2 == 0:
    print('0')
else:
    print('1')

# R: 0

4.

x = 17
y = 26
if x <= 17 or y > 40:
    print('1')
elif x < 17:
    print('2')
else:
    print('3')

# R: 1

5.

x = 7

if x!= 10:
    print('#')
    if x < 8:
        print('#')
    elif x == 10:
        print('#')
    else:
        print('#')
else:
    print('#'*3)

# R: 2

6.

float(4)

# R: 4.0

7.

import math

radio = float(input()) # 0

print(math.pi*radio**2, 2*math.pi*radio)

# R: 0, 0

8.

x = 1
while x < 4:
    x += 2
    print(x)

# R: 3, 5

9.

x = 0
while x <= 3:
    print(x)
    x =+ 2

# R: 0, 2

'''

10.

i = 1
j = 1

while i < 6:
    i += j + 1
    if i == 3:
    print(i)

# R: Mia: fallo por indentación del if. Alternativa: 3 (suponiendo que el print del if estuviera bien indentado)

'''

11.

for i in range(10, 7, -1):
    print(i)

# R: 10, 9, 8

12.

for i in range(1, 2, 1):
    print(i)

# R: 1

13.

for i in range(15):
    print(i)

# R: 0...14

14.

i = range(7, 15, 2)

for j in range(i):
    print(i)

# R: 7, 9, 11, 13

15.

for i in range(i):
    for j in range(2):
        print(i, j)

# R: 0 0 \n 0 1

16.

a = ['sistemas', 'bases', 'fol']

for i in a:
    if 'sistemas' in a:
        print(i)

# R: sistemas, bases, fol

17.

li = [1, 2, 3, 4]

print(li[1:3])

# R: 2, 3

18.

li = [1, 2, 3, 4]

li[2] = 5
print(li)

# R: [1, 2, 5, 4]

19.

li = [0, 1, 2, 3]
a = len(li)
print(a)

# R: 4

20.

li = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['#', 0, '@']]
print(li[2][1])

# R: 8

21.

d = {1: 'A', 2: 'B'}
for v in d.values():
    print(v)

# 'A', 'B'

22.

futbolistas = {} # muy largo paso

keys = futbolistas.keys()
print(keys) # sacaría por pantalla todas las keys que son los números

# R: (1, 15...)

23.

print(len(futbolistas))

# 11

24.


def f(a, b=5):

    return a * b


print(f(2))

# R: 10

25.

a = [1, 2, 3]


def f(a):

    s = 0
    for i in a:
        s += 1
    return s


print(f(a))

# R: 6




























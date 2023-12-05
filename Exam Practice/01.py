'''

# 1. ¿Cuántos '#' se mostrarán después de ejecutarse el siguiente fragmento de código?

# R: 2

x = 7

if x != 10:
    print('#') # 1

    if x < 8:
        print('#') # 2

    elif x == 10:
        print('#')

    else:
        print('#')

else:
    print('#'*3)

# 2. ¿Qué mostrará la consola después de ejecutarse el siguiente fragmento de código?

# R: 2

x = 17
y = 26

if x < 18 and y > 40:
    print("1")

elif x < 18:
    print("2")

else:
    print("3")

# 3. ¿Qué mostrará la consola después de ejecutarse el siguiente fragmento de código
# si el usuario introduce un 4?

# R: Hola X --> input siempre es como string


x = input()

if x == 4:
    print("Hola")

else:
    print("Adios")


# 4. ¿Cuánto vale p al terminar las iteraciones del siguiente diagrama de flujo?

# R: 20

# 5. ¿Qué mostrará la consola después de ejecutarse el siguiente fragmento de código?

# R: 2

x = 17
y = 26

if x < 18 and y > 40:
    print("1")

elif x < 18:
    print("2")

else:
    print("3")

# 6. ¿Cuál será el resultado exacto de la siguiente operación?

float(4)

# R: nada (4.0)

# 7. ¿Qué mostrará la consola después de ejecutarse el siguiente fragmento de código?

# R: 1

x = 18

if x <= 18:
    print("1")

if x >= 25:
    print("2")

else:
    print("3")

# 8. ¿Qué mostrará la consola después de ejecutarse el siguiente fragmento de código?

# R: 0, 2

x = 0

while x < 3:
    print(x)
    x += 2

# 9. ¿Qué mostrará exactamente la consola después de ejecutarse el siguiente
# fragmento de código si el usuario introduce un 0?

# R: 0, 0



import math

radio = float(input())
print(math.pi*radio**2,2*math.pi*radio)



# 10. ¿Qué mostrará la consola después de ejecutarse el siguiente fragmento de código?

# R: 3, 5

x = 1

while x < 4:
    x += 2
    print(x)

# 11. ¿Qué mostrará la consola después de ejecutarse el siguiente fragmento de código?

# R: 3, 6

x = 0

while x < 5:
    x += 3
    print(x)

# 12. ¿Qué mostrará la consola después de ejecutarse el siguiente fragmento de código?

# R: 10, 9, 8

for i in range(10, 7, -1):
    print(i)

# 13. ¿Qué mostrará la consola después de ejecutarse el siguiente fragmento de código?

# R: 1

for i in range(1, 2, 1):
    print(i)

# 14. ¿Qué mostrará la consola después de ejecutarse el siguiente fragmento de código?

# R: 1, 1 X --> 0 0 \n 0 1 /// i columnas ( 0 a 1; 2) de 0 a j -1 (0 a 1)

for i in range(1):
    for j in range(2):
        print(i, j)

# 15. ¿Qué mostrará la consola después de ejecutarse el siguiente fragmento de código?

# R: 0, 0 \n 0, 1 \n 0, 2

for i in range(1):
    for j in range(3):
        print(i, j)

# 16. ¿Qué mostrará la consola después de ejecutarse el siguiente fragmento de código?

# R: 0 al 14

for i in range(15):
    print (i)

# 17. ¿Qué mostrará la consola después de ejecutarse el siguiente fragmento de código?

# R: 7, 9, 11, 13

i = range(7,15,2)

for j in i:
    print(j)

# 18. ¿Qué mostrará la consola después de ejecutarse el siguiente fragmento de código?

# R: Examen

x = 25

if x <= 25:
    if x != 0:
        if x > 15 and x < 30:
            if 0 <= x < 50:
                print("Examen")
else:
    print("Programacion")

# 19. ¿Qué mostrará la consola después de ejecutarse el siguiente fragmento de código?

# R: sistemas, bases, fol

a = ["sistemas", "bases", "fol"]

for i in a:
    if "sistemas" in a:
        print(i)

# 20. ¿Qué mostrará exactamente la consola después de ejecutarse el siguiente fragmento de código?

# R: 2, 3, 4 X --> último índice no se incluye

li = [1,2,3,4]
print(li[1:3])

# 21. ¿Qué mostrará exactamente la consola después de ejecutarse el siguiente fragmento de código?

# R: [1, 2, 5, 4]

li = [1,2,3,4]
li[2] = 5
print(li)

# 22. ¿Qué mostrará exactamente la consola después de ejecutarse el siguiente fragmento de código?

# R: 4

li = [0,1,2,3]
a = len(li)
print(a)

# 23. ¿Qué mostrará exactamente la consola después de ejecutarse el siguiente
# fragmento de código?

# R: 1, 2

d = {1: "A", 2: "B"}

for k in d.keys():
    print(k)

# 24. ¿Qué mostrará exactamente la consola después de ejecutarse el siguiente fragmento de código?

# R: 8

li = [[1,2,3], [4,5,6], [7,8,9], ['#',0,'@']]
print(li[2][1])

# 25. ¿Qué mostrará la consola después de ejecutarse el siguiente fragmento de código?

# R: 10


def f(a, b=5):

    return a * b

print(f(2))

# 26. ¿Qué mostrará exactamente la consola después de ejecutarse el siguiente fragmento de código?

# R: 1, 2, 3 X --> 6 // Hace cada iteración del for y luego, una vez acaba la función, es cuando devuelve s

a = [1,2,3]

def f(a):

    s = 0

    for i in a:
        s += i

    return s


print(f(a))

# 27. ¿Qué mostrará exactamente la consola después de ejecutarse el siguiente
# fragmento de código?

# R: no lo hemos dado --> 6

a = 5


def f():

    global a    # global lo que hace es coger
    a = a + 1

f()

print(a)

# 28. ¿Qué mostrará exactamente la consola después de ejecutarse el siguiente fragmento de código?

# R: 2


def fx(num, f):

    return f(num)


def d(num):

    return num * 2


print(fx(1, d))

# 29. ¿Qué mostrará exactamente la consola después de ejecutarse el siguiente fragmento de código?


# R: nada (daría 9; no lo hemos dado)

f = lambda x1, y1, z1: x1 + y1 + z1

f(2, 3, 4)

# 30. ¿Qué mostrará exactamente la consola después de ejecutarse el siguiente fragmento de código?

# R: nada (daría 80)

f = lambda num: num * 4

f(20)


# 31. Escribir un programa que dado un diccionario vacío lo vaya llenado con
# información sobre una persona. Esta información debe ser: nombre, edad, sexo,
# teléfono y correo electrónico y debe ser introducida por el usuario. Cada vez
# que se añada un nuevo dato debe imprimirse el contenido del diccionario.

d = {}

loop = False

while not loop:

    nombre = str(input('Nombre: '))
    edad = int(input('Edad: '))
    sexo = str(input('Sexo (masculino o femenino): ')).lower()
    telefono = int(input('Teléfono: '))
    correo = str(input('Correo: '))

    d[nombre] = [edad, sexo, telefono, correo]

    print(d)

    choice = str(input('¿Desea continuar introduciendo datos? Y/N ')).lower()

    if 'n' in choice:

        loop = True



# 32. Escribir una función que reciba una muestra de números en una lista y
# devuelva otra lista con sus cuadrados.

nums = [1, 2, 3, 4, 5]


def cuadrados(lista):

    nums_2 = []
    index = int(len(lista))

    for items in range(1, index + 1):

        items = items ** 2
        nums_2.append(items)

    return nums_2


print(cuadrados(nums))



# 33. Escribir una función que calcule el área de un círculo y otra que calcule el
# volumen de un cilindro usando la primera función.


def area_circulo(r):

    from math import pi

    area_c = (r**2) * pi

    return area_c

def v_cilindo(first, altura):

    V_cilindro = first * altura

    return V_cilindro

radio = int(input('Radio del círculo: '))
h = int(input('Altura del cilindro: '))

data = round(v_cilindo(area_circulo(radio), h), 1)

print('El volumen del cilindro con radio ', radio, 'y altura ', h,  'es' + ' ' + str(data))

'''

# 34. Escribe un programa de conversión horas, minutos y segundos. El programa debe
# tener un menú donde el usuario pueda elegir la opción de conversión: es decir,
# convertir a segundos, convertir a horas,minutos y segundos o salir del
# programa.

def menu():

    print('-------------------------------\n'
          '¡Bienvenido a la Convertidora 4000!\n\n'
          '¿Qué desea hacer?\n'
          '1) Convertir a segundos\n'
          '2) Convertir a horas, minutos y segundos\n'
          '3) ¡Sácama de aquí!\n'
          '-------------------------------\n')

    loop = False

    while not loop:

        try:
            choice = int(input('Eliga la opción: '))

        except ValueError:
            print('¡Mal input! Ha de ser un número entre 1 - 3')

        else:
            loop = True

    if choice == 1:
        convertir_a_segundo()

    if choice == 2:
        convertir_a_horas_minutos_segundos()

    if choice == 3:
        print('¡Adios!')



def convertir_a_segundo():

    horas = int(input('Horas: '))
    minutos = int(input('Minutos: '))
    segundos = int(input('Segundos: '))

    horas_s = horas * 3600
    minutos_s = minutos * 60
    segundos_s = segundos

    total = horas_s + minutos_s + segundos_s

    print('Son un total de ', total, 'segundos')

    menu()


def convertir_a_horas_minutos_segundos():

    segundos = int(input('Segundos: '))

    if segundos > 3600:
        horas = segundos // 3600
        minutos = (segundos - (horas * 3600)) // 60
        segundos_s = segundos % 60

        print('Horas:', horas, '\n'
              'Minutos:', minutos, '\n'
              'Segundos:', segundos_s, '\n'
              )

    else:
        minutos = segundos // 60
        segundos_s = segundos % 60

        print('Minutos: ', minutos, 'Segundos: ', segundos_s, '\n')

    menu()

menu()


# ALT + SHIFT + flechas: mueves líneas enteras. En VS Code duplicas la línea. Para mover líneas basta ALT + flechas
# ALT + click en líneas: escribir en varias a la vez

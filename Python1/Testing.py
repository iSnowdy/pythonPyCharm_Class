#Actividad 1 - Buscar la versión de Python usada

import sys
print(sys.version)

#Actividad 2 - Usar print para imprimir un texto de una determinada forma.

Little_Star = ('Twinkle, twinkle, little star, '
               '\n\tHow I wonder what you are! '
               '\n\t\tUp above the world so high, '
               '\n\t\tLike a diamond in the sky. '
               '\nTwinkle, twinkle, little star, '
               '\n\tHow I wonder what you are')

print(Little_Star)

#Actividad 3 - Pedir nombre y luego imprimirlo por pantalla.

input('Inserte su nombre: ')
nombre = 'Andy'
print('Hola', nombre, 'bienvenido a Python')

#Actividad 4 - Pedir la edad y asignarle una variable.

input(int('Inserte su edad: '))
n = 24
print('La edad del sujeto es: ',n)


número = int(input('Introduzca un número entre 0 y 10: '))

while 0<=número<=10:
    print(número)
    número = número + 1
    if número >= 10:
        print('Se ha llegado a 10')
        break
else:
    número = int(input('Por favor introduzca un número entre 0 y 10: '))
    if número < 0 or número > 10:
        while 0 > número or número > 10:
            número = int(input('Su número', número ,'es incorrecto. Por favor introduzca un valor entre 0 y 10'))
    else:
        while 0 <= número <= 10:
            print(número)
            número = número + 1
            if número >= 10:
                print('Se ha llegado a 10')
                break


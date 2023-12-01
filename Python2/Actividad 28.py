# Actividad 28 - Escribe un programa para adivinar un número. El ordenador guarda en la memoria un número y el
# usuario ha de adivinarlo. El programa comienza por preguntarle al usuario el rango de los números.
# Luego, el usuario irá probando números y el programa le irá diciendo qué tan cerca está.

import random

mínimo = 0
máximo = 0
número_aleatorio = 0
count = 0

mínimo = int(input('Establezca un rango mínimo: '))
máximo = int(input('Establezca un rango máximo: '))

while máximo <= mínimo:
    máximo = int(input(f'Inténtelo otra vez. El máximo ha de ser mayor que {mínimo}:' ))

número_aleatorio = random.randrange(mínimo, máximo)
print(número_aleatorio)

print('Adivina un número aleatorio entre', mínimo, 'y', máximo)
número = int(input('Escribe tu primer número: '))

while número > número_aleatorio or número < número_aleatorio:
    if número > número_aleatorio:
        número = int(input('¡Muy grande! Inténtalo de nuevo: '))
        count = count + 1

    else:
        número = int(input('Muy pequeño! Inténtalo de nuevo: '))
        count = count + 1

else:
    print('¡Felicidades! Lo has adivinado. Efectivamente, el número aleatorio es', número_aleatorio)

print('Te ha costado', count, 'intentos')


# Actividad 12 - Pedir un número y que nos diga si es mayor o menor que 10.

número = 0

número = float(input('Inserte un número: '))

if número >= 10:
    print('Su número ' + str(número),', es mayor o igual que 10')

else:
    print('Su número ' + str(número),', es menor que 10')

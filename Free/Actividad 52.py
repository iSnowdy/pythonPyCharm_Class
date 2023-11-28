# Actividad 52 - Crear un programa que compruebe si dos palabras riman. Se considera que dos palabras riman
# cuando sus tres últimas letras son iguales.

x = 'string'
y = 'string'

print('Le diremos si las dos palabras que escriba a continuación riman o no. Para este ejemplo se considera que dos'
      'palabras riman cuando sus últimas tres letras son iguales')

x = str(input('Escriba una primera palabra: '))
y = str(input('Escriba una segunda palabra: '))

if x[-3:] == y[-3:]:
    print('¡Sus palabras riman!')
else:
    print('No riman según nuestras condiciones')


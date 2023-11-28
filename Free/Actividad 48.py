# Actividad 48 - Haz un programa que calcule el desglose de billetes y monedas de una cantidad exacta de
# euros. Hay billetes de 500, 200, 100, 50, 20, 10 y 5 € y monedas de 2 y 1 €.


# 1 km = 100000 cm
# 1 m = 100 cm

cantidad = 0

cantidad = int(input('¿Qué cantidad desea desglosar? '))

'''
billetes = [500, 200, 100, 50, 20, 10, 5, 2, 1]
print(billetes)
print(type(billetes))
'''

if cantidad == 2:
    print('2 monedas de 1 euro')

elif cantidad >= 2:
    billetes_500 = cantidad // 500
    if billetes_500 >= 1:
        cantidad = cantidad - billetes_500 * 500
        print(billetes_500, 'billetes de 500 euros.')
    billetes_200 = cantidad // 200
    if billetes_200 >= 1:
        cantidad = cantidad - billetes_200 * 200
        print(billetes_200, 'billetes de 200 euros.')
    billetes_100 = cantidad // 100
    if billetes_100 >= 1:
        cantidad = cantidad - billetes_100 * 100
        print(billetes_100, 'billetes de 100 euros.')
    billetes_50 = cantidad // 50
    if billetes_50 >= 1:
        cantidad = cantidad - billetes_50 * 50
        print(billetes_50, 'billetes de 50 euros.')
    billetes_20 = cantidad // 20
    if billetes_20 >= 1:
        cantidad = cantidad - billetes_20 * 20
        print(billetes_20, 'billetes de 20 euros.')
    billetes_10 = cantidad // 10
    if billetes_10 >= 1:
        cantidad = cantidad - billetes_10 * 10
        print(billetes_10, 'billetes de 10 euros.')
    billetes_5 = cantidad // 5
    if billetes_5 >= 1:
        cantidad = cantidad - billetes_5 * 5
        print(billetes_5, 'billetes de 5 euros.')
    monedas_2 = cantidad // 2
    if monedas_2 >= 1:
        cantidad = cantidad - monedas_2 * 2
        print(monedas_2, 'monedas de 2 euros.')
    monedas_1 = cantidad // 1
    if monedas_1 >= 1:
        cantidad = cantidad - monedas_1 * 1
        print(monedas_1, 'billetes de 1 euro.')
else:
    int(input('No es posible dar cambio de menos de 1 euro'))

''' print('B500', billetes_500, 'B200', billetes_200, 'B100', billetes_100, 'B50', billetes_50, 'B20', billetes_20
      , 'B10', billetes_10, 'B5', billetes_5, 'M2', monedas_2, 'M1', monedas_1) '''


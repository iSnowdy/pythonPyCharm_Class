# Actividad 22 - Escriba un programa que pida al usuario una distancia en centímetros y que luego,
# esta distancia, se imprima en unidades de: km, m y cm. Sólo escriba las unidades necesarias.

# 1 km = 100000 cm
# 1 m = 100 cm

número_cm = 0
número_km = 0
número_m = 0
número_cm2 = 0

número_cm = float(input('Escriba un número en centímetros: '))

if número_cm > 100000:
    número_km = número_cm // 100000
    número_m = número_cm % 100000
    número_cm2 = número_cm % 100
    print(número_km, 'km', número_m, 'm', número_cm2, 'cm')

else:
    número_m = número_cm // 100
    número_cm2 = número_cm % 100
    print(número_m, 'm', número_cm2, 'cm')


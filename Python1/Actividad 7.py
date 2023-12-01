# Actividad 7 - Calcular el promedio de 4 notas insertadas por el usuario y mostrar cada variable.

a = 0
b = 0
c = 0
d = 0
mean = 0

a = float(input('Inserte su primera nota: '))
b = float(input('Inserte su segunda nota: '))
c = float(input('Inserte su tercera nota: '))
d = float(input('Inserte su cuarta nota: '))

mean = (a+b+c+d)/4

print('Primera nota', a, '\nSegunda nota', b,'\nTercera nota', c,'\nCuarta nota', d,
      '\nFinalmente, la media de sus notas es', mean)

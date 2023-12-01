# Actividad 57 M3 - Hacer una tabla de multiplicar en forma de matriz.


for i in range(1, 11):
	for j in range(1,11):
		print('{:4}'.format(i*j), end=' ')
	print()

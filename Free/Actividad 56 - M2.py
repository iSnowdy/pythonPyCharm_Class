# Actividad 56 M2 - Escribe un programa que haga la matriz como se demuestra (NxN con N = 6):

for i in range(6):
    print()
    print(i, end=' ')
    for j in range(5):
        if i == 0:
            print(f'{j + 1}', end=' ')
        if i > 0:
            print(f'{j * 0}', end=' ')

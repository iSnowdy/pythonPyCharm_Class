m = int(input())
n = int(input())
p = 0
while m > 0:
    m = m - 1
    p = p + n
print ('El producto de m y n es', p)



for i in range(4, 11, 1):
    print(i)

sueldo = int(input('Ingrese su sueldo: '))
if sueldo < 1000:
    tasa = 0.00
elif 1000<= sueldo < 2000:
    tasa = 0.05
elif 2000 <= sueldo < 4000:
    tasa = 0.10
else:
    tasa = 0.12
print ('Usted debe pagar', tasa * sueldo, 'de impuesto')

i = 1
while i <= 9:
    print(i)
    i = i + 2

es_primo = True
for d in range(2, n):
    if n % d == 0:
        es_primo = False
        break


lista = []
mínimo = float(0)
máximo = float(0)
número = float(0)

mínimo = float(input('Escriba un número. Este será el mínimo: '))
máximo = float(input('Escriba un número. Este será el máximo, y por tanto, ha de ser mayor que el anterior: '))

if mínimo > máximo:
    máximo = float(input('Ha de ser mayor. Inténtelo de nuevo:'))

print('A continuación comenzaremos a introducir números comprendidos entre', mínimo, 'y', máximo)

número = float(input(f'Escriba el primer número comprendido entre, {mínimo} y {máximo}. \nDe lo contrario, '
                     f'se interrumpirá la lista: '))

if mínimo < número > máximo:
    while mínimo < número > máximo:
        número = float(input(f'Escriba un número comprendido entre, {mínimo} y {máximo}. \nDe lo contrario, '
                     f'se interrumpirá la lista: '))
    if mínimo < número > máximo:
        lista.append(número)

else:
    lista.append(mínimo)
    lista.append(máximo)

print(lista)


-----


lista = []
mínimo = float(0)
máximo = float(0)
número = float(0)

mínimo = float(input('Escriba un número. Este será el mínimo: '))
máximo = float(input('Escriba un número. Este será el máximo, y por tanto, ha de ser mayor que el anterior: '))

while mínimo > máximo: # Obligamos a que el máximo sea mayor que el mínimo.
    máximo = float(input('Ha de ser mayor. Inténtelo de nuevo:'))

número = float(input(f'Escriba el primer número comprendido entre, {mínimo} y {máximo}. \nDe lo contrario, '
                     f'se interrumpirá la lista: '))

if máximo > mínimo:

    lista.append(número)
    while mínimo < número < máximo:

        número = float(input(f'Escriba un número comprendido entre, {mínimo} y {máximo}. \nDe lo contrario, '
                             f'se interrumpirá la lista: '))
        if mínimo < número < máximo:
            lista.append(número)
        else:
            break

print('La lista ha terminado. Su lista es:', lista)
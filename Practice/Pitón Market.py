'''

El supermercado Pit ´on Market ha lanzado una promoci ´on para todos sus clientes
que posean la tarjeta Raw Input. La promoci ´on consiste en aplicar un descuento por cada n
productos que pasan por caja.

El primer descuento es de 20 %, y se aplica sobre los
primeros n productos ingresados. Luego, cada des-
cuento es la mitad del anterior, y es aplicado sobre los
siguientes n productos.

Por ejemplo, si n = 3 y la compra es de 11 productos,
entonces los tres primeros tienen 20 % de descuento,
los tres siguientes 10 %, los tres siguientes 5 %, y los
dos ´ultimos no tienen descuento.

Escriba un programa que pida al usuario ingresar n y
la cantidad de productos, y luego los precios de cada
producto. Al final, el programa debe entregar el precio
total, el descuento total y el precio final despu´es de
aplicar el descuento.

Si al aplicar el descuento el precio queda con deci-
males, redondee el valor hacia abajo.

'''


n = int(input('Ingrese n: '))
cantidad_p = int(input('Ingrese la cantidad de productos a descontar: '))
precio_L = []
precio_D = 0


for i in range(cantidad_p):

    precio = int(input(f'Precio del producto {i+1}: '))
    precio_L = precio_L + [precio]

indice = 0
contador = 0
contador_n = 0

while contador_n < 8:

    while contador < n:

        precio_D = precio_D + (precio_L[indice] * 0.2)
        indice += 1
        contador += 1

    contador_n += n
    contador = 0
    indice = n

    while contador < n:

        precio_D = precio_D + (precio_L[indice] * 0.1)
        indice += 1
        contador += 1

    contador_n += n
    contador = 0
    indice = n

    while contador < n:

        precio_D = precio_D + (precio_L[indice] * 0.05)
        indice += 1
        contador += 1








print('Total: ', sum(precio_L))
print('Descontado: ', precio_D)
print('A pagar: ', sum(precio_L) - precio_D)

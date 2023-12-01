# Actividad 14 - Crear un bucle que muestre en pantalla los números del 0 al 10.

número = float(input('Introduzca un número entre 0 y 10: '))

número = int(número)  # Convierte el número del usuario en entero.

while 0 <= número <= 10:
    print(número)
    número = número + 1

    if número == 10:
        print(número)
        print('Se ha llegado a 10')
        break

else:
    while 0 > número or número > 10:
        número = int(input('Su número no es válido. Por favor introduzca un valor entre 0 y 10: '))

    else:
        while 0 <= número <= 10:
            print(número)
            número = número + 1

            if número == 10:
                print(número)
                print('Se ha llegado a 10')
                break

# Pedimos un número entre 0 y 10. Pero si el usuario da cualquier otro número que no esté entre esos valores,
# se le inducirá a un bucle hasta que lo haga.

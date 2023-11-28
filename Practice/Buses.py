'''

La empresa de buses rawbus requiere implementar un sistema de asignaci ´on de asientos
para cada uno de los buses.

Para ello se debe implementar en base a los siguientes requerimientos. La disponibilidad de
asientos se encuentra en una cadena de caracteres que contiene las letras a (pasajero adulto), e
(pasajero estudiante) y v (vac´ıo). El ´ındice de esa cadena de caracteres representa el asiento. Por
ejemplo la cadena de caracteres vaaaev indica que el asiento 1 y 6 est ´an vac´ıos, hay 3 pasajeros
adultos en los asientos 2, 3 y 4, y un estudiante en el asiento 5.

Escriba un programa que permita al usuario ingresar la cadena de caracteres con los asientos
utilizados y no utilizados. Luego permita ingresar el tipo de pasajero (estudiante o adulto) y
finalmente el n ´umero del asiento que el pasajero desea utilizar. Si el asiento se encuentra ocupado,
se deber´a volver a ingresar otro n ´umero de asiento.

El programa dejar ´a de solicitar informaci ´on s ´olo cuando se ingrese el valor 0 (cero), o bien, cuando
ya no queden m ´as asientos disponibles (vacios). Una vez terminado el programa debe mostrar la
cantidad total de pasajes comprados por adultos y estudiantes, y el total de dinero recaudado por
las ventas, considerando que las tarifas son: $2200 para estudiantes y $4000 para adulto.

Nota: Asuma que el usuario ingresa datos v´alidos.

'''

asientos = str(input('Asientos: ')) # Pedimos string inicial de asientos

if 'v' in asientos:

    pasajero = str(input('Pasajero (adulto / estudiante): ')) # Preguntamos qué tipo de pasajero es

    posicion = '' # Iniciamos la variable de posicion

    while 'v' in asientos and posicion != 0:
        # Siempre que haya asientos vacíos (v) y la posición no sea 0, se iniciará el bucle

        posicion = int(input('¿En qué posición desea sentarse? '))

        if asientos[posicion - 1] == 'v': # Los índices en Python siempre van 1 por delante

            if pasajero == 'adulto':

                if posicion == 1:

                    asientos = 'a' + asientos[1:]
                    print('Asiento asignado')
                    # Reemplazamos vacío por asiento ocupado por adulto. Pero sólo funciona para la 1 posición

                else:

                    asientos = asientos[:posicion - 1] + 'a' + asientos[posicion:]
                    print('Asiento asignado')
                    # Si el asiento no está en la 1 posición, leemos los asientos antes de encontrar la posición
                    # correcta, al encontrar nuestra posición la reescribimos y el resto se vuelve a añadir como antes

            elif pasajero == 'estudiante':

                if posicion == 1:

                    asientos = 'e' + asientos[1:]
                    print('Asiento asignado')
                    # Reemplazamos vacío por asiento ocupado por un estudainte

                else:

                    asientos = asientos[:posicion - 1] + 'e' + asientos[posicion:]
                    print('Asiento asignado')

        else:

            print('Ocupado')

if 'v' not in asientos:

    print('Lo sentimos, el bus está lleno')


num_adultos = asientos.count('a')
num_estudiantes = asientos.count('e')
recaudado = (num_adultos * 4000) + (num_estudiantes * 2200)

print('Adultos en el bus: ', num_adultos)
print('Estudiantes en el bus: ', num_estudiantes)
print('Dinero recaudado en total: ', recaudado)
print(type(asientos))
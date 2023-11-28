'''

La Universidad Tropical Filomena Santa Marta ha instaurado un nuevo reglamento
de evaluaciones. Todas las asignaturas deben tener tres cert´amenes y un examen. Las notas
van entre 0 y 10, con un decimal.

Despu´es de los tres cert´amenes, los alumnos con promedio menor que 3 reprueban y los con
promedio mayor o igual que 7 aprueban. El resto va al examen, en el que deben sacarse por
lo menos un 5 para aprobar.

Adem´as, para reducir el trabajo de los profesores, se decidi ´o que los alumnos que se sacan
menos de un 2 en los dos primeros cert´amenes est´an autom´aticamente reprobados. A su
vez, los que obtienen m´as de un 9 en los dos primeros cert´amenes est´an autom´aticamente
aprobados. En ambos casos, no deben rendir el tercer certamen.

Escriba un programa que pregunte a un estudiante las notas de las evaluaciones que rindi ´o,
y le diga si est´a aprobado o reprobado.

'''

c1 = 0
c2 = 0
c3 = 0

c1 = float(input('Nota C1: '))
c2 = float(input('Nota C2: '))


if 2 <= (c1 + c2)/2 <= 9:

    c3 = float(input('Nota C3: '))

    if (c1 + c2 + c3) / 3 < 3:

        print('Usted ha suspendido')

    elif (c1 + c2 + c3) / 3 >= 7:

        print('Usted está aprobado')
        loop = True

    else:

        recu = float(input('Nota recuperación: '))

        if recu < 5:
            print('Está suspendido. Pero puede recuperar en la recuperación')
        else:

            print('Aprobado')

elif (c1 + c2)/2 < 2:

    print('Usted ha suspendido')


elif (c1 + c2)/2 >= 9:

    print('Usted está aprobado')


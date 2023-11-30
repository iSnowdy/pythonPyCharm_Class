def menu():

    print('-------------------------------\n'
          '¡Bienvenido a la Convertidora 4000!\n\n'
          '¿Qué desea hacer?\n'
          '1) Convertir a segundos\n'
          '2) Convertir a horas, minutos y segundos\n'
          '3) ¡Sácama de aquí!\n'
          '-------------------------------\n')

    try:
        choice = int(input('Eliga la opción: '))

    except ValueError:
        print('¡Mal input! Ha de ser un número entre 1 -3')

    if choice == 1:
        convertir_a_segundo()

    if choice == 2:
        convertir_a_horas_minutos_segundos()

    if choice == 3:
        print('¡Adios!')



def convertir_a_segundo():

    horas = int(input('Horas: '))
    minutos = int(input('Minutos: '))
    segundos = int(input('Segundos: '))

    horas_s = horas * 3600
    minutos_s = minutos * 60
    segundos_s = segundos

    total = horas_s + minutos_s + segundos_s

    print('Son un total de ', total, 'segundos')

    menu()





def convertir_a_horas_minutos_segundos():

    segundos = int(input('Segundos: '))

    if segundos > 3600:
        horas = segundos // 3600
        minutos = (segundos - (horas * 3600)) // 60
        segundos_s = segundos & 60

        print('Horas:', horas, '\n'
              'Minutos:', minutos, '\n'
              'Segundos:', segundos_s, '\n'
              )

    else:
        minutos = segundos // 60
        segundos_s = segundos & 60

        print('Minutos: ', minutos, 'Segundos: ', segundos_s, '\n')

    menu()


menu()
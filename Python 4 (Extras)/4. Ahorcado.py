nombre = ''
min = 999
max = 0
l_puntuacion = []
l_puntuacion_f = []
puntuacion_f = 0
puntuacion_final = 0


while 'FIN' not in nombre:

    nombre = str(input('Nombre: '))
    grado_dificultad = float(input('Grado de dificultad: '))

    for i in range(1, 8):

        puntuacion = float(input(f'Juez {i}: '))

        l_puntuacion = l_puntuacion + [puntuacion]

        if max < puntuacion:
            max = puntuacion
        if min > puntuacion:
            min = puntuacion

    puntuacion_f = (((sum(l_puntuacion) - min - max) * 0.6) * grado_dificultad)

    l_puntuacion_f = l_puntuacion_f + [puntuacion_f]

    if puntuacion_f > puntuacion_final:

        nombre_ganador = nombre
        puntuacion_final = puntuacion_f

    finalizar = str(input('Desea finalizar? Y/N '))

    if 'Y' in finalizar:

        print('Y el ganador es...', nombre_ganador, 'con una puntuación final de', round(puntuacion_final, 1))
        nombre = 'FIN'


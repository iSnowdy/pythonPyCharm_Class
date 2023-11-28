'''

En las competencias de clavados, como las que usted probablemente vio en los recientes
Juegos Ol´ımpicos, cada salto es evaluado por un panel de siete jueces.

Cada juez entrega una puntuaci ´on en una escala de 1 a 10, con incrementos de 1⁄2. La puntuaci ´on
m ´as alta y la m ´as baja son eliminadas. La suma de los cinco puntajes restantes es multiplicada
por 3⁄5, y el resultado es multiplicado por el grado de dificultad del salto. El valor obtenido es el
puntaje total del salto.

El ganador de la competencia es el clavadista que obtiene el puntaje total m´as alto.


a) Escriba un programa que pida al usuario ingresar el nombre de un clavadista, el grado de
dificultad de su salto y los puntajes entregados por los jueces. Como salida, el programa debe
imprimir el puntaje total obtenido.

b) Escriba un programa que pregunte los datos de los saltos de varios clavadistas, y al final imprima
el nombre del ganador. El programa debe terminar cuando el nombre ingresado sea FIN

'''


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


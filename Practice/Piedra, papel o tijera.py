import random


jugador_eleccion = (str(input('¿Piedra, papel o tijera?')))
elecciones = ['piedra', 'papel', 'tijera']

loop = False
ganar = 0
perder = 0
empate = 0

while not loop:


    pc_eleccion = random.choice(elecciones)

    if ((jugador_eleccion == 'piedra' and pc_eleccion == 'tijera') or (jugador_eleccion == 'papel' and pc_eleccion == 'piedra') or
            (jugador_eleccion == 'tijera' and pc_eleccion == 'papel')):

        print('La maquina eligió...', pc_eleccion)
        print('Ganaste!')
        ganar += 1

    elif jugador_eleccion == pc_eleccion:

        print('La maquina eligió...', pc_eleccion)
        print('Empate')
        empate += 1

    else:

        print('La maquina eligió...', pc_eleccion)
        print('Perdiste!')
        perder += 1

    choice = str(input('¿Desea continuar jugando? Y/N '))

    if 'N' in choice:

        print('El score es de...', ganar, 'victorias', perder, 'derrotas y ', empate, 'empates')
        loop = True

    else:

        jugador_eleccion = (str(input('¿Piedra, papel o tijera?')))






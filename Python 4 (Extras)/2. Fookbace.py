# La red social almacena los datos de los usuarios en un diccionario. Las llaves son un código numérico que identifica
# a cada usuario. Los valores son una tupla compuesta por: nombre, ciudad y fecha de nacimiento. La fecha de nacimiento
# es a su vez una tupla compuesta por (año, mes, dia).


# 1. Escribir la función misma_ciudad(u1, u2) que indique si el usuario con el código u1 y el usuario con el código
# u2 viven en la misma ciudad.

# 2. Escribir la función diferencia_edad(u1, u2) que retorne la diferencia de edad entre el usuario 1 y 2. Sólo
# tendremos en cuenta el año para calcular la diferencia.

# 3. Para guardar la información de qué usuarios son amigos entre sí, la red social utiliza el conjunto amistades.
# Este conjunto contiene las tuplas de ambos usuarios; sus códigos. El código del usuario 2 (b) ha de ser mayor que el
# del usuario 1 (a). De forma que b > a.

# 3.1. Escribir la función obtener_amigos(u) que retorne el conjunto de amigos del usuario u.
# 3.2. Escribir la función recomendar_amigos(u) que retorne el conjunto de códigos de los usuarios que cumplan
# todas las condiciones siguientes: (1) son amigos de un amigo de u; (2) no son amigos de u; (3) viven en la misma
# ciudad que u; (4) y tienen menos de diez años de diferencia con u.

usuarios = {

522514: ('Jean Dupont', 'Marseille', (1989, 11, 21)),
587125: ('Perico Los Palotes', 'Valparaiso', (1990, 4, 12)),
189471: ('Jan Kowalski', 'Krakow', (1994, 4, 22)),
914210: ('Antonio Nobel', 'Valparaiso', (1983, 7, 1)),
546216: ('Jose Pipo', 'Cuenca', (1995, 4, 2)),
457958: ('Miguel Kimi', 'Madrid', (1999, 23, 4)),
321564: ('Jean Clear', 'Barcelona', (1986, 21, 5)),
985125: ('Maria Martinez', 'Girona', (1976, 12, 8)),
745954: ('Antonia Lorena', 'Palma', (1980, 15, 10)),
159753: ('Cristian Jimenez', 'Huelva', (1981, 5, 12)),
198471: ('Alonso Ferrindo', 'Palma', (1995, 7, 21)),
289142: ('Jaime Lozano', 'Manacor', (1960, 2, 26)),
138555: ('Mariano Gomez', 'Benidor', (1975, 9, 20)),
429900: ('Luis Barco', 'Palma', (1989, 11, 14)),
349123: ('Cabrito Loquito', 'Palma', (1985, 5, 11)),
781118:  ('Pepito Loco', 'Palma', (1981, 2, 12)),

}


amistades = {

    (198471, 289142), (138555, 429900), (138555, 781118), (159753, 745954), (457958, 985125),
    (546216, 321564), (138555, 159753), (138555, 349123), (522514, 159753), (985125, 914210),

}


# 1.


def misma_ciudad (u1, u2):

    # De los usuarios en el código x, tendremos una tupla. Esta tupla tiene índice 0-3. Nos interesa el 1; la ciudad
    if usuarios[u1][1] == usuarios[u2][1]:
        return True
    else:
        return False

# 2.


def diferencia_edad (u1, u2):

    age_diff = usuarios[u1][2][0] - usuarios[u2][2][0]

    return(abs(age_diff)) # Nos devolverá siempre un número positivo


print('Tenemos una diferencia de', diferencia_edad(429900, 349123), 'años')
print('Tenemos una diferencia de', diferencia_edad(429900, 781118), 'años')

# 3.

def obtener_amigos (u):

    friends = set()

    for personas in amistades:
        u1, u2 = personas # Definimos los 2 números en el set amistades
        if u == u1:
            friends.add(u2) # De forma que si u es la persona 1 del set, nos añada la 2. No queremos repetir u
        elif u == u2:
            friends.add(u1)

    return friends


print('Mis amigos son', obtener_amigos(429900))


def recomendar_amigos (u):

    recommendation = set()

    friends_of_friend = False
    not_friends = False
    same_city = False
    ten_y_diff = False

    validate = False

    for amigos in obtener_amigos(u): # Buscamos los amigos de u
        for amigo_de_amigos in obtener_amigos(amigos): # Buscamos los amigos del amigo de u
            friends_of_friend = True
            if amigo_de_amigos != u: # Excluímos a u; para no recomendarnos a nosotros mismos
                if (amigo_de_amigos not in obtener_amigos(u) and misma_ciudad(amigo_de_amigos, u)
                        and diferencia_edad(amigo_de_amigos, u) < 10):
                # Aplicamos las condiciones requeridas: que no sean amigos de u / que estén en la misma ciudad / edad
                    not_friends = True
                    same_city = True
                    ten_y_diff = True
                    recommendation.add(amigo_de_amigos)


    print('Acuérdate de los return!!!!!!!! Faltaban y por eso no cumplía todas las condiciones')

    print('Validando...', friends_of_friend, not_friends, same_city, ten_y_diff)

    if friends_of_friend == True and not_friends == True and same_city == True and ten_y_diff == True:
        validate = True
        return recommendation
    else:
        validate = False
        return print('No cumple todas las condiciones')

print('Te recomiendo a estas personas como amigos: ', recomendar_amigos(429900))
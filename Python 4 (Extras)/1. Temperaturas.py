# Temperaturas ---


# Temperaturas máxima y mínimas de ciudades guardadas en un diccionario.
# Las llaves son las ciudades. Valores son las tuplas valores (mínima, máxima).
# Los nombres de las ciudades en las que hubo más de 25ºC deben de aparecer en mayúsculas.
# El nombre del archivo debe contener la fecha.
# No es necesario ordenar los datos.


# Escriba la función crear_reportes(fecha, temperaturas). Los parámetros son la fecha(una tupla compuesta de
# (año, mes, día)) y el diccionario de temperaturas. Y que genere el archivo txt.
# La función como tal no retorna nada.

temp = {
    'Vina del Mar': (9, 26),
    'Valparaiso': (10, 24),
    'Quilpue': (7, 30),
    'Olmue': (5, 29),
    'Limache': (9, 23),
    'Villa Alemana': (9, 22),
}


def crear_reporte(fecha, temperaturas):
    ano, mes, dia = fecha
    # Definimos fecha con las variables año, mes y día en ese orden
    fichero = open("reporte-" + str(ano) + "-" + str(mes) + "-" + str(dia) + ".txt", "w")
    # Nombramos el fichero.txt que crearemos de la forma señalizada. Hacemos casting de ellos porque son int

    for ciudades, tupla in temperaturas.items(): # Recorremos el diccionario entero (items)
        minima, maxima = tupla # Definimos que tupla esté divida en minima y maxima en ese orden
        if maxima > 25:
            new = ciudades.upper() + ': maximas ' + str(maxima) + ', minimas ' + str(minima) + "\n"
        else:
            new = ciudades + ': maximas ' + str(maxima) + ', minimas ' + str(minima) + "\n"

        # Creamos un nuevo string (new) en el que se vayan añadiendo los valores que queremos escribir en el .txt

        fichero.write(new)

    fichero.close()
    # Lo cerramos. Muy importante


crear_reporte((2011, 5, 14), temp)

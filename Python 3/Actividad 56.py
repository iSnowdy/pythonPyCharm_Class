# Actividad 56 - Crear un módulo que solicite al usuario un nombre de usuario y contraseña y los valide
# utilizando los módulos anteriores.

print('Comenzaremos con el nombre de usuario')

nombre_alf = str(input('Introduzca un nombre de usuario de entre 6 y 12 caracteres y que contenga caracteres sólo'
                   'alfanuméricos: '))

def nombre_usuario(nombre):
    for caracteres in nombre:
        if len(nombre) < 6:
            nombre = str(input('El nombre de usuario debe contener al menos 6 caracteres. Inténtelo de nuevo: '))
        elif len(nombre) > 12:
            nombre = str(input('El nombre de usuario no puede contener más de 12 caracteres. Inténtelo de nuevo: '))
        elif nombre.isalnum() is False:
            nombre = str(input('El nombre de usuario puede contener solo letras y números. Inténtelo de nuevo: '))
    return(nombre)

verificar_usuario = nombre_usuario(nombre_alf)

print(verificar_usuario)

print('Maravilloso. Su nombre de usuario es lo suficientemente seguro como para proseguir')

print('Ahora la contraseña')

contras = str(input('Introduzca una nueva contraseña. Debe contener al menos 8 caracteres con una combinación de '
                   'minúsculas, mayúsculas, números y al menos 1 caracter no alfanumérico: '))

def contraseña(contra):

    validar = False  # Comenzamos con el supuesto de que la contraseña es inválida.
    mayusculas = False  # Igual que antes. Para que cambie a True, deberá de tener minusc, mayusc y numeros.
    minusculas = False
    numeros = False
    alfan = contra.isalnum()  # Si es alfanumérico, devolverá True. Queremos que devuelva False.

    correcto = True  # Verificador de las condiciones

    for caracteres in contra:  # Comprobamos letra por letra si es minusc, mayusc y numérico. Cuando al menos una lo sea,
        # nos devolverá True como validación de que ese requisito se cumple.

        if caracteres.islower() == True:
            minusculas = True

        if caracteres.isupper() == True:
            mayusculas = True

        if caracteres.isnumeric() == True:
            numeros = True

    if len(contra) > 8:
        validar = True

    if minusculas == True and mayusculas == True and numeros == True and alfan == False and validar == True:
        validar = True  # Se cumplen todos los requisitos.
    else:
        correcto = False  # No se cumplen. Cambiamos el verificador.

    if correcto == False:
        print('La contraseña elegida no es segura')
        return False

    elif correcto == True:
        return True


verificar_contraseña = contraseña(contras)

print(verificar_contraseña)

while verificar_contraseña == False:
    print('La contraseña no es segura. ¡Inténtelo de nuevo!')
    contras = str(input('Introduzca una nueva contraseña. Debe contener al menos 8 caracteres con una combinación de '
                       'minúsculas, mayúsculas, números y al menos 1 caracter no alfanumérico: '))
    verificar_contraseña = contraseña(contras)
else:
    print('Buen trabajo. Ya tiene su nombre de usuario y contraseña. Estos son:')
    print('Usuario: ', verificar_usuario, 'y contraseña: ',contras)

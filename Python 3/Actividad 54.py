# Crea un módulo para la validación de nombres de usuarios. Dicho módulo debe cumplir con los siguientes criterios:

# 1. El nombre de usuario de contener un mínimo de 6 caracteres y un máximo de 12.
# 2. El nombre de usuario debe ser alfanumérico.
# 3. Si el nombre de usuario tiene menos de 6 caracteres, retornar el mensaje: “El nombre de usuario debe contener
# al menos 6 caracteres”
# 4. Si el nombre de usuario tiene más de 12 caracteres, retornar el mensaje: “El nombre de usuario no puede contener
# más de 12 caracteres”
# 5. Si el nombre de usuario tiene caracteres no alfanuméricos, retornar el mensaje: “El nombre de usuario puede contener
# solo letras y números”
# 6. Si el nombre de usuario es válido, retornar True.

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
    return(True)

verificar = nombre_usuario(nombre_alf)

print(verificar)


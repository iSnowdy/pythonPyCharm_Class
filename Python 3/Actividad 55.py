# Actividad 55 - Crea un módulo para la validación de contraseñas. Dicho modulo debería cumplir con
# los siguientes criterios:
import string

# 1. La contraseña debe tener un mínimo de 8 caracteres.
# 2. Una contraseña debe contener: letras minúsculas, mayúsculas, números y al menos 1 caracter no alfanumérico.
# 3. La contraseña no puede contener espacios en blanco.
# 4. Si la contraseña es válida, retornar True.
# 5. Si la contraseña no es válida, retornar “La contraseña elegida no es segura”.

from random import sample

contra = str(input('Introduzca una nueva contraseña. Debe contener al menos 8 caracteres con una combinación de '
                   'minúsculas, mayúsculas, números y al menos 1 caracter no alfanumérico: '))

def contraseña(contra):

    validar = False # Comenzamos con el supuesto de que la contraseña es inválida.
    long = len(contra)
    mayusculas = False # Igual que antes. Para que cambie a True, deberá de tener minusc, mayusc y numeros.
    minusculas = False
    numeros = False
    alfan = contra.isalnum() # Si es alfanumérico, devolverá True. Queremos que devuelva False.

    correcto = True # Verificador de las condiciones

    for caracteres in contra: # Comprobamos letra por letra si es minusc, mayusc y numérico. Cuando al menos una lo sea,
        # nos devolverá True como validación de que ese requisito se cumple.

        if caracteres.islower() == True:
            minusculas = True

        if caracteres.isupper() == True:
            mayusculas = True

        if caracteres.isnumeric() == True:
            numeros = True

    if long > 8:
        validar = True

    if minusculas == True and mayusculas == True and numeros == True and alfan == False and validar == True:
        validar = True # Se cumplen todos los requisitos.
    else:
        correcto = False # No se cumplen. Cambiamos el verificador.

    if correcto == False:
        print('La contraseña elegida no es segura')

    elif correcto == True:
        return True


print(contraseña(contra))

# ¡CoNtraSeñA44!
# Actividad 53 - Generación de IBAN.

# 1. Crear un código previo de IBAN de formato: código país (ES) seguido de '00' y el C.C.C o código de cuenta
# del cliente.

# 2077 0024 00 3102575766

CCC = str(input('Introduzca el código de cuenta de cliente: '))

c_1 = 'ES' + str('00') + CCC

# 2. Trasladamos los cuatro primeros caracteres al final del str.

c_2 = c_1[4:] + c_1[0:4]

# 3. Convertimos el código de país, en este caso 'ES', en su equivalente numérico (14 y 28).

c_f = c_2.replace('E', str('14'))
c_F = c_f.replace('S', str('28'))

mod = c_F.replace(' ', '') # Descartamos los espacios para poder realizar operaciones matemáticas.

# 4. Aplicamos el modelo 97 – 10. Es decir, dado un número, se divide entre 97 y el resto lo restamos a 98.
# Luego si el resto es un número de un único dígito, se introduce un 0 a la izquierda. Sino se mantiene igual.
# Se trata de un algoritmo de verificación de IBAN.

resto = 98 - int(mod)%97

if 0 <= resto < 10:
    resto = str('0') + str(resto)

# Finalmente imprimimos el IBAN.

IBAN = 'IBAN' + ' ' + 'ES' + str(resto) + ' ' + CCC
print('Su IBAN o número bancario internacional es', IBAN)

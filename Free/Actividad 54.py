# Actividad 54 - Calcularemos el dígito de control de una cuenta corriente.

entidad = str(input('Introduzca el número de su entidad bancaria. Estos son los 4 primeros números que'
                    'aparecen tras el código IBAN de su cuenta bancaria: '))

while 3 >= len(entidad) or len(entidad) > 4:
    entidad = str(input('Ha introducido un número erróneo. Revise correctamente su número de entidad bancaria: '))

oficina = str(input('Introduzca el número de su oficina. Estos son los 4 primeros números que'
                    'aparecen tras el número de su entidad bancaria: '))

while 3 >= len(oficina) or len(oficina) > 4:
    oficina = str(input('Ha introducido un número erróneo. Revise correctamente su número de oficina: '))

num_cuenta = str(input('Finalmente introduzca por favor su número de cuenta. Son los 10 últimos dígitos de su IBAN: '))

while 9 >= len(num_cuenta) or len(num_cuenta) > 10:
    num_cuenta = str(input('Ha introducido un número erróneo. Revise correctamente su número de cuenta: '))

# Primer dígito de control.

entidad_1 = int(entidad[0:1]) * 4
entidad_2 = int(entidad[1:2]) * 8
entidad_3 = int(entidad[2:3]) * 5
entidad_4 = int(entidad[-1]) * 10

oficina_1 = int(oficina[0:1]) * 9
oficina_2 = int(oficina[1:2]) * 7
oficina_3 = int(oficina[2:3]) * 3
oficina_4 = int(oficina[-1]) * 6

suma = entidad_1 + entidad_2 + entidad_3 + entidad_4 + oficina_1 + oficina_2 + oficina_3 + oficina_4
resto = suma % 11
Primer_Digito = 11 - resto

if Primer_Digito == 10:
    Primer_Digito = 1
elif Primer_Digito == 11:
    Primer_Digito = 0

# Segundo dígito de control.

cuenta_1 = int(num_cuenta[0:1]) * 1
cuenta_2 = int(num_cuenta[1:2]) * 2
cuenta_3 = int(num_cuenta[2:3]) * 4
cuenta_4 = int(num_cuenta[3:4]) * 8
cuenta_5 = int(num_cuenta[4:5]) * 5
cuenta_6 = int(num_cuenta[5:6]) * 10
cuenta_7 = int(num_cuenta[6:7]) * 9
cuenta_8 = int(num_cuenta[7:8]) * 7
cuenta_9 = int(num_cuenta[8:9]) * 3
cuenta_10 = int(num_cuenta[-1]) * 6

suma_c = cuenta_1 + cuenta_2 + cuenta_3 + cuenta_4 + cuenta_5 + cuenta_6 + cuenta_7 + cuenta_8 + cuenta_9 + cuenta_10

resto_c = suma_c % 11
Segundo_Digito = 11 - resto_c

if Segundo_Digito == 10:
    Segundo_Digito = 1
elif Segundo_Digito == 11:
    Segundo_Digito = 0

print('Su dígito de control es', str(Primer_Digito) + str(Segundo_Digito))


# Actividad 47 - Queremos calcular la letra del DNI. El algoritmo para ello es el siguiente:
# 1. División entera del número de DNI entre 23.
# 2. A cada resto se le asocia una letra según la tabla presentada.

DNI_sin_letra = 0
resto = 0
i = 0
lista = []

print('Calcularemos la letra de su DNI')
DNI_sin_letra = int(input('Escriba su DNI sin la letra: '))
resto = DNI_sin_letra % 23

lista = ['T','R','W','A','G','M','Y','F','P','D','X','B','N','J','Z','S','Q','V','H','L','C','K','E']

print('La letra de su DNI número', DNI_sin_letra, 'es', lista[resto])

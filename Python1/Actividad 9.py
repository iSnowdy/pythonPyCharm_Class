# Actividad 9 - Queremos saber la nota necesaria en el tercer control para aprobar la asignatura.
# Pedimos la nota de los dos primeros exámenes y la de laboratorio. Sabiendo esto,
# mostramos la nota del tercer control que el usuario necesita para tener una nota final de 60.

Nc = 0
Nf = 0
NL = 0
C1 = 0
C2 = 0
C3 = 0

print('El promedio de exámenes es Nc.' '\nEl promedio de laboratorio es NL.' '\nY la nota final es Nf.')

C1 = float(input('Por favor, introduzca la nota de su primer examen: '))
C2 = float(input('Por favor, introduzca la nota de su segundo examen: '))
NL = float(input('Por favor, introduzca la nota obtenida de laboratorio: '))
Nf = 60  # Si aquí en vez de asignarle un valor fijo, le pedimos al usuario qué nota final quiere sacar, es posible
         # calcularla.
print('Queremos tener como nota final', Nf)

NL = NL * 0.3
print(NL)
NC = (Nf - NL)/0.7
print(NC)

C3 = (NC*3) - (C1 + C2)
print(C3)

print('Necesitará una nota de', C3, 'en el tercer examen para poder sacar una nota final de 60')

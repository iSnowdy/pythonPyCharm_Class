# Actividad 15 - Escribir un programa que pida el año actual y un año cualquiera. Luego, queremos
# imprimir al usuario cuántos años han pasado desde este o cuántos faltan.

Año_Actual = 0
Año_Cualquiera = 0
Año_Resultado = 0

Año_Actual = int(input('Escriba el año actual: '))
Año_Cualquiera = int(input('Escriba un año cualquiera: '))

if Año_Actual < Año_Cualquiera:
    Año_Resultado = Año_Cualquiera - Año_Actual
    print('Para llegar al año', Año_Cualquiera, 'faltan', Año_Resultado, 'años')
else:
    Año_Resultado = Año_Actual - Año_Cualquiera
    print('Desde el año', Año_Actual, 'han pasado', Año_Resultado,'años')

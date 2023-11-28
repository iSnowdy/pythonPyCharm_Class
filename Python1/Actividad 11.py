# Actividad 11 - Queremos calcular el IRPF en base al sueldo. Conociendo la tabla, queremos que al
# introducir nuestro sueldo nos aplique el porcentaje correspondiente al rango salarial y muestre tanto el
# sueldo bruto como neto.

bruto = 0
neto = 0

bruto = float(input('Introduzca su sueldo bruto: '))


if bruto<1000:
    neto = bruto * 1
    print('Siendo su sueldo bruto',bruto,', una vez aplicado el IRPF, su sueldo neto, sería',neto,)


if 1000<=bruto<2000:
    neto = bruto * (1-5/100)
    print('Siendo su sueldo bruto',bruto,', una vez aplicado el IRPF, su sueldo neto, sería',neto,)


if 2000<=bruto<4000:
    neto = bruto * (1-10/100)
    print('Siendo su sueldo bruto',bruto,', una vez aplicado el IRPF, su sueldo neto, sería',neto,)


if bruto>4000:
    neto = bruto * (1-12/100)
    print('Siendo su sueldo bruto',bruto,', una vez aplicado el IRPF, su sueldo neto, sería',neto,)

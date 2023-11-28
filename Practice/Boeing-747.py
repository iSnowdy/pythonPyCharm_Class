'''

Un BOEING 747 tiene una capacidad de carga para equipaje de aproximadamente 18.000
Kg.

Confeccione un diagrama de flujo que controle la recepci ´on de equipaje, sabiendo que:
Se deben rechazar los bultos de m´as de 500 Kg.
El valor por Kg del bulto es :

• de 0 a 25 Kg. $1000 por Kg.
• de 26 a 300 Kg. $1500 por Kg.
• de 301 a 500 Kg. $2000 por Kg.

Notar que los pesos siempre estar ´an en Kg (sin decimales). Considere que el precio por un bulto
de 30 Kg es 30 ∗ 1500 y no 25 ∗ 1000 + 5 ∗ 1500.
Cuando se intente agregar un nuevo bulto y con ´este se sobrepasen los 18, 000Kg de carga en
el avi ´on, el programa no debe agregar dicho bulto y debe mostrar la siguiente informaci ´on con
respecto al vuelo:

a) N ´umero total de bultos.
b) Peso del bulto m´as pesado.
c) Peso promedio de los bultos.
d) Ingreso total por concepto de carga en el avi ´on.

Nota: Asuma que los bultos se ingresan uno por uno. Adem ´as habr ´an suficientes bultos para
copar la capacidad del avi ´on.

'''

boeing_747 = 18000
peso_total_equipaje = 0
bulto = 0
to_pay = 0
lista_bulto = []
lista_to_pay = []

while peso_total_equipaje < boeing_747:

    loop = False

    while not loop:

        try:
            bulto = int(input('¿Cuánto pesa su bulto? Ha de añadir un número entero y en Kg '))
            lista_bulto = lista_bulto + [bulto]
        except ValueError:
            print('Entrada inválida. Vuelva a introducir el número entero')
        else:
            loop = True

    if bulto > 500:
        print('El bulto no puede sobre pasar los 500 Kg por persona. Lo sentimos.')
        lista_bulto.remove(bulto)
        print(lista_bulto)

    else:

        peso_total_equipaje = peso_total_equipaje + bulto
        if 0 <= bulto <= 25:

            to_pay = bulto * 1000
            print('Usted deberá pagar $1000 por kilogramo. Es decir, $' + str(to_pay))
            lista_to_pay = lista_to_pay + [to_pay]

        elif 26 <= bulto <= 300:

            to_pay = bulto * 1500
            print('Usted deberá pagar $1500 por kilogramo. Es decir, $' + str(to_pay))
            lista_to_pay = lista_to_pay + [to_pay]

        elif 301 <= bulto <= 500:

            to_pay = bulto * 2000
            print('Usted deberá pagar $2000 por kilogramo. Es decir, $' + str(to_pay))
            lista_to_pay = lista_to_pay + [to_pay]

    print('Hay un total de', len(lista_bulto), 'bultos')
    print('El bulto más pesado es de', max(lista_bulto), ' kg')
    print('El peso promedio de los bultos es de', sum(lista_bulto)/len((lista_bulto)), ' kg')
    print('Se han ingresado un total de $', sum(lista_to_pay))
    print(peso_total_equipaje)
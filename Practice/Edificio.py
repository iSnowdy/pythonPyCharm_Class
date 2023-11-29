'''

Un edificio tiene 25 pisos de 8 departamentos cada uno. La due ˜na del edificio ha
definido una estrategia para ponerle precio a cada departamento.

El n ´umero que identifica cada departamento se divide en dos partes:

los dos ´ultimos d´ıgitos indican en qu´e posici ´on est´a (de acuerdo al
diagrama), y los restantes indican el piso. Por ejemplo, el departa-
mento 1105 est´a en el und´ecimo piso, en la posici ´on 5.
Los dos departamentos al extremo derecho del diagrama tienen vista
al mar, y los dos del extremo izquierdo tienen vista al cerro.

0 1 2 3
4 5 6 7
Vista al mar
Vista al cerro

Todos los departamentos del primer piso valen 100, y todos los departamentos del ´ultimo
piso valen 400.

Para los pisos intermedios, se ha fijado un precio base de 245; el precio de los departamentos
con vista al mar se aumentar´a en 13 %, y el de los con vista al cerro se rebajar´a en 17 %. Los
decimales se redondear´an hacia abajo.

Adicionalmente, se difundi ´o el rumor de que el ´ıdolo adolescente Justino Vivar habr´ıa alo-
jado una noche en el departamento 807. Como hay un gran inter´es entre sus fan´aticas por
adquirir este departamento, la due ˜na ha decidido fijar su precio en 500.

Escriba un programa que pregunte al comprador el n ´umero del departamento, y le entregue
cu´al es el precio de ese departamento.

'''


print('Dígame el número del departamento que desea')
departamento = str(input('Departamento: '))

print(departamento)

if len(departamento) == 3:

    piso = int(departamento[0])
    print('Piso ', piso)

elif len(departamento) == 4:

    piso = int(departamento[:2])
    print('Piso ', piso)

dpto = int(departamento[-1])
print('Departamento', dpto)

print(type(piso))
print(type(dpto))

precio = 0

if piso == 1:

    precio = 100

elif piso == 25:

    precio = 400

else:

    precio = 245

    if dpto == 7 or dpto == 3:

        precio = round(245 * 1.13, 0)

    elif dpto == 0 or dpto == 4:

        precio = round(245 * 0.83, 0)


if piso == 8 and dpto == 7:

    precio = 500

print(precio)
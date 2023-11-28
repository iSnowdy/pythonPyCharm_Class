# Actividad 10 - Queremos un programa que calcule el índice de masa corporal (IMC). Pediremos al usuario su estatura
# y peso y mostraremos el resultado en pantalla.
# Opcionalmente, podemos mostrar que nos diga la clasificación según la Organización Mundial de la Salud de su IMC.

altura = 0
peso = 0
IMC = 0

# Creamos un comando que pida al usuario su estatura. Sin embargo, lo restringimos de forma que sólo acepte un valor
# válido. Se define como valor válido la altura mínima y máxima (según Google) registrada en humanos.

altura = float(input('Indique por favor su estatura en metros: '))
while altura < 0.6 or altura > 2.6:
    altura = float(input('Por favor introduzca un valor correcto de su altura: '))

# Hacemos lo mismo que con la estatura pero con el peso.

peso = float(input('Indique por favor su peso en kilogramos: '))
while peso < 20 or peso > 600:
    peso = float(input('Por favor introduzca un valor correcto de su peso: '))
else:
    print('Gracias. Ahora procederemos a calcular su índice de masa corporal o IMC')

IMC = peso/altura**2
IMC = round(IMC, 3)
print('Su IMC es', IMC)

# Definimos las diferentes clasificaciones de IMC según la OMS. Luego, según el valor de IMC obtenido del usuario,
# se le imprime en pantalla su clasificación. Se redondea a 3 cifras el IMC para que entre dentro del espectro de
# los valores otorgados.

clas1 = 'Infrapeso: Delgadez Severa'
clas2 = 'Infrapeso: Delgadez moderada'
clas3 = 'Infrapeso: Delgadez aceptable'
clas4 = 'Peso Normal'
clas5 = 'Sobrepeso'
clas6 = 'Obeso: Tipo I'
clas7 = 'Obeso: Tipo II'
clas8 = 'Obeso: Tipo III'

if IMC < 16:
    print('Según la Organización Mundial de la Salud, usted entra dentro de la clasificación:', clas1)
if 16 <= IMC <= 16.999:
    print('Según la Organización Mundial de la Salud, usted entra dentro de la clasificación:', clas2)
if 17 <= IMC <= 18.499:
    print('Según la Organización Mundial de la Salud, usted entra dentro de la clasificación:', clas3)
if 18.50 <= IMC <= 24.999:
    print('Según la Organización Mundial de la Salud, usted entra dentro de la clasificación:', clas4)
if 25 <= IMC <= 29.999:
    print('Según la Organización Mundial de la Salud, usted entra dentro de la clasificación:', clas5)
if 30 <= IMC <= 34.999:
    print('Según la Organización Mundial de la Salud, usted entra dentro de la clasificación:', clas6)
if 35 <= IMC <= 40:
    print('Según la Organización Mundial de la Salud, usted entra dentro de la clasificación:', clas7)
if IMC > 40:
    print('Según la Organización Mundial de la Salud, usted entra dentro de la clasificación:', clas8)

# Capítulo uno


print('Hello world')

print(1,2,3,4,5)
print(1,2,3,4,5, sep=',')
print(1,2,4,5, sep='; ', end='.') # sep es al final de cada elemento del print y end al final de toda la cadena
print(1,2,3,4,5, sep=': ', end=' this \n') # cada final de elemento está determinado por puntuaciones
print(123,4,5, sep=': ', end=' this \n') # Si se le añade end, hay que dar salto de línea o se muestra seguido


lista = ['gato', 'perro', 'raton']
print(lista)
lista = lista + ['delfin']
print(lista)

string = ('hola mundo')
print(string)
print(string.capitalize())
string = string.upper()
print(string)
print(string.casefold())
print(string.lower())
print(string.center(50))

print(string.center(50, '.'))

print('End of Chapter 1')

# Capítulo 2

numero = int(input('Número de 1 al 10: '))
if numero > 10:
    print('¡Has escrito un numero mayor que 10!')
print('El número que has escrito es' + ' ' + str(numero))
print('El número que has escrito es', numero)

i = 0
while i < 10:
    i += 1
    print(i)

j = 0
while j < 10:
    j += 2
    print(j, end='\n')

for item1 in range(3): # El bucle externo se realiza elemento por elemento suyo sobre el bucle interno
    for item2 in range(5):
        print('Item1:' + ' ' + str(item1), 'Item2:' + ' ' + str(item2))
        # Así pues, se realiza el item1 3 veces. Y cada item1 se realiza 5 veces sobre el item2

print('--------------')

item1 = 0
while item1 < 3:
    for item2 in range(5):
        print('Item1:' + ' ' + str(item1), 'Item2:' + ' ' + str(item2))
    item1 += 1
    print('Programa finalizado')

print('--------------')

item1 = 0
while item1 < 3:
    item2 = 0
    while item2 < 5:
        print('Item1: ' + str(item1), 'Item2: ' + str(item2))
        item2 += 1
    item1+= 1
    print('Programa')

print('End of Chapter 2')

# Capítulo 3


def sumarRestar (param1, param2):

    return param1 + param2, param1 - param2


print(sumarRestar(10, 5))
resultadosuma, resultadoresta = sumarRestar(10, 5)

print('Esta es la suma obtenida', resultadosuma)
print('Esta es la resta obtenida', resultadoresta)


def sumarTodo (*valores): # Si se le pone el * pillará todos los datos que se le introduzcan como valores

    resultado = 0
    for item in valores: # Pero como tiene tantos datos, hay que recorrerlos con un for
        resultado = resultado + item

    print(type(item))
    print(type(valores))

    return resultado


result = sumarTodo(5, 10, 15, 20, 25)
print('El resultado total es', result)


print('End of Chapter 3')


# Capítulo 4

class Punto:
    def __init__(self, x, y):
        self.X = x
        self.Y = y
    def showPoint(self):
        print('El punto es (', self.X, ',', self.Y, ')')


p1 = Punto(4, 6)
p1.showPoint()
print(type(p1))

p1.X = 7
p1.showPoint()



class Point:

    def __init__(self, x, y):

        self.X = x
        self.Y = y

    def showthis(self):
        print('El punto es(', self.X, ',', self.Y, ')')


class Triangle:

    def __init__(self, v1, v2, v3):

        self.V1 = v1
        self.V2 = v2
        self.V3 = v3

    def showvertex(self):

        self.V1.showthis()
        self.V2.showthis()
        self.V3.showthis()


v1 = Point(3, 4)
v2 = Point(6, 8)
v3 = Point(9, 2)

triangulo = Triangle(v1, v2, v3)
triangulo.showvertex()


print('End of Chapter 4')



# Capítulo 5 - Encapsulamiento, herencia y herencia múltiple


class PublicPoint: # los datos o atributos que componen esta clase son públicos o accesibles sin control

    def __init__(self, x, y):

        self.X = x
        self.Y = y


class PrivatePoint: # los datos o atributos que componenen esta clase son privados o accesibles de forma controlada

    def __init__(self, x, y):

        self._X = x
        self._Y = y

    def GetX(self): # método para leer

        return self._X

    def GetY(self):

        return self._Y

    def SetX(self, x): # método para escribir

        self._X = x

    def SetY(self, y):

        self._Y = y


public = PublicPoint(4, 6)
private = PrivatePoint(6, 4)

print('Public data: ', public.X,',', public.Y)
print('Private data: ', private.GetX(),',', private.GetY())

# Modificamos los datos

public.X = 2
private.SetX(9) # Así modificamos datos privados

print('Public data modified: ', public.X,',', public.Y)
print('Private data modified: ', private.GetX(),',', private.GetY())


class OperateValues:

    def __init__(self, x, y):

        self._X = x
        self._Y = y

    def __Addition(self): # los métodos también pueden ser privados como lo es este y el siguiente

        return self._X + self._Y

    def __Subtract(self):

        return self._X - self._Y

    def Operate(self): # método público; el único al que podremos acceder

        print('The addition result is: ', self.__Addition())
        print('The subtract result is: ', self.__Subtract())


dostuff = OperateValues(100, 200)
dostuff.Operate()
# print('The result isA:', dostuff.__Addition()) Da error porque se está intentando acceder a un método privado


class Electrodomestico:

    def __init__(self):

        self._Encendido = False
        self._Tension = 0

    def Encender(self):

        self._Encendido = True

    def Apagar(self):

        self._Encendido = False

    def Encendido(self):

        return self._Encendido

    def SetTension(self, tension):

        self._Tension = tension

    def GetTension(self):

        return self._Tension


class Lavadora(Electrodomestico):

    def __init__(self):

        self._RPM = 0
        self._Kilos = 0

    def SetRPM(self, rpm):

        self._RPM = rpm

    def SetKilos(self, kilos):

        self._Kilos = kilos

    def MostrarLavadora(self):

        print('--------------------')
        print('Lavadora:')
        print('\tRPM: ', self._RPM)
        print('\tKilos: ', self._Kilos)
        print('\tTension: ', self.GetTension())
        if self.Encendido():
            print('\tLavadora encendida')
        else:
            print('\tLavadora no encendida')
        print('--------------------')


lavadora = Lavadora()
lavadora.SetRPM(1200)
lavadora.SetKilos(10)
lavadora.SetTension(250)
lavadora.Encender()
lavadora.MostrarLavadora()

lavadora = Lavadora()
lavadora.SetRPM(1200)
lavadora.SetKilos(10)
lavadora.SetTension(250)
lavadora.Apagar()
lavadora.MostrarLavadora()

print('on to the next one')

class Microondas(Electrodomestico):

    def __init__(self):

        self._PotenciaMaxima = 0
        self._Grill = False

    def SetPotenciaMaxima(self, potencia):

        self._PotenciaMaxima = potencia

    def SetGrill(self, grill):

        self._Grill = grill

    def MostrarMicroondas(self):

        print('--------------------')
        print('Microondas:')
        print('\tPotencia máxima: ', self._PotenciaMaxima)
        if self._Grill == True:
            print('\tGrill: Si')
        else:
            print('\tGrill: No')
        print('\tTension: ', self.GetTension())
        if self.Encendido():
            print('\tMicroondas encendido')
        else:
            print('\tMicroondas no encendido')
        print('--------------------')

microondas = Microondas()
microondas.SetPotenciaMaxima(800)
microondas.SetGrill(True)
microondas.SetTension(220)
microondas.Encender()
lavadora.MostrarLavadora()
microondas.MostrarMicroondas()
microondas.Apagar()
microondas.MostrarMicroondas()



class Hotel:

    def __init__(self):

        self._RoomNumbers = 0
        self._Stars = 0

    def SetRoomNumbers(self, rooms):

        self._RoomNumbers = rooms

    def SetStars(self, stars):

        self._Stars = stars

    def ShowHotel(self):

        print('--------------------')
        print('Hotel: ')
        print('\tStars: ', self._Stars)
        print('\tNumber of Rooms: ', self._RoomNumbers)
        print('--------------------')


class Restaurant:

    def __init__(self):

        self._Forks = 0
        self._OpeningTime = 0

    def SetForks(self, forks):

        self._Forks = forks

    def SetOpeningTime(self, time):

        self._OpeningTime = time

    def ShowRestaurant(self):

        print('--------------------')
        print('Restaurant: ')
        print('Number of Forks: ', self._Forks)
        print('Opening Time: ', self._OpeningTime)


class Business(Hotel, Restaurant):

    def __init__(self):

        self._Name = ''
        self._Adress =  ''
        self._Phone = 0

    def SetName(self, name):

        self._Name = name

    def SetAdress(self, adress):

        self._Adress = adress

    def SetPhone(self, phone):

        self._Phone = phone

    def ShowBusiness(self):

        print('--------------------')
        print('Business: ')
        print('\tName: ', self._Name)
        print('\tAdress: ', self._Adress)
        print('\tPhone: ', self._Phone)
        self.ShowHotel()
        self.ShowRestaurant()
        print('--------------------')


business = Business()
business.SetStars(4)
business.SetRoomNumbers(180)
business.SetForks(3)
business.SetOpeningTime(8)
business.SetName('Python Hotel')
business.SetAdress('Fake Street Taxi 155')
business.SetPhone('680555950')
business.ShowBusiness()


print('End of Chapter 5')



# Capítulo 6 - Ficheros


f = open('test.txt','r')
texto = f.read()
print(texto)
f.close()



for linea in open('test.txt', 'r'):

    print('This is one line:', linea)



f = open('test.txt', 'r')
print(f.readline())
print(f.readline()) # Leemos sólo 2 líneas del fichero. Si queremos seguir leyendo más, hay que repetir el comando

lineas = f.readline()
f.close()
print(len((lineas)))
print('Hello', lineas)

print(lineas[0])
print(lineas[1])
print(lineas[2])
print(lineas[3])


f = open('test.txt', 'r')
lineslist = list(f)
f.close()

print(type(lineslist))
print(len(lineslist))
print(lineslist)

for item in lineslist:
    print(item)




print('----------- Original Text File -----------')
fread = open('test.txt', 'r')
text = fread.read()
fread.close()
print(text)

print('----------- Inserting Data into the Text File -----------')
fedit = open('test.txt', 'a')
fedit.write('And like this I will be editing this file from PyCharm IDE\n')
fedit.close()

print('----------- Modified Text File -----------')
fread = open('test.txt', 'r')
text = fread.read()
print(text)

fcreate = open('anotherone.txt', 'x')
fcreate.write('And you shall be punished!\n')
fcreate.write('by Python')
fcreate.close()

fread = open('anotherone.txt', 'r')
text = fread.read()
fread.close()
print(text)

print('End of Chapter 6')



# Chapter 7 - Control de excepciones



try:
    print(3 / 0)
except:
    print('Error. No se puede dividir por cero')
else:
    print('División correcta')
finally:
    print('See you later!')


try:
    print(3 / 1)
except:
    print('Error. No se puede dividir por cero')
else:
    print('División correcta')
finally:
    print('See you later!')




try:
    print(3 / 0)
except ZeroDivisionError:
    print('Error. No se puede dividir por cero')
except:
    print('General error. Not zero division')
else:
    print('División correcta')
finally:
    print('See you later!')


print('End of Chapter 7')







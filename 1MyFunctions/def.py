def contador_vocales (vowels):
    print('¿Funciona?')
    contador = 0
    for letra in vowels:
        if letra.lower() in 'aeiouáéíóúäëïöüàèìòù': # Obligamos a que lo que haya en la frase se ponga en minus.
            contador += 1 # Contador. Es lo mismo que hacer i = i + 1
    return contador # Si no se hace un return no se completa la función.

def borrador_vocales (frase):
    texto = ''
    for letra in frase:
        if letra.lower() not in 'aeiouáéíóúäëïöüàèìòù':
            texto += letra # Te va añadiendo cada cosa que no esté incluida en esas vocales a la variable texto.
    return texto # Luego te saca la variable texto.

def contraseña(contra): # Validación de contraseñas

    validar = False # Comenzamos con el supuesto de que la contraseña es inválida.
    long = len(contra)
    mayusculas = False # Igual que antes. Para que cambie a True, deberá de tener minusc, mayusc y numeros.
    minusculas = False
    numeros = False
    alfan = contra.isalnum() # Si es alfanumérico, devolverá True. Queremos que devuelva False.

    correcto = True # Verificador de las condiciones

    for caracteres in contra: # Comprobamos letra por letra si es minusc, mayusc y numérico. Cuando al menos una lo sea,
        # nos devolverá True como validación de que ese requisito se cumple.

        if caracteres.islower() == True:
            minusculas = True

        if caracteres.isupper() == True:
            mayusculas = True

        if caracteres.isnumeric() == True:
            numeros = True

    if long > 8:
        validar = True

    if minusculas == True and mayusculas == True and numeros == True and alfan == False and validar == True:
        validar = True # Se cumplen todos los requisitos.
    else:
        correcto = False # No se cumplen. Cambiamos el verificador.

    if correcto == False:
        print('La contraseña elegida no es segura')

    elif correcto == True:
        return True


from random import sample

def safe_password(longitud): # Random password generator
    minusc = 'abcdefghijklmnñopqrstuvwxyzç'
    mayusc = minusc.upper()
    numeros = '0123456789'
    simbolos = '[]{}()*;,.-_/¿?¡!$%&@'

    secuencia = minusc + mayusc + numeros + simbolos

    contraseña_requisitos = sample(secuencia, longitud)

    contraseña_resultante = "".join(contraseña_requisitos)

    return contraseña_resultante

password = safe_password(15)

print('La contraseña es: ', password)

def letter_counter (oracion): # Contador de letras en una frase e introducirlas en diccionario
    d = {}
    oracion = oracion.lower() # Pasamos a minusculas
    oracion = oracion.replace(' ', '') # Quitamos espacios
    for letters in oracion:
        if letters not in d:
            d[letters] = 1 # Decimos que si el caracter de oracion no está ya en d, lo inicie a valor 1
        else:
            d[letters] += 1 # Y en caso de que lo esté, se vaya sumando
    d = dict(sorted(d.items())) # Ordenamos los elementos clave alfabéticamente
    return d

def initial_counter(new): # Contador de iniciales

    new = ''.join([words[0] for words in sentence.split()])
    print(new) # Hacemos una nueva lista con la primera letra de cada palabra en una lista que separamos por palabra
    d = {}
    oracion = new.lower() # Pasamos a minusculas
    for letters in oracion:
        if letters not in d:
            d[letters] = 1 # Decimos que si el caracter de oracion no está ya en d, lo inicie a valor 1
        else:
            d[letters] += 1 # Y en caso de que lo esté, se vaya sumando

    d = dict(sorted(d.items())) # Ordenamos los elementos clave alfabéticamente

    return d
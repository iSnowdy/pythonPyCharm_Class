mapping_type = dict(nombre="Tomeu", altura=1.78, age=50) # Tipo mapping

print(mapping_type)
print(type(mapping_type))

print(mapping_type.keys())
print(mapping_type.values())
print(mapping_type.items())


'''

def llenar_informacion_persona():
    # Crear un diccionario vacío para almacenar la información de la persona
    persona = {}

    continuar_ingresando = True

    while continuar_ingresando:
        # Solicitar al usuario que ingrese la información
        nombre = input("Ingrese el nombre de la persona: ")
        edad = input("Ingrese la edad de la persona: ")
        sexo = input("Ingrese el sexo de la persona: ")
        telefono = input("Ingrese el número de teléfono de la persona: ")
        correo = input("Ingrese el correo electrónico de la persona: ")

        # Añadir la información al diccionario
        persona['Nombre'] = nombre
        persona['Edad'] = edad
        persona['Sexo'] = sexo
        persona['Teléfono'] = telefono
        persona['Correo'] = correo

        # Imprimir el contenido del diccionario
        print("Información actualizada:")
        for clave, valor in persona.items():
            print(f"{clave}: {valor}")

        # Preguntar al usuario si desea continuar ingresando información
        respuesta = input("¿Quieres ingresar más información? (s/n): ")
        if respuesta.lower() != 's':
            continuar_ingresando = False

# Llamar a la función para llenar la información de la persona
llenar_informacion_persona()

'''

def llenar_informacion_persona():


    # Crear una lista para almacenar la información de cada persona
    lista_personas = []

    loop = True

    while loop:
        # Crear un diccionario vacío para almacenar la información de la persona actual
        persona = {}

        nombre = input("Ingrese el nombre de la persona: ")
        edad = input("Ingrese la edad de la persona: ")
        sexo = input("Ingrese el sexo de la persona: ")
        telefono = input("Ingrese el número de teléfono de la persona: ")
        correo = input("Ingrese el correo electrónico de la persona: ")

        # Añadir la información al diccionario
        persona['Nombre'] = nombre
        persona['Edad'] = edad
        persona['Sexo'] = sexo
        persona['Teléfono'] = telefono
        persona['Correo'] = correo

        # Añadir el diccionario a la lista de personas
        lista_personas.append(persona)

        # Imprimir el contenido del diccionario actual
        print("Información actualizada:")
        for clave, valor in persona.items():
            print(f"{clave}: {valor}")

        # Preguntar al usuario si desea continuar ingresando información
        respuesta = input("¿Quieres ingresar más información? (Y/N): ").lower()
        if respuesta.lower() != 'y':
            loop = False

    # Imprimir la información acumulada en la lista
    print("\nInformación acumulada:")
    for idx, persona in enumerate(lista_personas, start=1):
        print(f"\nPersona {idx}:")
        for clave, valor in persona.items():
            print(f"{clave}: {valor}")


llenar_informacion_persona()

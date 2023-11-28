n = int(input("Numero de universidades: "))

uni_acepta = 0
uni_rechaza = 0
uni_empata = 0

for i in range(n):
    universidad = input("Universidad: ")
    voto = "hola"

    acepta = 0
    rechaza = 0
    blanco = 0
    nulo = 0

    while voto != 'X':
        voto = input("Voto: ")
        if voto == 'A':
            acepta += 1
        elif voto == 'R':
            rechaza += 1
        elif voto == 'B':
            blanco += 1
        elif voto == 'N':
            nulo += 1

    print
    universidad + str(':') + " " + str(acepta) + " aceptan", rechaza, "rechazan", blanco, "blancos", nulo, "nulos."
    if acepta > rechaza:
        uni_acepta += 1
    elif acepta == rechaza:
        uni_empata += 1
    else:
        uni_rechaza += 1
    print

print(
"Universidades que aceptan:", uni_acepta)
print(
"Universidades que rechazan:", uni_rechaza)
print(
"Universidades con empate:", uni_empata)
a = [5, 1, 4, 9, 0]
c = [[1, 2], [3, 4, 5], [6, 7]]
e = ['a', a, a*4]

print(e[c[0][1]].count(5))

print(e[2])
print(e)


x = 25

if x <= 25:
    if x != 0:
        if x > 15 and x < 30:
            if 0 <= x < 50:
                print("Examen")
else:
    print("Programacion")
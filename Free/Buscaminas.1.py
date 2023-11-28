import random
# import os

mineCount = 3
dimension = [6, 5]
mine = []
board = []

for i in range(mineCount):

    mine.append([])
    mine[i].append(random.randint(0, (dimension[0])-1))
    mine[i].append(random.randint(0, (dimension[1])-1))

for i in range(dimension[1]):
    board.append([])

    for j in range(dimension[0]):
        board[i].append(0)

        for l in mine:

            if l[0]-j == 0 and l[1]-i == 0:

                board[i][j] = 'M'
                break

            elif abs(l[0]-j) < 2 and abs(l[1]-i) < 2:

                board[i][j] += 1


# os.system('clear')


print('----BUSCAMINAS----\n')

for i in mine:
    print(mine)

for i in range(len(board)):

    for j in board[i]:

        print(j, end='  ')

    print('\n')

covered = []
coveredCount = 0

while coveredCount < mineCount:

    cover = list([int(input('Columna: ')), int(input('Fila: '))])
    # os.system('clear')

    print('----BUSCAMINAS----\n')

    if cover in mine:
        print('Has perdido.\n')

        for i in range(len(board)):
            for j in board[i]:
                print(j,end='  ')
            print('\n')
        break

    covered.append(cover)

    for i in range(len(board)):

        for j in range(len(board[i])):

            if [j,i] in covered :

                print(board[i][j],end='  ')

            else:

                print('x', end='  ')

        print('\n')


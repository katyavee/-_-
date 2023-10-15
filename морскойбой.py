# План


# игроки ходят по очереди, вводят координаты клетки: если попал, значит ходишь еще раз, если нет, то следующий игрок
#   важно: при получении координат точки, программа должна проверить правильность ввода данных
# условия окончания партии: хотя бы у одного из игроков убиты все корабли, ничьи не существует
# после каждого хода программа выводит обновленное поле
# 0 - горизонталь, 1 - вертикаль
#

from random import randint

def pole(pole2):
    for i in pole2:
        print(*i)
def space_between_ships(ship, x_start, y_start, pole1, direction):
    if direction == 0:
        for i in range(int(ship)):
            if y_start + 1 <= 10:
                pole1[y_start + 1][x_start + i] = '-'
            if y_start - 1 >= 1:
                pole1[y_start - 1][x_start + i] = '-'
            if x_start + int(ship) <= 10:
                pole1[y_start][x_start + int(ship)] = '-'
                if y_start + 1 <= 10:
                    pole1[y_start + 1][x_start + int(ship)] = '-'
                if y_start - 1 >= 1:
                    pole1[y_start - 1][x_start + int(ship)] = '-'
            if x_start - 1 >= 1:
                pole1[y_start][x_start - 1] = '-'
                if y_start + 1 <= 10:
                    pole1[y_start + 1][x_start - 1] = '-'
                if y_start - 1 >= 1:
                    pole1[y_start - 1][x_start - 1] = '-'

    else:
        for i in range(int(ship)):
            if x_start + 1 <= 10:
                pole1[y_start + i][x_start + 1] = '-'
            if x_start - 1 >= 1:
                pole1[y_start + i][x_start - 1] = '-'
            if y_start + int(ship) <= 10:
                pole1[y_start + int(ship)][x_start] = '-'
                if x_start + 1 <= 10:
                    pole1[y_start + int(ship)][x_start + 1] = '-'
                if x_start - 1 >= 1:
                    pole1[y_start + int(ship)][x_start - 1] = '-'
            if y_start - 1 >= 1:
                pole1[y_start - 1][x_start] = '-'
                if x_start + 1 <= 10:
                    pole1[y_start - 1][x_start + 1] = '-'
                if x_start - 1 >= 1:
                    pole1[y_start - 1][x_start - 1] = '-'


pole1 = [['0' for k in range(11)] for i in range(11)]
pole1[0] = [' '] + [chr(i) for i in range(ord('A'), ord('A') + 10)]
for i in range(10):
    pole1[i + 1][0] = i + 1
pole2 = [row[:] for row in pole1]
ships_locations = []
ships1 = ['4', '3', '3', '2', '2', '2', '1', '1', '1', '1']
ships2 = ships1.copy()
columns = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10}
for ship in ships1:
    if ship == '4':
        direction = randint(0, 1)
        x_start = randint(1, 10)
        y_start = randint(1, 10)

        if direction == 0:
            while not (x_start <= 7):
                x_start = randint(1, 10)
            pole1[y_start][x_start: x_start + 4] = ['4', '4', '4', '4']
            space_between_ships(ship, x_start, y_start, pole1, direction)
            ships_locations.append([[y_start, x_start], [y_start, x_start + 1], [y_start, x_start + 2], [y_start, x_start +3]])
        else:
            while not (y_start <= 7):
                y_start = randint(1, 10)
            for i in range(4):
                pole1[y_start + i][x_start] = '4'
            space_between_ships(ship, x_start, y_start, pole1, direction)
            ships_locations.append([[y_start, x_start], [y_start + 1, x_start], [y_start + 2, x_start], [y_start + 3, x_start]])

    if ship == '3':
        direction = randint(0, 1)
        print(direction)
        x_start = randint(1, 10)
        y_start = randint(1, 10)

        if direction == 0:
            while x_start > 8 or pole1[y_start][x_start] != '0' or pole1[y_start][x_start + 1] != '0' or pole1[y_start][x_start + 2] != '0':
                x_start = randint(1, 10)
                y_start = randint(1 , 10)
            pole1[y_start][x_start: x_start + 3] = ['3', '3', '3']
            space_between_ships(ship, x_start, y_start, pole1, direction)
            ships_locations.append([[y_start, x_start], [y_start, x_start + 1], [y_start, x_start + 2]])


        else:
            while y_start > 8 or pole1[y_start][x_start] != '0' or pole1[y_start + 1][x_start] != '0' or pole1[y_start + 2][x_start] != '0':
                y_start = randint(1, 10)
                x_start = randint(1, 10)

            for i in range(3):
                pole1[y_start + i][x_start] = '3'
            space_between_ships(ship, x_start, y_start, pole1, direction)
            ships_locations.append([[y_start, x_start], [y_start + 1, x_start], [y_start + 2, x_start]])
    if ship == '2':
        direction = randint(0, 1)
        x_start = randint(1, 10)
        y_start = randint(1, 10)

        if direction == 0:
            while x_start > 9 or pole1[y_start][x_start] != '0' or pole1[y_start][x_start + 1] != '0':
                x_start = randint(1, 10)
                y_start = randint(1 , 10)
            pole1[y_start][x_start: x_start + 2] = ['2', '2']
            space_between_ships(ship, x_start, y_start, pole1, direction)
            ships_locations.append([[y_start, x_start], [y_start, x_start + 1]])

        else:
            while y_start > 9 or pole1[y_start][x_start] != '0' or pole1[y_start + 1][x_start] != '0':
                y_start = randint(1, 10)
                x_start = randint(1, 10)
            for i in range(2):
                pole1[y_start + i][x_start] = '2'
            space_between_ships(ship, x_start, y_start, pole1, direction)
            ships_locations.append([[y_start, x_start], [y_start + 1, x_start]])
    if ship == '1':
        direction = randint(0, 1)
        x_start = randint(1, 10)
        y_start = randint(1, 10)

        if direction == 0:
            while x_start > 10 or pole1[y_start][x_start] != '0':
                x_start = randint(1, 10)
                y_start = randint(1 , 10)
            pole1[y_start][x_start] = '1'
            space_between_ships(ship, x_start, y_start, pole1, direction)
            ships_locations.append([[y_start, x_start]])

        else:
            while y_start > 10 or pole1[y_start][x_start] != '0':
                y_start = randint(1, 10)
                x_start = randint(1, 10)
            pole1[y_start][x_start] = '1'
            space_between_ships(ship, x_start, y_start, pole1, direction)
            ships_locations.append([[y_start, x_start]])

for i in pole1:
    print(*i)
while len(ships_locations) >= 1:
    hod_col = input('введите номер столбца (ABCDEFGHIJ)')
    while hod_col not in columns:
        hod_col = input('введите номер столбца (ABCDEFGHIJ)')
    hod_row = input('введите номер строки (12345678910)')
    while hod_row not in [str(i) for i in range(1, 11)]:
        hod_row = input('введите номер строки (12345678910)')
    hod_row = int(hod_row)


    flag = True
    for ship in ships_locations:
        if [hod_row, columns[hod_col]] in ship:
            pole2[hod_row][columns[hod_col]] = '+'
            flag = True
            ship.remove([hod_row, columns[hod_col]])
            if not ship:
                print('корабль убит')
                ships_locations.remove(ship)
            else:
                print('корабль ранен')
            break
        else:
            flag = False
    if flag == False:
        print('пусто')


    pole(pole2)
print('game is over')
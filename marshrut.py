
import random

coord = []

def get_SIZE():
    SIZE = int(input("Введите размер лабиринта: "))
    # SIZE = 10
    return SIZE

def create_board():
    SIZE = get_SIZE()
    return [[0 for j in range(SIZE)] for i in range(SIZE)]

def print_field():
    global board
    for row in board:
        for col in row:
            print(col, end="  ")
        print()

def mark_on_field_1(x, y, symbol):
    board[x][y] = symbol

def mark_on_field_2(k, h, symbol):
    board[k][h] = symbol

def get_start():
    global board
    print("Введите координаты точки старта:")
    y1 = (int(input("Введите x координату: ")) - 1)
    x1 = (int(input("Введите y координату: ")) - 1)
    # y1 = 0
    # x1 = 0
    mark_on_field_1(x1, y1, 2)
    return x1, y1

def get_finish():
    global board
    print("Введите координаты точки финиша:")
    y2 = (int(input("Введите x координату: ")) - 1)
    x2 = (int(input("Введите y координату: ")) - 1)
    # y2 = 9
    # x2 = 9
    mark_on_field_1(x2, y2, 6)
    return x2, y2

def get_level():
    level = 0

    if len(coord) > 1:

        while True:
            level = int(input("Введите колличество усложнений лабиринта: "))
            if level > (len(coord)//2):
                print("Колличество ошибок не подходит под выбранные вами точки старта и финиша, введите сложность меньше ")
            else:
                return level
    else:
        print("Для автоматической генерации маленький путь между точками старта и финиша")
        exit(0)

def check_points(k1, h1):
    if board[k1 - 1][h1 - 1] != 1 and board[k1 + 1][h1 + 1] != 1 and board[k1 + 1][h1 - 1] != 1 and board[k1 - 1][h1 + 1] != 1:
        b = 1
        return b
    else:
        b = 0
        return b



def go_left(k1, h1, symbol):
    global checker
    global counter
    print("Отдано влево")

    if h1 - 4 < len(board[0]) and h1 - 4 >= 0 and board[k1][h1 - 1] < 2 and board[k1][h1 - 2] < 2 and board[k1][h1 - 3] < 2 and board[k1][h1 - 4] == 0\
            and board[k1 + 1][h1 - 1] == 0 and board[k1 - 1][h1 - 1] == 0:
        print("Лево 3")
        mark_on_field_2(k1, h1 - 1, 1)
        mark_on_field_2(k1, h1 - 2, 1)
        mark_on_field_2(k1, h1 - 3, 1)
        if symbol == 1:
            get_random_turn(k1, (h1 - 3), 11, 16)

    elif h1 - 3 < len(board[0]) and h1 - 3 >= 0 and board[x1][h1 - 1] < 2 and board[x1][h1 - 2] < 2 and board[k1][h1 - 3] == 0\
            and board[k1 + 1][h1 - 1] == 0 and board[k1 - 1][h1 - 1] == 0:
        print("Лево 2")
        mark_on_field_2(k1, h1 - 1, 1)
        mark_on_field_2(k1, h1 - 2, 1)
        if symbol == 1:
            get_random_turn(k1, (h1 - 2), 11, 16)

    elif h1 - 2 < len(board[0]) and h1 - 2 >= 0 and board[x1][h1 - 1] == 0:
        print("Лево 1")
        get_random_turn(k1, h1, 5, 8)

    else:
        if checker == 0:
            checker += 1
            print("инверсия")
            go_right(k1, h1, symbol)

        else:
            counter -= 1
            mark_on_field_2(k1, h1, 1)
            checker = 0
            print("сброс")

def go_right(k1, h1, symbol):
    global checker
    global counter
    print("Отдано ввправо")

    if h1 + 4 < len(board[0]) and h1 + 4 >= 0 and board[k1][h1+ 1] < 2 and board[k1][h1 + 2] < 2 and board[k1][h1 + 3] < 2 and board[k1][h1 + 4] == 0\
            and board[k1 + 1][h1 + 1] == 0 and board[k1 - 1][h1 + 1] == 0:
        print("Право 3")
        mark_on_field_1(k1, h1 + 1, 1)
        mark_on_field_1(k1, h1 + 2 ,1)
        mark_on_field_1(k1, h1 + 3, 1)
        if symbol == 1:
            get_random_turn(k1, (h1 + 3), 13, 18)

    elif h1 + 3 < len(board[0]) and h1 + 3 >= 0 and board[k1][h1 + 1] < 2 and board[k1][h1 + 2] < 2 and board[k1][h1 + 3] == 0\
            and board[k1 + 1][h1 + 1] == 0 and board[k1 - 1][h1 + 1] == 0:
        print("Право 2")
        mark_on_field_1(k1, h1 + 1, 1)
        mark_on_field_1(k1, h1 + 2 ,1)
        if symbol == 1:
            get_random_turn(k1, (h1 + 2), 13, 18)

    elif h1 + 2 < len(board[0]) and h1 + 2 >= 0 and board[k1][h1 + 1] == 0:
        print("Право 1")
        get_random_turn(k1, h1, 5, 8)

    else:
        if checker == 0:
            checker += 1
            print("инверсия")
            go_left(k1, h1, symbol)

        else:
            counter -= 1
            checker = 0
            print("сброс")
            mark_on_field_2(k1, h1, 1)

def go_down(k1, h1, symbol):
    global checker
    global counter
    print("Отдано вниз")

    if k1 + 4 < len(board) and k1 + 4 >= 0 and board[k1 + 1][h1] < 2 and board[k1 + 2][h1] < 2 and board[k1 + 3][h1] < 2 and board[k1 + 4][h1] == 0\
            and board[k1 + 1][h1 - 1] == 0 and board[k1 + 1][h1 + 1] == 0:
        print("Низ 3")
        mark_on_field_1(k1 + 1, h1, 1)
        mark_on_field_1(k1 + 2, h1, 1)
        mark_on_field_1(k1 + 3, h1, 1)
        if symbol == 1:
            get_random_turn((k1 + 3), h1, 15, 20)

    elif k1 + 3 < len(board) and k1 + 3 >= 0 and board[k1 + 1][h1] < 2 and board[k1 + 2][h1] < 2 and board[k1 + 3][h1] == 0\
            and board[k1 + 1][h1 - 1] == 0 and board[k1 + 1][h1 + 1] == 0:
        print("Низ 2")
        mark_on_field_1(k1 + 1, h1, 1)
        mark_on_field_1(k1 + 2, h1, 1)
        if symbol == 1:
            get_random_turn((k1 + 2), h1, 15, 20)

    elif k1 + 2 < len(board) and k1 + 2 >= 0 and board[k1 + 1][h1] == 0:
        print("Низ 1")
        get_random_turn(k1, h1, 1, 4)

    else:
        if checker == 0:
            checker += 1
            print("инверсия")
            go_up(k1, h1, symbol)

        else:
            counter -= 1
            checker = 0
            print("сброс")
            mark_on_field_2(k1, h1, 1)

def go_up(k1, h1, symbol):
    global checker
    global counter
    print("Отдано вверх")

    if k1 - 4 < len(board) and k1 - 4 >= 0 and board[k1 - 1][h1] < 2 and board[k1 - 2][h1] < 2 and board[k1 - 3][h1] < 2 and board[k1 - 4][h1] == 0\
            and board[k1 - 1][h1 - 1] == 0 and board[k1 - 1][h1 + 1] == 0:
        print("Верх 3")
        mark_on_field_1(k1 - 1,h1, 1)
        mark_on_field_1(k1 - 2,h1, 1)
        mark_on_field_1(k1 - 3,h1, 1)
        if symbol == 1:
            get_random_turn((k1 - 3), h1, 9, 14)

    elif k1 - 3 < len(board) and k1 - 3 >= 0 and board[k1 - 1][h1] < 2 and board[k1 - 2][h1] < 2 and board[k1 - 3][h1] == 0\
            and board[k1 - 1][h1 - 1] == 0 and board[k1 - 1][h1 + 1] == 0:
        print("Верх 2")
        mark_on_field_1(k1 - 1,h1, 1)
        mark_on_field_1(k1 - 2,h1, 1)
        if symbol == 1:
            get_random_turn((k1 - 2), h1, 9, 14)

    elif k1 - 2 < len(board) and k1 - 2 >= 0 and board[k1 - 1][h1] == 0:
        print("Верх 1")
        get_random_turn(k1, h1, 1, 4)

    else:
        if checker == 0:
            checker += 1
            print("инверсия")
            go_down(k1, h1, symbol)

        else:
            counter -= 1
            checker = 0
            print("сброс")
            mark_on_field_2(k1, h1, 1)



def print_way_right(k1, h1, k2, h2, symbol):
    global counter_
    while True:
        if h2 != h1 and board[k1][h1+1] < 2:
            h1 += 1
            mark_on_field_2(k1, h1, 1)
            coord.append((h1, k1))
            if symbol == 1:
                counter_ += 1

        else:
            return

def print_way_left(k1, h1, k2, h2, symbol):
    global counter_
    while True:
        if h2 != h1  and board[k1][h1-1] < 2:
            h1 -= 1
            mark_on_field_2(k1, h1, 1)
            coord.append((h1, k1))
            if symbol == 1:
                counter_ += 1
        else:
            return

def print_way_down(k1, h1, k2, h2, symbol):
    global counter_
    while True:
        if k2 != k1 and board[k1 + 1][h1] < 2:
            k1 += 1
            mark_on_field_2(k1, h1, 1)
            coord.append((h1, k1))
            if symbol == 1:
                counter_ += 1
        else:
            return

def print_way_up(k1, h1, k2, h2, symbol):
    global counter_
    while True:
        if k2 != k1 and board[k1-1][h1] < 2:
            k1 -= 1
            mark_on_field_2(k1, h1, 1)
            coord.append((h1, k1))
            if symbol == 1:
                counter_ += 1
        else:
            return

def del_coord(counter_):
    global coord
    del coord[counter_ + 1]
    del coord[counter_ ]
    del coord[counter_ - 1]
    del coord[counter_ - 2]
    del coord[counter_ - 3]

def check_edge(k, h):
    a = 0
    if k == 0 and h == 0:
        mark_on_field_2(k, (h +1), 1)
        mark_on_field_2((k+1), (h + 1), 1)
        k += 1
        h += 1
        a = 1
        return a

    elif k == 0:
        mark_on_field_2((k + 1), h, 1)
        k += 1
        a = 2
        return a

    elif h == 0:
        mark_on_field_2(k, (h + 1), 1)
        h += 1
        a = 3
        return a

    elif k == len(board[0]) - 1 and h == len(board[0]) - 1:
        mark_on_field_2(k, (h - 1), 1)
        mark_on_field_2((k - 1), (h - 1), 1)
        k -= 1
        h -= 1
        a = 4
        return a

    elif k == len(board[0]) - 1:
        mark_on_field_2((k - 1), h, 1)
        k -= 1
        a = 5
        return a

    elif h == len(board[0]) - 1:
        mark_on_field_2(k, (h - 1), 1)
        h -= 1
        a = 6
        return a

def way():
    global counter
    global coord

    k1 = x1
    h1 = y1

    k2 = x2
    h2 = y2

    a = check_edge(k1, h1)
    if a == 1:
        k1 += 1
        h1 += 1
    elif a == 2:
        k1 += 1
    elif a == 3:
        h1 += 1
    elif a == 4:
        k1 -= 1
        h1 -= 1
    elif a == 5:
        k1 -= 1
    elif a == 6:
        h1 -= 1

    a = check_edge(k2, h2)
    if a == 1:
        k2 += 1
        h2 += 1
    elif a == 2:
        k2 += 1
    elif a == 3:
        h2 += 1
    elif a == 4:
        k2 -= 1
        h2 -= 1
    elif a == 5:
        k2 -= 1
    elif a == 6:
        h2 -= 1



    if h2 > h1 and k2 > k1:
        counter += 1
        a = random.randint(1, 2)
        if a == 1:
            print_way_right(k1, h1, k2, h2, 1)
            h1 = h2
            print_way_down(k1, h1, k2, h2, 0)
            return
        else:
            print_way_down(k1, h1, k2, h2, 1)
            k1 = k2
            print_way_right(k1, h1, k2, h2, 0)
            return

    elif h2 > h1 and k2 < k1:
        counter += 1
        a = random.randint(1, 2)
        if a == 1:
            print_way_right(k1, h1, k2, h2, 1)
            h1 = h2
            print_way_up(k1, h1, k2, h2, 0)
            return
        else:
            print_way_up(k1, h1, k2, h2, 1)
            k1 = k2
            print_way_right(k1, h1, k2, h2, 0)
            return

    elif h2 < h1 and k2 > k1:
        counter += 1
        a = random.randint(1, 2)
        if a == 1:
            print_way_left(k1, h1, k2, h2, 1)
            h1 = h2
            print_way_down(k1, h1, k2, h2, 0)
            return
        else:
            print_way_down(k1, h1, k2, h2, 1)
            k1 = k2
            print_way_left(k1, h1, k2, h2, 0)
            return

    elif h2 < h1 and k2 < k1:
        counter += 1
        a = random.randint(1, 2)
        if a == 1:
            print_way_left(k1, h1, k2, h2, 1)
            h1 = h2
            print_way_up(k1, h1, k2, h2, 0)
            return
        else:
            print_way_up(k1, h1, k2, h2, 1)
            k1 = k2
            print_way_left(k1, h1, k2, h2, 0)
            return

    elif h1 == h2 and k2 > k1:
        print_way_down(k1, h1, k2, h2, 0)
        return

    elif h1 == h2 and k2 < k1:
        print_way_up(k1, h1, k2, h2, 0)
        return

    elif k1 == k2 and h2 > h1:
        print_way_right(k1, h1, k2, h2, 0)
        return

    elif k1 == k2 and h2 < h1:
        print_way_left(k1, h1, k2, h2, 0)
        return

    else:
        return

def get_random_points():
    global coord
    global counter
    global board
    level = get_level()

    while counter != level:

        a = random.randint(0, (len(coord)-1))

        h1 = coord[a][0]
        k1 = coord[a][1]
        del coord[a]
        print_field()
        print(h1, k1)

        b = check_points(k1, h1)
        if b == 1:
            print("подходит")


            if board[k1 - 1][h1 - 1] != 1 and board[k1 + 1][h1 + 1] != 1 and board[k1 + 1][h1 - 1] != 1 and board[k1 - 1][h1 + 1] != 1:
                counter += 1
                if board[k1][h1 + 1] > 0:
                    get_random_turn(k1, h1, 5, 6)
                    print(counter)

                elif board[k1][h1 - 1] > 0:
                    get_random_turn(k1, h1, 5, 6)
                    print(counter)

                else:
                    get_random_turn(k1, h1, 1, 2)
                    print(counter)
        else:
            print("не подошла")

def get_random_turn(k1, h1, frame1, frame2):

    a = random.randint(frame1, frame2)

    if a == 1:
        go_left(k1, h1, 1)

    if a == 2:
        go_right(k1, h1, 1)

    if a == 3:
        go_left(k1, h1, 0)

    if a == 4:
        go_right(k1, h1, 0)

    if a == 5:
        go_down(k1, h1, 1)

    if a == 6:
        go_up(k1, h1, 1)

    if a == 7:
        go_down(k1, h1, 0)

    if a == 8:
        go_up(k1, h1, 0)





    if a == 9:
        go_right(k1, h1, 1)

    if a == 10:
        go_right(k1, h1, 0)

    if a == 11:
        go_left(k1, h1, 1)

    if a == 12:
        go_left(k1, h1, 0)

    if a == 13:
        go_up(k1, h1, 1)

    if a == 14:
        go_up(k1, h1, 0)



    if a == 15:
        go_down(k1, h1, 1)

    if a == 16:
        go_down(k1, h1, 0)

    if a == 17:
        go_right(k1, h1, 1)

    if a == 18:
        go_right(k1, h1, 0)

    if a == 19:
        go_left(k1, h1, 1)

    if a == 20:
        go_left(k1, h1, 0)




if __name__ == '__main__':

    board = create_board()

    counter = 0
    counter_ = 0
    checker = 0


    x1, y1 = get_start()
    x2, y2 = get_finish()

    way()
    del_coord(counter_)
    print(coord)
    get_random_points()
    print_field()
    print(coord)
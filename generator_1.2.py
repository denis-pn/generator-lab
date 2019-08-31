
X = 1

import random

def get_SIZE():
    SIZE = int(input("Введите размер лабиринта: "))
    return SIZE

def create_board():
    global SIZE
    return [[0 for j in range(SIZE)] for i in range(SIZE)]

def print_field():
    global board
    for row in board:
        for col in row:
            print(col, end="  ")
        print()

def go_left():
    global x1, y1
    if y1 - 3 < len(board[0]) and y1 - 3 >= 0 and board[x1][y1 - 1] < 2 and board[x1][y1 - 2] < 2 and board[x1][y1 - 3] < 2:
        mark_on_field_1(x1, y1 - 1, X)
        mark_on_field_1(x1, y1 - 2, X)
        mark_on_field_1(x1, y1 - 3, X)
        y1 = y1 - 3

    elif y1 - 2 < len(board[0]) and y1 - 2 >= 0 and board[x1][y1 - 1] < 2 and board[x1][y1 - 2] < 2:
        mark_on_field_1(x1, y1 - 1, X)
        mark_on_field_1(x1, y1 - 2, X)
        y1 = y1 - 2

    elif y1 - 1 < len(board[0]) and y1 - 1 >= 0 and board[x1][y1 - 1] < 2:
        mark_on_field_1(x1, y1 - 1, X)
        y1 = y1 - 1

    else:
        y1 = y1

def go_left_back():
    global x1, y1
    if y1 - 3 < len(board[0]) and y1 - 3 >= 0 and board[x1][y1 - 1] < 2 and board[x1][y1 - 2] < 2 and board[x1][y1 - 3] < 2:
        mark_on_field_1(x1, y1 - 1, X)
        mark_on_field_1(x1, y1 - 2 ,X)
        mark_on_field_1(x1, y1 - 3, X)

    elif y1 - 2 < len(board[0]) and y1 - 2 >= 0 and board[x1][y1 - 1] < 2 and board[x1][y1 - 2] < 2:
        mark_on_field_1(x1, y1 - 1, X)
        mark_on_field_1(x1, y1 - 2 ,X)

    elif y1 - 1 < len(board[0]) and y1 - 1 >= 0 and board[x1][y1 - 1] < 2:
        mark_on_field_1(x1, y1 - 1, X)

    else:
        y1 = y1

def go_right():
    global x1, y1
    if y1 + 3 < len(board[0]) and y1 + 3 >= 0 and board[x1][y1+ 1] < 2 and board[x1][y1 + 2] < 2 and board[x1][y1 + 3] < 2:
        mark_on_field_1(x1, y1 + 1, X)
        mark_on_field_1(x1, y1 + 2 ,X)
        mark_on_field_1(x1, y1 + 3, X)
        y1 = y1 + 3

    elif y1 + 2 < len(board[0]) and y1 + 2 >= 0 and board[x1][y1 + 1] < 2 and board[x1][y1 + 2] < 2:
        mark_on_field_1(x1, y1 + 1, X)
        mark_on_field_1(x1, y1 + 2 ,X)
        y1 = y1 + 2

    elif y1 + 1 < len(board[0]) and y1 + 1 >= 0 and board[x1][y1 + 1] < 2:
        mark_on_field_1(x1, y1 + 1, X)
        y1 = y1 + 1

    else:
        return


def go_right_back():
    global x1, y1
    if y1 + 3 < len(board[0]) and y1 + 3 >= 0 and board[x1][y1+ 1] < 2 and board[x1][y1 + 2] < 2 and board[x1][y1 + 3] < 2:
        mark_on_field_1(x1, y1 + 1, X)
        mark_on_field_1(x1, y1 + 2 ,X)
        mark_on_field_1(x1, y1 + 3, X)

    elif y1 + 2 < len(board[0]) and y1 + 2 >= 0 and board[x1][y1 + 1] < 2 and board[x1][y1 + 2] < 2:
        mark_on_field_1(x1, y1 + 1, X)
        mark_on_field_1(x1, y1 + 2 ,X)

    elif y1 + 1 < len(board[0]) and y1 + 1 >= 0 and board[x1][y1 + 1] < 2:
        mark_on_field_1(x1, y1 + 1, X)

    else:
        return

def go_down():
    global x1, y1
    if x1 + 3 < len(board) and x1 + 3 >= 0 and board[x1 + 1][y1] < 2 and board[x1 + 2][y1] < 2 and board[x1 + 3][y1] < 2:
        mark_on_field_1(x1 + 1,y1, X)
        mark_on_field_1(x1 + 2,y1, X)
        mark_on_field_1(x1 + 3,y1, X)
        x1 = x1 + 3

    elif x1 + 2 < len(board) and x1 + 2 >= 0 and board[x1 + 1][y1] < 2 and board[x1 + 2][y1] < 2:
        mark_on_field_1(x1 + 1,y1, X)
        mark_on_field_1(x1 + 2,y1, X)
        x1 = x1 + 2

    elif x1 + 1 < len(board) and x1 + 1 >= 0 and board[x1 + 1][y1] < 2:
        mark_on_field_1(x1 + 1,y1, X)
        x1 = x1 + 1

    else:
        return


def go_down_back():
    global x1, y1
    if x1 + 3 < len(board) and x1 + 3 >= 0 and board[x1 + 1][y1] < 2 and board[x1 + 2][y1] < 2 and board[x1 + 3][y1] < 2:
        mark_on_field_1(x1 + 1,y1, X)
        mark_on_field_1(x1 + 2,y1, X)
        mark_on_field_1(x1 + 3,y1, X)

    elif x1 + 2 < len(board) and x1 + 2 >= 0 and board[x1 + 1][y1] < 2 and board[x1 + 2][y1] < 2:
        mark_on_field_1(x1 + 1,y1, X)
        mark_on_field_1(x1 + 2,y1, X)

    elif x1 + 1 < len(board) and x1 + 1 >= 0 and board[x1 + 1][y1] < 2:
        mark_on_field_1(x1 + 1,y1, X)

    else:
        return

def go_up():
    global x1, y1
    if x1 - 3 < len(board) and x1 - 3 >= 0 and board[x1 - 1][y1] < 2 and board[x1 - 2][y1] < 2 and board[x1 - 3][y1] < 2:
        mark_on_field_1(x1 - 1,y1, X)
        mark_on_field_1(x1 - 2,y1, X)
        mark_on_field_1(x1 - 3,y1, X)
        x1 = x1 - 3

    elif x1 - 2 < len(board) and x1 - 2 >= 0 and board[x1 - 1][y1] < 2 and board[x1 - 2][y1] < 2:
        mark_on_field_1(x1 - 1,y1, X)
        mark_on_field_1(x1 - 2,y1, X)
        x1 = x1 - 2

    elif x1 - 1 < len(board) and x1 - 1 >= 0 and board[x1 - 1][y1] < 2:
        mark_on_field_1(x1 - 1,y1, X)
        x1 = x1 - 1

    else:
        return


def go_up_back():
    global x1, y1
    if x1 - 3 < len(board) and x1 - 3 >= 0 and board[x1 - 1][y1] < 2 and board[x1 - 2][y1] < 2 and board[x1 - 3][y1] < 2:
        mark_on_field_1(x1 - 1,y1, X)
        mark_on_field_1(x1 - 2,y1, X)
        mark_on_field_1(x1 - 3,y1, X)

    elif x1 - 2 < len(board) and x1 - 2 >= 0 and board[x1 - 1][y1] < 2 and board[x1 - 2][y1] < 2:
        mark_on_field_1(x1 - 1,y1, X)
        mark_on_field_1(x1 - 2,y1, X)

    elif x1 - 1 < len(board) and x1 - 1 >= 0 and board[x1 - 1][y1] < 2:
        mark_on_field_1(x1 - 1,y1, X)

    else:
        return


def finish():
    global board
    global x1, y1
    board[x1][y1] = 6


def get_points():
    global board
    y1 = random.randint(1, (SIZE-2))
    x1 = random.randint(1, (SIZE-2))
    mark_on_field_1(x1, y1, 2)
    return x1, y1



def mark_on_field_1(x, y, symbol):
    board[x][y] = symbol

def get_level():
    lev = int(input("Введите уровень сложности: "))
    return lev


def get_random():
    lev = get_level()
    k = 0

    while k != lev:
        a = random.randint(0, 7)
        print(f"a =  {a}")

        if a == 0:
            go_left()
            k += 1

            if k != lev:
                b = random.randint(0, 6)
                print(b)
                if b == 0:
                    go_left_back()
                    k += 1

                elif b == 1:
                    go_right()
                    k += 1

                elif b == 2:
                    go_right_back()
                    k += 1

                elif b == 3:
                    go_down()
                    k += 1

                elif b == 4:
                    go_down_back()
                    k += 1

                elif b == 5:
                    go_up()
                    k += 1

                elif b == 6:
                    go_up_back()
                    k += 1

                else:
                    return

        if a == 1:
            go_left_back()
            k += 1

            if k != lev:
                b = random.randint(0, 6)
                print(b)
                if b == 0:
                    go_left()
                    k += 1

                elif b == 1:
                    go_right()
                    k += 1

                elif b == 2:
                    go_right_back()
                    k += 1

                elif b == 3:
                    go_down()
                    k += 1

                elif b == 4:
                    go_down_back()
                    k += 1

                elif b == 5:
                    go_up()
                    k += 1

                elif b == 6:
                    go_up_back()
                    k += 1

                else:
                    return

        if a == 2:
            go_right()
            k += 1

            if k != lev:
                b = random.randint(0, 6)
                print(b)
                if b == 0:
                    go_left()
                    k += 1

                elif b == 1:
                    go_left_back()
                    k += 1

                elif b == 2:
                    go_right_back()
                    k += 1

                elif b == 3:
                    go_down()
                    k += 1

                elif b == 4:
                    go_down_back()
                    k += 1

                elif b == 5:
                    go_up()
                    k += 1

                elif b == 6:
                    go_up_back()
                    k += 1

                else:
                    return

        if a == 3:
            go_right_back()
            k += 1

            if k != lev:
                b = random.randint(0, 6)
                print(b)
                if b == 0:
                    go_left()
                    k += 1

                elif b == 1:
                    go_left_back()
                    k += 1

                elif b == 2:
                    go_right()
                    k += 1

                elif b == 3:
                    go_down()
                    k += 1

                elif b == 4:
                    go_down_back()
                    k += 1

                elif b == 5:
                    go_up()
                    k += 1

                elif b == 6:
                    go_up_back()
                    k += 1

                else:
                    return

        if a == 4:
            go_down()
            k += 1

            if k != lev:
                b = random.randint(0, 6)
                print(b)
                if b == 0:
                    go_left()
                    k += 1

                elif b == 1:
                    go_left_back()
                    k += 1

                elif b == 2:
                    go_right()
                    k += 1

                elif b == 3:
                    go_right_back()
                    k += 1

                elif b == 4:
                    go_down_back()
                    k += 1

                elif b == 5:
                    go_up()
                    k += 1

                elif b == 6:
                    go_up_back()
                    k += 1

                else:
                    return

        if a == 5:
            go_down_back()
            k += 1

            if k != lev:
                b = random.randint(0, 6)
                print(b)
                if b == 0:
                    go_left()
                    k += 1

                elif b == 1:
                    go_left_back()
                    k += 1

                elif b == 2:
                    go_right()
                    k += 1

                elif b == 3:
                    go_right_back()
                    k += 1

                elif b == 4:
                    go_down()
                    k += 1

                elif b == 5:
                    go_up()
                    k += 1

                elif b == 6:
                    go_up_back()
                    k += 1

                else:
                    return

        if a == 6:
            go_up()
            k += 1

            if k != lev:
                b = random.randint(0, 6)
                print(b)
                if b == 0:
                    go_left()
                    k += 1

                elif b == 1:
                    go_left_back()
                    k += 1

                elif b == 2:
                    go_right()
                    k += 1

                elif b == 3:
                    go_right_back()
                    k += 1

                elif b == 4:
                    go_down()
                    k += 1

                elif b == 5:
                    go_down_back()
                    k += 1

                elif b == 6:
                    go_up_back()
                    k += 1

                else:
                    return

        if a == 7:
            go_up_back()
            k += 1

            if k != lev:
                b = random.randint(0, 6)
                print(b)
                if b == 0:
                    go_left()
                    k += 1

                elif b == 1:
                    go_left_back()
                    k += 1

                elif b == 2:
                    go_right()
                    k += 1

                elif b == 3:
                    go_right_back()
                    k += 1

                elif b == 4:
                    go_down()
                    k += 1

                elif b == 5:
                    go_down_back()
                    k += 1

                elif b == 6:
                    go_up()
                    k += 1

                else:
                    return



    finish()




if __name__ == '__main__':

    SIZE = get_SIZE()
    board = create_board()

    x1, y1 = get_points()


    get_random()
    print_field()

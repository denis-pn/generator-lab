import random

import numpy as np
from PIL import Image



def get_SIZE():
    # SIZE = int(input("Введите размер лабиринта: "))
    SIZE = 100
    return SIZE

def get_x_and_y(SIZE):
    while True:
        y = (int(input("Введите x координату: ")))
        x = (int(input("Введите y координату: ")))

        if y >= 0 and y <= (SIZE) and x >= 0 and x <= (SIZE):
            return x, y
        else:
            print("Вы вышли за приделы поля, введите заново")

def get_start_and_finish():

    SIZE = get_SIZE()

    SIZE_start_finish = []
    SIZE_start_finish.append((SIZE))

    print("Введите координаты точки старта:")


    # x, y = get_x_and_y(SIZE)
    x = 1
    y = 1


    i = 0
    while i != 1:
        if x == 0 or y == 0 or x == SIZE + 1 or y == SIZE + 1:
            print("Координата не может равнятся 0 или быть больше размера лабиринта повторите попытку")
            x, y = get_x_and_y(SIZE)

        else:
            SIZE_start_finish.append((y, x))
            i = 1


    print("Введите координаты точки финиша:")
    # x, y = get_x_and_y(SIZE)
    x = 100
    y = 100


    i = 0
    while i != 1:
        if x == 0 or y == 0 or x == SIZE + 1 or y == SIZE + 1:
            print("Координата не может равнятся 0 или быть больше размера лабиринта повторите попытку")
            x, y = get_x_and_y(SIZE)

        else:
            SIZE_start_finish.append((y, x))
            i = 1

    return SIZE_start_finish

def create_board():
    SIZE = SIZE_start_finish[0]
    return [[0 for j in range(SIZE + 2)] for i in range(SIZE + 2)]

def print_field():
    global board
    for row in board:
        for col in row:
            print(col, end="  ")
        print()

def mark_on_field_1(x, y, symbol):
    board[x][y] = symbol



def print_way_right(k1, h1, k2, h2):
    while True:
        if h2 != h1 and board[k1][h1+1] < 2:
            h1 += 1
            mark_on_field_1(k1, h1, 1)
            coord.append((k1, h1))
        else:
            return coord

def print_way_left(k1, h1, k2, h2):

    while True:
        if h2 != h1  and board[k1][h1-1] < 2:
            h1 -= 1
            mark_on_field_1(k1, h1, 1)
            coord.append((k1, h1))
        else:
            return coord

def print_way_down(k1, h1, k2, h2):
    while True:
        if k2 != k1 and board[k1 + 1][h1] < 2:
            k1 += 1
            mark_on_field_1(k1, h1, 1)
            coord.append((k1, h1))
        else:
            return coord

def print_way_up(k1, h1, k2, h2):
    while True:
        if k2 != k1 and board[k1-1][h1] < 2:
            k1 -= 1
            mark_on_field_1(k1, h1, 1)
            coord.append((k1, h1))
        else:
            return coord



def way():
    global counter
    turns = []
    coord = []

    k1 = SIZE_start_finish[1][1]
    h1 = SIZE_start_finish[1][0]
    mark_on_field_1(k1, h1, 2)

    k2 = SIZE_start_finish[2][1]
    h2 = SIZE_start_finish[2][0]
    mark_on_field_1(k2, h2, 6)


    if h2 > h1 and k2 > k1:
        a = random.randint(1, 8)
        if a == 1:
            # counter += 1
            coord = print_way_right(k1, h1, k2, h2)
            h1 = h2
            turns.append((k1, h1))
            coord = print_way_down(k1, h1, k2, h2)
            return turns
        elif a == 2:
            # counter += 1
            coord = print_way_down(k1, h1, k2, h2)
            k1 = k2
            turns.append((k1, h1))
            coord = print_way_right(k1, h1, k2, h2)
            return turns

        elif a == 3 or a == 5 or a == 7:
            # counter += 3
            IH = (h2 - h1) // 2
            IK = (k2 - k1) // 2

            coord = print_way_right(k1, h1, k2, h2 - IH)

            h1 = h2 - IH
            turns.append((k1, h1))
            coord = print_way_down(k1, h1, k2 - IK,  h2)

            k1 = k2 - IK
            turns.append((k1, h1))
            coord = print_way_right(k1, h1, k2, h2)

            h1 = h2
            turns.append((k1, h1))
            coord = print_way_down(k1, h1, k2, h2)
            return turns
        elif a == 4 or a == 6 or a == 8:
            # counter += 3
            IH = (h2 - h1) // 2
            IK = (k2 - k1) // 2

            coord = print_way_down(k1, h1, k2 - IK, h2)

            k1 = k2 - IK
            turns.append((k1, h1))
            coord = print_way_right(k1, h1, k2,  h2 - IH)

            h1 = h2 - IH
            turns.append((k1, h1))
            coord = print_way_down(k1, h1, k2, h2)

            k1 = k2
            turns.append((k1, h1))
            coord = print_way_right(k1, h1, k2, h2)
            return turns

    elif h2 > h1 and k2 < k1:
        a = random.randint(1, 8)
        if a == 1:
            # counter += 1
            coord = print_way_right(k1, h1, k2, h2)
            h1 = h2
            turns.append((k1, h1))
            coord = print_way_up(k1, h1, k2, h2)
            return turns
        elif a == 2:
            # counter += 1
            coord = print_way_up(k1, h1, k2, h2)
            k1 = k2
            turns.append((k1, h1))
            coord = print_way_right(k1, h1, k2, h2)
            return turns
        elif a == 3  or a == 5 or a == 7:
            # counter += 3
            IH = (h2 - h1) // 2
            IK = (k1 - k2) // 2

            coord = print_way_right(k1, h1, k2, h2 - IH)

            h1 = h2 - IH
            turns.append((k1, h1))
            coord = print_way_up(k1, h1, k2 + IK,  h2)

            k1 = k2 + IK
            turns.append((k1, h1))
            coord = print_way_right(k1, h1, k2, h2)

            h1 = h2
            turns.append((k1, h1))
            coord = print_way_up(k1, h1, k2, h2)
            return turns
        elif a == 4  or a == 6 or a == 8:
            # counter += 3
            IH = (h2 - h1) // 2
            IK = (k1 - k2) // 2

            coord = print_way_up(k1, h1, k2 + IK, h2)

            k1 = k2 + IK
            turns.append((k1, h1))
            coord = print_way_right(k1, h1, k2,  h2 - IH)

            h1 = h2 - IH
            turns.append((k1, h1))
            coord = print_way_up(k1, h1, k2, h2)

            k1 = k2
            turns.append((k1, h1))
            coord = print_way_right(k1, h1, k2, h2)
            return turns

    elif h2 < h1 and k2 > k1:
        a = random.randint(1, 8)
        if a == 1:
            # counter += 1
            coord = print_way_left(k1, h1, k2, h2)
            h1 = h2
            coord = print_way_down(k1, h1, k2, h2)
            return turns
        elif a == 2:
            # counter += 1
            coord = print_way_down(k1, h1, k2, h2)
            k1 = k2
            coord = print_way_left(k1, h1, k2, h2)
            return turns
        elif a == 3  or a == 5 or a == 7:
            # counter += 3
            IH = (h1 - h2) // 2
            IK = (k2 - k1) // 2

            coord = print_way_left(k1, h1, k2, h2 + IH)

            h1 = h2 + IH
            turns.append((k1, h1))
            coord = print_way_down(k1, h1, k2 - IK,  h2)

            k1 = k2 - IK
            turns.append((k1, h1))
            coord = print_way_left(k1, h1, k2, h2)

            h1 = h2
            turns.append((k1, h1))
            coord = print_way_down(k1, h1, k2, h2)
            return turns
        elif a == 4  or a == 6 or a == 8:
            # counter += 3
            IH = (h1 - h2) // 2
            IK = (k2 - k1) // 2

            coord = print_way_down(k1, h1, k2 - IK, h2)

            k1 = k2 - IK
            turns.append((k1, h1))
            coord = print_way_left(k1, h1, k2,  h2 + IH)

            h1 = h2 + IH
            turns.append((k1, h1))
            coord = print_way_down(k1, h1, k2, h2)

            k1 = k2
            turns.append((k1, h1))
            coord = print_way_left(k1, h1, k2, h2)
            return turns

    elif h2 < h1 and k2 < k1:
        a = random.randint(1, 8)
        if a == 1:
            # counter += 1
            coord = print_way_left(k1, h1, k2, h2)
            h1 = h2
            coord = print_way_up(k1, h1, k2, h2)
            return turns
        elif a == 2:
            # counter += 1
            coord = print_way_up(k1, h1, k2, h2)
            k1 = k2
            coord = print_way_left(k1, h1, k2, h2)
            return turns
        elif a == 3 or a == 5 or a == 7:
            # counter += 3
            IH = (h1 - h2) // 2
            IK = (k1 - k2) // 2

            coord = print_way_left(k1, h1, k2, h2 + IH)

            h1 = h2 + IH
            turns.append((k1, h1))
            coord = print_way_up(k1, h1, k2 + IK,  h2)

            k1 = k2 + IK
            turns.append((k1, h1))
            coord = print_way_left(k1, h1, k2, h2)

            h1 = h2
            turns.append((k1, h1))
            coord = print_way_up(k1, h1, k2, h2)
            return turns
        elif a == 4 or a == 6 or a == 8:
            # counter += 3
            IH = (h1 - h2) // 2
            IK = (k1 - k2) // 2

            coord = print_way_up(k1, h1, k2 + IK, h2)

            k1 = k2 + IK
            turns.append((k1, h1))
            coord = print_way_left(k1, h1, k2,  h2 + IH)

            h1 = h2 + IH
            turns.append((k1, h1))
            coord = print_way_up(k1, h1, k2, h2)

            k1 = k2
            turns.append((k1, h1))
            coord = print_way_left(k1, h1, k2, h2)
            return turns


    elif h1 == h2 and k2 > k1:
        coord = print_way_down(k1, h1, k2, h2)
        return coord

    elif h1 == h2 and k2 < k1:
        coord = print_way_up(k1, h1, k2, h2,)
        return coord

    elif k1 == k2 and h2 > h1:
        coord = print_way_right(k1, h1, k2, h2)
        return coord

    elif k1 == k2 and h2 < h1:
        coord = print_way_left(k1, h1, k2, h2)
        return coord

    else:
        return

def get_level():
    level = 0

    if len(coord) != 0:
        while True:
            level = int(input("Введите колличество усложнений лабиринта: "))
            if level > (len(coord)):
                print("Колличество ошибок не подходит под выбранные вами точки старта и финиша, введите сложность меньше ")

            else:
                return level
    else:
        print(coord)
        print("Для автоматической генерации маленькое расстояние между точками старта и финиша")
        exit(0)


def get_random_points():
    points = []
    # level = get_level()
    level = 50
    i = 0

    # coord.pop(len(coord) - 1)

    if len(turns) > 2:

         if level == 1:
             pnt = turns[1]
             points.append(turns[1])
             turns_list = check_turns(pnt)
             get_random_turn(pnt, turns_list)
             i += 1

         elif level == 2:
             a = random.randint(1, 2)
             if a == 1:
                pnt = turns[0]
                points.append(turns[0])
                turns_list = check_turns(pnt)
                get_random_turn(pnt, turns_list)
                pnt = turns[1]
                points.append(turns[1])
                turns_list = check_turns(pnt)
                get_random_turn(pnt, turns_list)
                i += 2
             else:
                 pnt = turns[1]
                 points.append(turns[1])
                 turns_list = check_turns(pnt)
                 get_random_turn(pnt, turns_list)
                 pnt = turns[2]
                 points.append(turns[2])
                 turns_list = check_turns(pnt)
                 get_random_turn(pnt, turns_list)
                 i += 2

         else:
            pnt = turns[0]
            points.append(turns[0])
            turns_list = check_turns(pnt)
            get_random_turn(pnt, turns_list)
            pnt = turns[1]
            points.append(turns[1])
            turns_list = check_turns(pnt)
            get_random_turn(pnt, turns_list)
            pnt = turns[2]
            points.append(turns[2])
            turns_list = check_turns(pnt)
            get_random_turn(pnt, turns_list)
            i += 3


    if i < level:
        while i != level + 1:
            if len(coord) != 0:
                a = len(coord)
                i += 1
                q = random.randint(0, len(coord) - 1)

                points_check = coord[q]

                check_point = check_points(points_check, points)

                if check_point == 1:
                    pnt = coord[q]
                    points.append(coord[q])
                    turns_list = check_turns(pnt)
                    get_random_turn(pnt, turns_list)
                    coord.pop(q)
                else:
                    i -= 1
                    coord.pop(q)
            else:
                return points

    # i = 0
    # while i != level // 3:
    #     if len(coord) != 0:
    #         q = random.randint(0, len(coord) - 1)
    #         k1 = coord[q][0]
    #         h1 = coord[q][1]
    #         mark_on_field_2(k1, h1, 0)
    #         i += 1
    # i += 1

    return points

def check_points(points_check, points):
    k1 = points_check[0]
    h1 = points_check[1]

    ch = 0
    while ch != len(points):

        if points_check != points[ch]:
            ch += 1

        else:
            check_point = 0
            return check_point


    if board[k1 - 1][h1 - 1] != 1 and board[k1 + 1][h1 + 1] != 1 and board[k1 + 1][h1 - 1] != 1 and board[k1 - 1][h1 + 1] != 1:
        check_point = 1
        return check_point

    else:
        check_point = 0
        return check_point

def check_turns(pnt):

    k1 = pnt[0]
    h1 = pnt[1]
    turns_list = []

    if board[k1 - 1][h1] == 0 and k1 - 2 > 0:
        turns_list.append(4)
    if board[k1 + 1][h1] == 0 and k1 + 2 < len(board[0]):
        turns_list.append(3)
    if board[k1][h1 - 1] == 0 and h1 - 2 > 0:
        turns_list.append(1)
    if board[k1][h1 + 1] == 0 and h1 + 2 < len(board[0]):
        turns_list.append(2)

    return turns_list

def get_random_turn(pnt, turns_list):

    k1 = pnt[0]
    h1 = pnt[1]

    if len(turns_list) > 0:
        a = random.choice(turns_list)

        if a == 1:
            go_left(k1, h1)

        if a == 2:
            go_right(k1, h1)

        if a == 3:
            go_down(k1, h1)

        if a == 4:
            go_up(k1, h1)



def go_left(k1, h1):
    # print("лево")
    SIZE = SIZE_start_finish[0]
    step = SIZE // 3
    un_step = 0


    while step != 0:

        if h1 - step > 0 and board[k1][h1 - step] < 2:
            if (board[k1 + 1][h1 - step] == 1 and board[k1 + 1][h1 - step + 1] == 1) or (board[k1 - 1][h1 - step] == 1 and board[k1 - 1][h1 - step + 1] == 1):
                un_step += 1
            else:
                mark_on_field_1(k1, h1 - step, 1)

        else:
            un_step += 1

        step -= 1

    # print_field()
    repeat = random.randint(1, 3)

    # print(un_step)
    step = SIZE // 3
    # print(step)

    if repeat == 1 or repeat == 2:
        pnt_ = []
        pnt_.append(k1)
        pnt_.append(h1 - step + un_step)
        turns_list = check_turns(pnt_)
        # print(turns_list)
        get_random_turn(pnt_, turns_list)

def go_right(k1, h1):
    # print("право")
    SIZE = SIZE_start_finish[0]
    step = SIZE // 3
    un_step = 0

    while step != 0:

        if h1 + step < len(board) - 1 and board[k1][h1 + step] < 2 :
            if (board[k1 + 1][h1 + step] == 1 and board[k1 + 1][h1 + step - 1] == 1) or  (board[k1 - 1][h1 + step] == 1 and board[k1 - 1][h1 + step - 1] == 1):
                    un_step += 1

            else:
                mark_on_field_1(k1, h1 + step, 1)
        else:
            un_step += 1

        step -= 1
    #
    # print_field()

    repeat = random.randint(1, 3)
    step = SIZE // 3
    if repeat == 1 or repeat == 2:
        pnt_ = []
        # print("повтор")
        pnt_.append(k1)
        pnt_.append(h1 + step - un_step)
        turns_list = check_turns(pnt_)
        # print(turns_list)
        get_random_turn(pnt_, turns_list)

def go_down(k1, h1):
    # print("вниз")
    SIZE = SIZE_start_finish[0]
    step = SIZE // 3
    un_step = 0

    while step != 0:

        if k1 + step < len(board) - 1 and board[k1 + step][h1] < 2:
            if (board[k1 + step][h1 + 1] == 1 and board[k1 + step - 1][h1 + 1] == 1) or (board[k1 + step][h1 - 1] == 1 and board[k1 + step - 1][h1 - 1] == 1):
                    un_step += 1
            else:
                mark_on_field_1(k1 + step, h1, 1)
        else:
            un_step += 1
        step -= 1

    # print_field()

    repeat = random.randint(1, 3)
    pnt_ = []
    step = SIZE // 3
    # print("повтор")
    if repeat == 1 or repeat == 2:
        pnt_.append(k1 + step - un_step)
        pnt_.append(h1)
        turns_list = check_turns(pnt_)
        # print(turns_list)
        get_random_turn(pnt_, turns_list)

def go_up(k1, h1):
    # print("вверх")
    SIZE = SIZE_start_finish[0]
    step = SIZE // 3
    un_step = 0

    while step != 0:

        if k1 - step > 0 and board[k1 - step][h1] < 2:
            if (board[k1 - step][h1 + 1] == 1 and board[k1 - step + 1][h1 + 1] == 1) or (board[k1 - step][h1 - 1] == 1 and board[k1 - step + 1][h1 - 1] == 1):
                    un_step += 1
            else:
                mark_on_field_1(k1 - step, h1, 1)
        else:
            un_step += 1
        step -= 1


    repeat = random.randint(1, 3)
    pnt_ = []
    step = SIZE // 3
    # print("повтор")
    if repeat == 1 or repeat == 2:
        pnt_.append(k1 - step + un_step)
        pnt_.append(h1)
        turns_list = check_turns(pnt_)
        # print(turns_list)
        get_random_turn(pnt_, turns_list)



def board_in_numpy():

    SIZE = len(board)
    board_1 = [[0 for j in range(SIZE)] for i in range(SIZE)]
    # print(len(board))
    # print(len(board_1))

    i = 0
    i_1 = 0
    while i != len(board):

        while i_1 != len(board):
            if board[i][i_1] == 0:
                board_1[i][i_1]  = [255, 255, 255, 255]

            elif board[i][i_1] == 1:
                board_1[i][i_1] = [0, 0, 0, 255]

            elif board[i][i_1] == 2:
                board_1[i][i_1] = [245, 225, 7, 255]

            elif board[i][i_1] == 6:
                board_1[i][i_1] = [250, 5, 46, 255]

            i_1 += 1

        i += 1
        i_1 = 0

    arr = np.array(board_1)
    print(arr)
    img2 = Image.fromarray(arr, 'RGBA')
    img2.show()









if __name__ == '__main__':

    coord = []
    SIZE_start_finish = get_start_and_finish()

    board = create_board()

    turns = way()

    points = get_random_points()

    # print_field()
    # print(board)
    board_in_numpy()

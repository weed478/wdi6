#       0  1  2  3  4  5  6  7
# T = [[0, 0, 0, 0, 0, 0, 0, K],  0
#      [0, 0, 0, 0, 0, 0, 0, 0],  1
#      [0, 0, 0, 0, 0, 0, 0, 0],  2
#      [0, 0, 0, 0, 0, 0, 0, 0],  3
#      [0, 0, 0, 0, 0, 0, 0, 0],  4
#      [0, 0, 0, 0, 0, 0, 0, 0],  5
#      [0, 0, 0, 0, 0, 0, 0, 0],  6
#      [0, 0, 0, 0, 0, 0, 0, 0]]  7

import random

N = 8

T = [[random.randint(0, 99) for _ in range(N)] for _ in range(N)]


def find_route(T, pos=(N - 1, 0)):
    if pos[0] > N - 1 or pos[1] > N - 1:
        return None, None

    cost = T[pos[1]][pos[0]]

    l_pos = (pos[0] - 1, pos[1] + 1)
    left = find_route(T, l_pos)  # none

    d_pos = (pos[0], pos[1] + 1)
    down = find_route(T, d_pos)  # NOne

    r_pos = (pos[0] + 1, pos[1] + 1)
    right = find_route(T, r_pos)  # None

    element = None
    if right[0] is not None:
        if left[0] < down[0]:
            minn = left[0]
            element = left
        else:
            minn = down[0]
            element = down
        if right[0] < minn:
            element = right

    elif left[0] is not None:
        if down[0] < left[0]:
            minn = down[0]
            element = down
        else:
            minn = left[0]
            element = left

    else:
        tab = [pos]
        return cost, tab

    cost += element[0]
    tab = element[1]
    tab.append(pos)
    return cost, tab


route = find_route(T)
tab = route[1]

for row in range(N):
    print("[", end='')
    for col in range(N):
        if tab.__contains__((col, row)):
            print("\u001b[33m", T[row][col], "\u001b[0m", end='', sep='')
            print("\t", end='')
        else:
            print(T[row][col], end='', sep='')
            print("\t", end='')
    print("]")

print(route[0])
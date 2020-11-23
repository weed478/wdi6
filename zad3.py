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

T = [[random.randint(0, 10) for _ in range(8)] for _ in range(8)]

for row in range(8):
    print("[", end='')
    for col in range(8):
        print(T[row][col], end='')
        print("\t", end='')
    print("]")


def find_route(T, pos=(7, 0)):
    if pos[0] > 7 or pos[1] > 7:
        return None

    cost = T[pos[1]][pos[0]]

    l_pos = (pos[0] - 1, pos[1] + 1)
    left = find_route(T, l_pos)  # none

    d_pos = (pos[0], pos[1] + 1)
    down = find_route(T, d_pos)  # NOne

    r_pos = (pos[0] + 1, pos[1] + 1)
    right = find_route(T, r_pos)  # None

    if right is not None:
        cost += min(left, down, right)
    elif left is not None:
        cost += min(left, down)

    return cost


print(find_route(T))

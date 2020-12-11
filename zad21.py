from itertools import permutations
from meszstack import meszgen


def zad21(t, s):
    n = len(t)

    def next_i(i=None):
        if i is None:
            return 0
        elif i + 1 < n:
            return i + 1
        else:
            return None

    for x in meszgen(next_i):
        for y in permutations(i for i in range(n)):
            pos = []
            for o in range(len(x)):
                pos.append((x[o], y[o]))

            current_sum = 0

            for p in pos:

                current_sum += t[p[0]][p[1]]

            if current_sum == s:
                print(pos)
                return True

    return False


tab = [[0, 0, 1, 0],
       [0, 0, 0, 0],
       [0, 0, 1, 1],
       [2, 0, 0, 0]]

print(zad21(tab, 4))

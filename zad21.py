from meszstack import meszgen
from itertools import permutations


def zad21(t, s):
    n = len(t)

    def next_i(i=None):
        if i is None:
            return 0

        elif i + 1 < n:
            return i + 1

        else:
            return None

    for rows in meszgen(next_i):
        for cols in permutations(range(n), len(rows)):
            pos = [(r, c) for (r, c) in zip(rows, cols)]

            current_sum = 0
            for p in pos:
                current_sum += t[p[0]][p[1]]

            if current_sum == s:
                print(pos)
                return True

    return False


tab = [[1 for _ in range(4)] for _ in range(4)]
print(zad21(tab, 3))

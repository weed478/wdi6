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
        for y in permutations(range(n), len(x)):
            current_sum = 0
            for o in range(len(x)):
                current_sum += t[x[o]][y[o]]
            if current_sum == s:
                return True
    return False


tab = [[0, 0, 1, 0, 0, 3, 2, 1],
       [0, 0, 0, 0, 1, 1, 0, 0],
       [0, 0, 1, 1, 0, 1, 0, 0],
       [2, 0, 0, 0, 0, 1, 0, 0],
       [0, 0, 4, 0, 0, 0, 0, 0],
       [1, 0, 0, 0, 0, 1, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0],
       [1, 0, 0, 3, 0, 0, 1, 0]]

print(zad21(tab, 15))

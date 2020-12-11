from itertools import permutations
from meszstack import meszgen


def zad21(t, s):
    n = len(t)

    def next_i(i=None):
        if i is None:
            return 0
        elif i < n:
            return i + 1
        else:
            return None

    for x in meszgen(next_i):
        for y in permutations(i for i in range(n)):
            pos = []
            for o in range(len(x)):
                pos.append((x[o], y[o]))

            cols = set()
            rows = set()

            current_sum = 0

            for p in pos:
                if p[0] in rows:
                    break

                rows.add(p[0])

                if p[1] in cols:
                    break

                cols.add(p[1])

                current_sum += t[p[0]][p[1]]

            if current_sum == s:
                print(pos)
                return True

    return False


tab = [[0, 1, 0],
       [1, 0, 0],
       [0, 0, 1]]
print(zad21(tab, 3))

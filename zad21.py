from meszstack import meszgen


def zad21(t, s):
    n = len(t)

    def next_i(i=None):
        if i is None:
            return 0, 0

        elif i[1] + 1 < n:
            return i[0], i[1] + 1

        elif i[0] + 1 < n:
            return i[0] + 1, 0

        else:
            return None

    for pos in meszgen(next_i):
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

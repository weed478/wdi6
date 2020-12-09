from meszstack import meszgen


def zad21(t, s):
    n = len(t)

    def next_i(i=None):
        if i is None:
            return 0

        elif i + 1 < n*n:
            return i + 1

        else:
            return None

    for x in meszgen(next_i):
        print(list(map(lambda i: (i % n, i // n), x)))


tab = [[0, 1],
       [1, 0]]
zad21(tab, 2)

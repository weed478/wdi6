def gen_podzial(n, l):
    tab = [0 for _ in range(n)]

    while True:
        tab[0] += 1
        for i in range(0, n - 1):
            if tab[i] >= l:
                tab[i] = 0
                tab[i + 1] += 1
        if tab[n - 1] < l:
            yield tab
        else:
            break


def works(tab, podzial, k):
    s = ([0, 0], [0, 0])
    for i in range(len(tab)):
        if podzial[i] != 0:
            s[podzial[i] - 1][1] += 1
            s[podzial[i] - 1][0] += tab[i]
    # print(s)
    return s[0][0] == s[1][0] and s[0][1] + s[1][1] == k


def zad32(t, k):
    n = len(t)

    for podzial in gen_podzial(n, 3):
        # print(podzial)
        if works(t, podzial, k):
            return True

    return False


print(zad32([3, 4, 5, 3, 3, 1, 1, 3, 2, 1], 3))

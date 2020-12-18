def waga(num):
    w = 0

    while num > 1:
        f = 2
        while f <= num:
            if num % f == 0:
                while num % f == 0:
                    num //= f
                w += 1
            f += 1

    return w


def next(p):
    p[len(p) - 1] += 1
    for i in range(len(p) - 2, -1, -1):
        if p[i + 1] >= 3:
            p[i + 1] = 0
            p[i] += 1


def works(tab, podzial):
    s = [0, 0, 0]
    for i in range(len(tab)):
        s[podzial[i]] += tab[i]

    return s[0] == s[1] == s[2]


def zad2(tab):
    tab = [waga(n) for n in tab]
    podzial = [0 for _ in tab]

    while podzial[0] < 3:
        if works(tab, podzial):
            return True
        next(podzial)

    return False


from random import shuffle

data = [64, 6, 30, 1, 1, 2, 2, 2]
shuffle(data)

print(zad2(data))

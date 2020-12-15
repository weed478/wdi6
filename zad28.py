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


def waga(num):
    if num == 0:
        return 0
    i = 0
    while num > 0:
        num, rem = divmod(num, 2)
        if rem == 1:
            i += 1
    return i


# from zad2.py
def works(tab, podzial):
    s = [0, 0, 0]
    for i in range(len(tab)):
        s[podzial[i]] += tab[i]

    return s[0] == s[1] == s[2]


def zad28(tab):
    tab = [waga(num) for num in tab]
    for podzial in gen_podzial(len(tab), 3):
        #print(podzial)
        if works(tab, podzial):
            return True

    return False


print(zad28([2, 3, 5, 7, 15]))

from myszka import permutations


def zad23(tab, r, k):
    n = len(tab)

    for podzial in permutations(range(n), k):
        #print(podzial)
        serial = 0
        parallel = 0
        for e in podzial:
            e = tab[e]
            serial += e
            parallel += 1 / e
        if serial == r or parallel == r:
            #print(podzial)
            return True

    return False


tab = [2, 60, 1, 10, 5.4, 30, 7.5, 45, 9]
print(zad23(tab, 0.15, 3))

from myszka import combinations
from random import randint


def enki(t, target, n):
    count = 0
    for comb in combinations(t, n):
        t = 1
        for i in comb:
            t *= i

        if t == target:
            print(comb)
            count += 1

    return count


tab = [randint(0, 10) for _ in range(10)]
print(tab)
print(enki(tab, 6, 2))

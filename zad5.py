from math import log10
from random import randint


def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False

    div = 3
    while div * div <= n:
        if n % div == 0:
            return False
        div += 2
    return True


def bin_to_dec(num):
    a = 0
    i = 0
    while num > 0:
        num, rem = divmod(num, 10)
        a += rem * (2 ** i)
        i += 1
    return a


def split(tab, pos=0, num=0):
    # print(num)
    if not pos >= len(tab):
        a = split(tab, pos + 1, num * 10 + tab[pos])
        if a:
            return True
        b = False
        if is_prime(bin_to_dec(num)):
            b = split(tab, pos + 1, tab[pos])
        return b
    if log10(bin_to_dec(num) + 1) != len(tab):
        return is_prime(bin_to_dec(num))


T = [randint(0, 1) for _ in range(10)]
print(T)
print(split(T))

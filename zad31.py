from myszka import meszgen
from is_prime import prime_factors


def zad31(num):
    _factors = [i for i in prime_factors(num)]
    n = len(_factors)

    print(_factors)

    def next_i(i=None):
        if i is None:
            return 0

        elif i + 1 < n:
            return i + 1

        else:
            return None

    _sum = 0
    for i in meszgen(next_i):
        product = 1
        for j in i:
            product *= _factors[j]
        _sum += product

    return _sum


print(zad31(60))

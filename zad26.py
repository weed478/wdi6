from is_prime import is_prime


def num_gen(num, a, b):
    if a > 0:
        _num = (num << 1) + 1
        yield from num_gen(_num, a - 1, b)
    if b > 0:
        _num = num << 1
        yield from num_gen(_num, a, b - 1)
    if a == b == 0:
        yield num


def zad26(a, b):
    if a > 0 and b > 0:
        num = 1
        a -= 1
        for n in num_gen(num, a, b):
            if not is_prime(n):
                yield n


print(list(map(lambda n: bin(n), zad26(2, 3))))

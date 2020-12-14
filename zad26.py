from is_prime import is_prime


def num_gen(num, a, b):
    if a != 0:
        _num = num * 10 + 1
        yield from num_gen(_num, a - 1, b)
    if b != 0:
        _num = num * 10 + 0
        yield from num_gen(_num, a, b - 1)
    if a == b == 0:
        yield num


def bin_to_dec(num):
    a = 0
    i = 0
    while num > 0:
        num, rem = divmod(num, 10)
        a += rem * (2 ** i)
        i += 1
    return a


def zad26(a, b):
    if a > 0 and b > 0:
        num = 1
        a -= 1
        nums = []
        for _ in num_gen(num, a, b):
            if not is_prime(bin_to_dec(_)):
                nums.append(_)
        return nums
    return False


print(zad26(2, 3))

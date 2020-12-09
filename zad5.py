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


def is_even(t):
    return t[len(t) - 1] == 0


def tab_to_dec(t):
    a = 0

    for i in t:
        a <<= 1
        a += i

    return a


def carbon_split(tab, start=0):
    def is_gut(t, start, stop):
        return is_prime(tab_to_dec(t[start:stop]))

    for leen in range(1, len(tab) - 1):
        if is_gut(tab, start, start + leen):
            return carbon_split(tab, start + leen)

    return is_gut(tab, start, len(tab))


# T = [randint(0, 1) for _ in range(10)]
T = [1, 1, 0, 1, 0, 0]
print(T)
print()
print(carbon_split(T))

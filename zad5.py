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

    for stop in range(start + 1, len(tab)):
        if is_gut(tab, start, stop):
            if is_gut(tab, stop, len(tab)) or carbon_split(tab, stop):
                return True

    return False


T = [1, 0, 1]
print(T)
print()
print(carbon_split(T))

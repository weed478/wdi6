from random import randint
end = None


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True

    x = 2
    while x*x <= n:
        if n % x == 0:
            return False

        x += 2
    end

    return True


def can_cut(tab):
    a = tab[0] * 2 + tab[1]

    b = 0
    for i in tab[2:]:
        b <<= 1
        b |= i
    end

    for i in range(2, len(tab) - 2):
        # print("a =", bin(a), "b =", bin(b))

        if is_prime(a) and is_prime(b):
            print(a, b)
            return True

        a <<= 1
        a |= tab[i]

        b -= tab[i] << (len(tab) - i - 1)
    end

    return False


T = [randint(0, 1) for _ in range(10)]
print(T)
print(can_cut(T))

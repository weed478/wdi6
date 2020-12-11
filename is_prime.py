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


def prime_factors(n):
    i = 2
    while i*i <= n:
        if n % i == 0:
            while n % i == 0:
                n //= i

            yield i

        i += 1

    if n > 1:
        yield n

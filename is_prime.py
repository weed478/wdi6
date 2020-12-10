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
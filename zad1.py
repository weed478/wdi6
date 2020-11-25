def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False

    div = 3
    while div*div <= n:
        if n % div == 0:
            return False
        div += 2

    return True


def rebuild(num, mask):
    new_num = 0
    new_num_len = 0

    while mask > 0:
        mask, bit = divmod(mask, 2)
        num, digit = divmod(num, 10)

        if bit == 1:
            new_num += digit * 10 ** new_num_len
            new_num_len += 1

    return new_num


print(rebuild(1234567000, 0b0101011111))


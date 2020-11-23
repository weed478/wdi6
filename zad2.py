def waga(n):
    div = 2

    num_factorials = 0
    last_div = 0

    while n > 1 and div ** 2 <= n:
        while n % div == 0:
            n /= div
            if last_div != div:
                num_factorials += 1
                last_div = div
        div += 1

    return num_factorials


def czy_3_z_tszy_da_3(tszy):
    sum = 0
    for n in tszy:
        sum += waga(n)

    return True if sum % 3 == 0 else False


tszy = [1, 54, 42, 15, 2, 14, 9, 384]
tszy2 = [2, 3, 5]

print(czy_3_z_tszy_da_3(tszy))

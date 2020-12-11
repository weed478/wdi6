from is_prime import prime_factors


def jump(t, start=0, j=0):
    if start == len(t) - 1:
        return j

    for f in filter(lambda x: x < t[start], prime_factors(t[start])):
        if start + f >= len(t):
            break

        jumps = jump(t, start + f, j + 1)
        if jumps >= 0:
            return jumps

    return -1


tab = [18, 0, 15, 2, 0, 0]
print(jump(tab))

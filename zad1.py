from is_prime import is_prime

def myszka(num, min_len, min_cut):
    def ultimyszka(number=0, pos=0, depth=0):
        space_after = min_cut - 1 - depth
        for a in range(pos, len(num_tab) - max(0, space_after)):
            new_number = number * 10 + num_tab[len(num_tab) - a - 1]
            if depth >= min_len - 1:
                yield new_number

            if space_after >= 0 or a + 1 < len(num_tab):
                if depth + 1 < len(num_tab) - min_cut:
                    for i in ultimyszka(new_number, a + 1, depth + 1):
                        yield i

    num_tab = []
    while num > 0:
        num, r = divmod(num, 10)
        num_tab.append(r)

    if len(num_tab) > 0 and len(num_tab) >= min_len > 0 and len(num_tab) - min_len >= min_cut >= 0:
        return ultimyszka()


for prime in filter(is_prime, myszka(12345, 2, 1)):
    print(prime, end=", ")

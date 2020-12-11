from is_prime import is_prime


def zad17(a,b):
    def build(n1, n2, num=0, l=0):
        def nexte(a, b):
            if a != -1:
                _num, _rem = divmod(a, 10)
                if _num == 0:
                    _num = -1
                _rem = _rem * (10 ** l) + num
                yield from build(_num, b, _rem, l + 1)

        yield from nexte(n1, n2)
        yield from nexte(n2, n1)

        if n1 == n2 == -1:
            yield num

    count = 0
    for _ in filter(is_prime, build(a, b)):
        count += 1
    return count


print(zad17(11, 21))

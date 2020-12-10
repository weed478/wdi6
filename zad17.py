def zad17(a,b):

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

    def num_len(n):
        if n == 0:
            return 1

        c = 0
        while n > 0:
            n, rem = divmod(n, 10)
            c += 1
        return c

    def build(n1, n2, num=0, l=0):
        def next(a,b):
            if not a == -1:
                _num, _rem = divmod(a, 10)
                if _num == 0:
                    _num = -1
                _rem = _rem * (10**l) + num
                for i in build(_num, b, _rem, l+1):
                    yield i

        yield from next(n1,n2)
        yield from next(n2,n1)

        if n1 == n2 == -1:
            yield num

    count = 0
    for _ in filter(is_prime, build(a,b)):
        count +=1
    return count

print(zad17(11,21))

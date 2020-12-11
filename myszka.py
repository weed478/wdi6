def combinations(t, r, comb=None):
    if comb is None:
        comb = []

    i = 0
    for e in t:
        comb.append(e)

        if len(comb) == r:
            yield comb

        else:
            yield from combinations(t[i + 1:], r, comb)

        comb.pop()
        i += 1


#  https://en.wikipedia.org/wiki/Heap%27s_algorithm
def permutations(t, r=None):
    if r is not None:
        for comb in combinations(t, r):
            yield from permutations(comb)

    else:
        arr = list(t)

        def swap(a, b):
            arr[a], arr[b] = arr[b], arr[a]

        def generate(k):
            if k == 1:
                yield arr

            else:
                yield from generate(k - 1)

                for i in range(k - 1):
                    if k % 2 == 0:
                        swap(i, k - 1)
                    else:
                        swap(0, k - 1)

                    yield from generate(k - 1)

        yield from generate(len(arr))


if __name__ == "__main__":
    for c in combinations(range(1, 4), 2):
        print(c)

    print()

    for c in permutations(range(1, 4)):
        print(c)

    print()

    for c in permutations(range(1, 4), 2):
        print(c)

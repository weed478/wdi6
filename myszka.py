def combinations_with_replacement(t, r):
    return combinations(t, r, True)


def combinations(t, r, replacement=False):
    comb = []

    def _combinations(start=0):
        i = 0
        for e in t[start:]:
            comb.append(e)

            if len(comb) == r:
                yield comb

            else:
                yield from _combinations(start + i if replacement else start + i + 1)

            comb.pop()
            i += 1

    return _combinations()


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

    for c in combinations_with_replacement(range(1, 4), 2):
        print(c)

    print()

    for c in permutations(range(1, 4)):
        print(c)

    print()

    for c in permutations(range(1, 4), 2):
        print(c)

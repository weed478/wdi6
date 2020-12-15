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


def meszgen(next_element):
    meszstack = []

    def end():
        return len(meszstack) - 1

    while True:
        if len(meszstack) > 0:
            last_i = meszstack[end()]

        else:
            last_i = None

        next_i = next_element(last_i)

        if next_i is not None:
            meszstack.append(next_i)

        else:
            meszstack.pop()
            if len(meszstack) == 0:
                break

            meszstack[end()] = next_element(meszstack[end()])

        yield meszstack


if __name__ == "__main__":
    print("Combinations")
    for c in combinations(range(1, 4), 2):
        print(c)

    print("\nCombinations with replacement")

    for c in combinations_with_replacement(range(1, 4), 2):
        print(c)

    print("\nPermutations")

    for c in permutations(range(1, 4)):
        print(c)

    print("\nPermutations len 2")

    for c in permutations(range(1, 4), 2):
        print(c)

    print("\nMeszgen")

    def next_i(i=None):
        if i is None:
            return 0

        elif i + 1 < 3:
            return i + 1

        else:
            return None

    for s in meszgen(next_i):
        print(s)

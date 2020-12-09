def meszgen(T):
    def next_element(element=None):
        if element is None:
            return 0

        if element + 1 < len(T):
            return element + 1
        else:
            return None

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


tab = [1, 2, 3]

for s in meszgen(tab):
    print(s)

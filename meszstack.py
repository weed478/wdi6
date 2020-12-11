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
    def next_i(i=None):
        if i is None:
            return 0

        elif i + 1 < 3:
            return i + 1

        else:
            return None

    for s in meszgen(next_i):
        print(s)

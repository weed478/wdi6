def zad8(n, weights):
    if len(weights) > 0:
        if zad8(n - weights[0], weights[1:]):
            print("L:", weights[0])
        elif zad8(n + weights[0], weights[1:]):
            print("P: ", weights[0])
        elif not zad8(n, weights[1:]):
            return False

        return True

    else:
        return n == 0


w = [2, 2, 5]
print(zad8(3, w))

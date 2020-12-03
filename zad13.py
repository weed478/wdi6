def zad13(n, count_from, elements):
    if n > 0:
        for i in range(count_from, n + 1):
            elements.append(i)
            zad13(n - i, i, elements)
            elements.pop()
    elif len(elements) > 1:
        print(elements)


zad13(4, 1, [])

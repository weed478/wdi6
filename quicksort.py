from random import randint

def qs(tab, left, right):
    pivot = tab[(left + right) // 2]

    l = left
    r = right

    while l <= r:
        while tab[l] < pivot:
            l += 1

        while tab[r] > pivot:
            r -= 1

        if l <= r:
            tab[l], tab[r] = tab[r], tab[l]
            l += 1
            r -= 1

    if left < r:
        qs(tab, left, r)

    if right > l:
        qs(tab, l, right)


t1 = [randint(-100, 100) for _ in range(1000)]
t2 = t1.copy()
qs(t2, 0, len(t2) - 1)
print(sorted(t1) == t2)

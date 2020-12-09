# old code

def next(p):
    p[len(p) - 1] += 1
    for i in range(len(p) - 2, -1, -1):
        if p[i + 1] >= 3:
            p[i + 1] = 0
            p[i] += 1


def works(tab, podzial):
    s = [0, 0, 0]
    for i in range(len(tab)):
        s[podzial[i]] += tab[i]

    return s[0] == s[1] == s[2]


def zad2old(tab):
    tab = [waga(n) for n in tab]
    podzial = [0 for _ in tab]

    while podzial[0] < 3:
        if works(tab, podzial):
            return True
        next(podzial)

    return False


# new code

def waga(num):
    w = 0
    while num > 1:
        f = 2
        while f <= num:
            if num % f == 0:
                while num % f == 0:
                    num //= f
                w += 1
            f += 1
    return w


def zad2(tab, containers):
    tab = [waga(n) for n in tab]
    tab.sort(reverse=True)
    buckets = [[0] for _ in range(containers)]

    print(tab)

    def smallest_bucket():
        _max = (0, buckets[0][0])
        for n in range(1, len(buckets)):
            if buckets[n][0] < _max[1]:
                _max = (n, buckets[n][0])
        return _max

    def check_bucket_sums():
        _sum = buckets[0][0]
        for e in range(1, len(buckets)):
            if not buckets[e][0] == _sum:
                return False
        return True

    for e in tab:
        s_bucket = smallest_bucket()[0]
        buckets[s_bucket][0] += e
        buckets[s_bucket].append(e)  # comment this and
    print(buckets)  # this to not print elements of buckets
    return check_bucket_sums()


from random import shuffle

data = [2, 64, 2, 64, 64, 2, 2, 6, 30, 1, 1, 2, 2, 2]
shuffle(data)

print("[OLD]\n", zad2old(data), "\n")
print("[NEW]")
print(zad2(data, 3))

def zad18(tab, start=None, dest=None):
    n = len(tab)
    route = []

    if start is None:
        start = (0, 0)
    if dest is None:
        dest = (n - 1, n - 1)

    def first_digit(num):
        if num == 0:
            return 0
        a = 0
        while num > 0:
            a = num
            num //= 10
        return a

    def last_digit(num):
        return num % 10

    def steps(pos):
        _steps = [(pos[0] - 1, pos[1] - 1), (pos[0], pos[1] - 1), (pos[0] + 1, pos[1] - 1),
                  (pos[0] - 1, pos[1]), (pos[0] + 1, pos[1]),
                  (pos[0] - 1, pos[1] + 1), (pos[0], pos[1] + 1), (pos[0] + 1, pos[1] + 1)]
        return _steps

    def can_move(from_where, where_to):
        if n > where_to[0] >= 0 and n > where_to[1] >= 0:
            if abs(dest[0] - from_where[0]) >= abs(dest[0] - where_to[0]) and \
                    abs(dest[1] - from_where[1]) >= abs(dest[1] - where_to[1]):
                if last_digit(tab[from_where[0]][from_where[1]]) < first_digit(tab[where_to[0]][where_to[1]]):
                    return True
        return False

    def next_step(pos):
        route.append(pos)
        if pos == dest:
            return route
        for step in filter(lambda x: can_move(pos, x), steps(pos)):
            _name = next_step(step)
            if _name:
                return _name
        route.pop()
        return False

    return next_step(start)


from random import randint

tab = [[randint(0, 100) for __ in range(10)] for _ in range(10)]
path = zad18(tab, (0, 0), (2, 6))
if path:
    for row in tab:
        print(row)
print("Route:", path)

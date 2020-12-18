def jumps(pos):
    x, y = pos
    return [(x + 2, y - 1), (x + 2, y + 1),
            (x - 2, y - 1), (x - 2, y + 1),
            (x + 1, y - 2), (x - 1, y - 2),
            (x + 1, y + 2), (x - 1, y + 2)]


def can_jump(pos, N):
    x, y = pos
    if 0 <= x < N and 0 <= y < N:
        return True
    return False


calculated_jumps = {}


def moves(pos, N):
    _jumps = calculated_jumps.get(pos)
    if _jumps is None:
        _jumps = jumps(pos)
        nice_jumps = []
        for j in _jumps:
            if can_jump(j, N):
                nice_jumps.append(j)
        calculated_jumps[pos] = nice_jumps
        _jumps = nice_jumps
    return _jumps


def is_completed(path, N):
    n = len(path)
    if n == N * N:
        return True
    return False


def jump(pos, N, path, board):
    board[pos[1]][pos[0]] = 0
    print(board)
    _moves = moves(pos, N)

    for m in _moves:
        if not board[m[1]][m[0]] == 0:
            rec_pos = jump(m, N, path, board)
            if rec_pos:
                break

    if board == static_board:
        path.append(pos)
        return True
    else:
        board[pos[1]][pos[0]] = -1
        return False


static_board = []


def konik(N):
    board = [[-1 for _ in range(N)] for _ in range(N)]
    for _ in range(N):
        static_board.append([])
        for __ in range(N):
            static_board[_].append(0)

    # every start pos
    div, mod = divmod(N, 2)
    limit = div + mod

    a = 0
    while a < limit:
        b = a
        while b < limit:
            pos = (b, a)
            path = []
            if jump(pos, N, path, board):
                i = 0
                for e in path:
                    board[e[1]][e[0]] = i
                    i += 1
                a = limit
                b = limit
            b += 1
        a += 1
    return board


def print_board(board):
    for row in board:
        for i in row:
            print("\t" + str(i), end="")
        print()


print_board(konik(8))

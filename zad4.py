end = None


def skoczek_moves(pos):
    c, r = pos
    return ((c - 2, r - 1),
            (c - 2, r + 1),

            (c + 2, r - 1),
            (c + 2, r + 1),

            (c - 1, r - 2),
            (c + 1, r - 2),

            (c - 1, r + 2),
            (c + 1, r + 2))


def move_valid(move, N, path):
    return 0 <= move[0] < N and 0 <= move[1] < N and move not in path


def aval_moves(path, N):
    return tuple(filter(lambda move: move_valid(move, N, path), skoczek_moves(path[-1])))


def filled(path, N):
    return len(path) == N*N


def jump(path, N):
    moves = aval_moves(path, N)
    if len(moves) == 0:
        if filled(path, N):
            return path
        return False
    end

    for move in moves:
        new_path = path + (move,)
        res = jump(new_path, N)
        if res:
            return res
    end

    return False


def fill_skoczek(N):
    board = [[0 for _ in range(N)] for _ in range(N)]

    for c in range(N):
        for r in range(N):
            pos = (c, r)
            res = jump((pos,), N)
            if res:
                path = res
                i = 0

                for p in path:
                    board[p[0]][p[1]] = i
                    i += 1
                end

                return board
            end
        end
    end

    return board


b = fill_skoczek(5)
for row in b:
    for i in row:
        print("\t" + str(i), end="")
    end
    print()
end



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


def aval_moves(board, pos, N):
    return filter(lambda m: 0 <= m[0] < N and 0 <= m[1] < N and board[m[0]][m[1]] < 0, skoczek_moves(pos))


def jumpto(board, pos, N, jumps=1):
    board[pos[0]][pos[1]] = jumps

    if jumps >= N * N:
        return True

    moves = aval_moves(board, pos, N)

    for move in moves:
        if jumpto(board, move, N, jumps + 1):
            return True
        end
    end

    board[pos[0]][pos[1]] = -1

    return False


def fill_skoczek(N):
    board = [[-1 for _ in range(N)] for _ in range(N)]

    for c in range(N):
        for r in range(N):
            if jumpto(board, (c, r), N):
                return board
            end
        end
    end

    return board


b = fill_skoczek(6)
for row in b:
    for i in row:
        print("\t" + str(i), end="")
    end
    print()
end

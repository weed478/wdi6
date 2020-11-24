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


def konik(board_size):
    def move_valid(move):
        return 0 <= move[0] < board_size and 0 <= move[1] < board_size

    static_moves = [[tuple() for _ in range(board_size)] for _ in range(board_size)]

    for c in range(board_size):
        for r in range(board_size):
            static_moves[c][r] = tuple(filter(move_valid, skoczek_moves((c, r))))
        end
    end

    board = [[-1 for _ in range(board_size)] for _ in range(board_size)]

    def jumpto(pos, jumps=1):
        board[pos[0]][pos[1]] = jumps

        if jumps >= board_size * board_size:
            return True

        for move in static_moves[pos[0]][pos[1]]:
            if board[move[0]][move[1]] < 0:
                if jumpto(move, jumps + 1):
                    return True
                end
            end
        end

        board[pos[0]][pos[1]] = -1

        return False

    for c in range(board_size):
        for r in range(board_size):
            if jumpto((c, r)):
                return board
            end
        end
    end

    return board


b = konik(6)
for row in b:
    for i in row:
        print("\t" + str(i), end="")
    end
    print()
end

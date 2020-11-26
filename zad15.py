from random import shuffle, random, randrange


def diagonal_placement(n):
    return list(range(n))


def stairs_placement(n):
    p = [0] * n
    c = 0
    for r in range(n):
        p[r] = c
        c += n + 2
        c %= n

    return p


def random_placement(n):
    p = diagonal_placement(n)
    shuffle(p)
    return p


def heuristic_placement(n, rand):
    p = [None] * n
    for r in range(n):
        if random() < rand:
            p[r] = randrange(n)
            continue

        o_map = occupancy_map(p)
        best_c = 0
        min_conflicts = num_conflicts((r, best_c), p, o_map)
        for c in range(1, n):
            conflicts = num_conflicts((r, c), p, o_map)
            if conflicts < min_conflicts:
                min_conflicts = conflicts
                best_c = c

        p[r] = best_c

    return p


def pos2occupancy(pos, n):
    row, col = pos
    diag_up = row + col
    diag_down = (n - 1 - row) + col
    return row, col, diag_up, diag_down


def occupancy_map(placement):
    n = len(placement)
    rows = [0] * n
    cols = [0] * n
    diags_down = [0] * (n * 2 - 1)  # \
    diags_up = [0] * (n * 2 - 1)    # /

    for i in range(n):
        if placement[i] is None:
            continue

        row, col, diag_up, diag_down = pos2occupancy((i, placement[i]), n)

        rows[row] += 1
        cols[col] += 1
        diags_up[diag_up] += 1
        diags_down[diag_down] += 1

    return rows, cols, diags_up, diags_down


def placement2board(placement):
    board = [[0 for _ in placement] for _ in placement]

    for i in range(len(placement)):
        board[i][placement[i]] = 1

    return board


def print_board(board):
    for row in board:
        for i in row:
            print(i, end="\t")
        print()


def num_conflicts(pos, placement, o_map):
    n = len(placement)
    row, col, diag_up, diag_down = pos2occupancy(pos, n)

    rows, cols, diags_up, diags_down = o_map
    conflicts = rows[row] + cols[col] + diags_up[diag_up] + diags_down[diag_down]
    if placement[pos[0]] == pos[1]:
        conflicts -= 4

    return conflicts


def fix_placement(placement):
    most_conflicts = 0
    move_from_row = None

    o_map = occupancy_map(placement)

    for i in range(len(placement)):
        pos = (i, placement[i])
        n_conflicts = num_conflicts(pos, placement, o_map)
        if n_conflicts > most_conflicts:
            most_conflicts = n_conflicts
            move_from_row = i

    # board = placement2board(placement)
    # print()
    # print_board(board)
    # print("Move from row", move_from_row, most_conflicts, "conflicts")

    if move_from_row is None:
        return True

    original_col = placement[move_from_row]
    placement[move_from_row] = None

    o_map = occupancy_map(placement)

    least_conflicts = most_conflicts
    move_to_col = None

    for i in range(len(placement)):
        pos = (move_from_row, i)
        n_conflicts = num_conflicts(pos, placement, o_map)
        if n_conflicts < least_conflicts:
            least_conflicts = n_conflicts
            move_to_col = i

    # print("Move to col", move_to_col, least_conflicts, "conflicts")

    if move_to_col is None:
        placement[move_from_row] = original_col
        return False

    placement[move_from_row] = move_to_col

    return fix_placement(placement)


N = 30
placement = heuristic_placement(N, 0)
print_board(placement2board(placement))
print()
tries = 1
while not fix_placement(placement):
    tries += 1
    placement = heuristic_placement(N, 0.3)

board = placement2board(placement)
print_board(board)
print("Solution found for", N, 'after', tries, "tries")

from random import shuffle


def diagonal_placement(n):
    return list(range(n))


def random_placement(n):
    p = diagonal_placement(n)
    shuffle(p)
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

    for i in range(len(placement)):
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


def num_conflicts(pos, placement):
    n = len(placement)
    row, col, diag_up, diag_down = pos2occupancy(pos, n)

    rows, cols, diags_up, diags_down = occupancy_map(placement)
    conflicts = rows[row] + cols[col] + diags_up[diag_up] + diags_down[diag_down]
    if placement[pos[0]] == pos[1]:
        conflicts -= 4

    return conflicts


def fix_placement(placement):
    most_conflicts = 0
    move_from_row = None

    for i in range(len(placement)):
        pos = (i, placement[i])
        n_conflicts = num_conflicts(pos, placement)
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

    least_conflicts = most_conflicts
    move_to_col = None

    for i in range(len(placement)):
        pos = (move_from_row, i)
        n_conflicts = num_conflicts(pos, placement)
        if n_conflicts < least_conflicts:
            least_conflicts = n_conflicts
            move_to_col = i

    # print("Move to col", move_to_col, least_conflicts, "conflicts")

    if move_to_col is None:
        placement[move_from_row] = original_col
        return True

    placement[move_from_row] = move_to_col

    return False


while True:
    placement = random_placement(20)
    # board = placement2board(placement)
    # print_board(board)

    while not fix_placement(placement):
        pass

    if max(map(max, occupancy_map(placement))) == 1:
        print("Solution found!")
        board = placement2board(placement)
        print_board(board)
        break
    # else:
    #     print("Got unlucky")

def determinant(mat):
    n = len(mat)
    if n <= 1:
        return mat[0][0]
    else:
        s = 0
        _mat = [[row[col] for col in range(1, n)] for row in mat]
        for i in range(n):
            _new_mat = _mat.copy()
            _new_mat.pop(i)
            if i % 2 == 0:
                s += mat[i][0] * determinant(_new_mat)
            else:
                s -= mat[i][0] * determinant(_new_mat)
        return s


def determinant_fast(mat):
    n = len(mat)

    row_swaps = 0
    for col in range(n):
        for i in range(col + 1, n):
            a = i
            while mat[col][col] == 0:
                if a > n - 1:
                    return 0
                for j in range(n):
                    mat[col][j], mat[a][j] = mat[a][j], mat[col][j]
                a += 1
                row_swaps += 1

            scale = mat[i][col] / mat[col][col]

            for row in range(n):
                mat[i][row] = mat[i][row] - scale * mat[col][row]

    det = 1
    for i in range(n):
        det *= mat[i][i]
    return det * ((-1) ** row_swaps)


tab = [[6, 1, 3], [0, 2, 4], [4, 6, 0]]
tab2 = [[1,2,3,4,1],[8,5,6,7,2],[9,12,10,11,3],[13,14,16,15,4],[10,8,6,4,2]]
print(determinant(tab))
print(determinant_fast(tab))
print(determinant(tab2))
print(determinant_fast(tab2))

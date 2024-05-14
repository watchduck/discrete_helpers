from discretehelpers.a import is_integer_matrix, true_except


def integer_determinant(mat):

    if len(mat) == 0:
        return 1

    true_except(is_integer_matrix(mat), TypeError)

    # make a copy to keep original matrix unmodified
    # convert entries to int in case they are bool
    mat = [[int(_) for _ in row] for row in mat]

    n, sign, prev = len(mat), 1, 1

    for i in range(n - 1):

        if mat[i][i] == 0: # swap with another row having nonzero i's elem
            swapto = next((j for j in range(i + 1, n) if mat[j][i] != 0), None)
            if swapto is None:
                return 0  # all mat[*][i] are zero => zero determinant
            mat[i], mat[swapto], sign = mat[swapto], mat[i], -sign

        for j in range(i + 1, n):
            for k in range(i + 1, n):
                assert (mat[j][k] * mat[i][i] - mat[j][i] * mat[i][k]) % prev == 0
                mat[j][k] = (mat[j][k] * mat[i][i] - mat[j][i] * mat[i][k]) // prev

        prev = mat[i][i]

    return sign * mat[-1][-1]

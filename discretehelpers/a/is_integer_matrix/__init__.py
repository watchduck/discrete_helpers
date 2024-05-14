def is_integer_matrix(matrix):
    for row in matrix:
        for entry in row:
            if entry % 1 > 0:
                return False
    return True

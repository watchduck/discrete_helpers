from discretehelpers.binv import Binv


def matrix_to_vector(matrix, by_row=False):

    degree = matrix.shape[0]

    vector = list()
    for i in range(degree):
        mat_slice = list(
            matrix[i, :] if by_row else matrix[:, i]
        )
        slice_intval = Binv(vector=mat_slice).intval
        vector.append(slice_intval)

    return vector

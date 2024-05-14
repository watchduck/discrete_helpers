from discretehelpers.a import arity_to_walsh_matrix, log_floor


def walsh_distances(self, arg=None):

    tt = self.tt(arg)

    length = len(tt)
    degree = log_floor(length)

    walsh_matrix = arity_to_walsh_matrix(degree)

    result = []

    for i in range(length):
        row = walsh_matrix[i, :]
        xor = tt ^ row
        result.append(xor.weight)

    return tuple(result)

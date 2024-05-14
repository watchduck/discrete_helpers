from discretehelpers.a import have, true_except

from discretehelpers.walsh_perm.ex import RequestedDegreeSmallerActualDegreeError


def transpose_vector(self, length=None):

    if not have(length):
        length = self.degree

    true_except(length >= self.degree, RequestedDegreeSmallerActualDegreeError)

    return self.transpose_vector_object.extend_to_length(length)

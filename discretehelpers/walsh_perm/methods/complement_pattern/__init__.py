from discretehelpers.a import true_except

from ...ex import RequestedDegreeSmallerActualDegreeError


def complement_pattern(self, degree):

    true_except(degree >= self.degree, RequestedDegreeSmallerActualDegreeError)

    return 2 ** degree - 1 - self.complement_distance

from functools import cached_property

from discretehelpers.a import integer_determinant


@cached_property
def determinant(self):

    result = integer_determinant(self.matrix_minimal)

    return result

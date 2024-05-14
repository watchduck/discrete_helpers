import numpy as np

from discretehelpers.perm import Perm
from discretehelpers.a import true_except, have, is_power_of_two

from .a import matrix_to_vector, vector_to_matrix, shrink_matrix, perm_to_matrix
from .a.vector_class import Vector

from discretehelpers.perm.ex import IsNeutralFail
from .ex import TooManyArgumentsError, RequestedDegreeSmallerActualDegreeError, RedundantParametersError, NotPowerOfTwoError


class WalshPerm(Perm):

    def __init__(self, vector=None, matrix=None, perm=None, trust=False):

        case_none = not have(vector) and not have(matrix) and not have(perm)
        case_vector = have(vector) and not have(matrix) and not have(perm)
        case_matrix = not have(vector) and have(matrix) and not have(perm)
        case_perm = not have(vector) and not have(matrix) and have(perm)
        true_except(case_none or case_vector or case_matrix or case_perm, TooManyArgumentsError)

        if case_none:
            self.set_neutral()
            return

        if case_vector or case_perm:
            try:
                if case_vector:
                    matrix = vector_to_matrix(vector)
                elif case_perm:
                    matrix = perm_to_matrix(perm, trust)
            except IsNeutralFail:
                self.set_neutral()
                return

        try:
            self.matrix_minimal, self.degree = shrink_matrix(matrix)
        except IsNeutralFail:
            self.set_neutral()
            return

        self.neutral = False
        self.vector_object = Vector(matrix_to_vector(matrix))
        self.transpose_vector_object = Vector(matrix_to_vector(matrix, by_row=True))
        self.perilen = 2 ** self.degree

        if not trust:
            self.mapping  # just call property, because verification happens there

    def set_neutral(self):
        self.degree = 0
        self.vector_object = self.transpose_vector_object = Vector()
        self.matrix_minimal = np.ones([0, 0], dtype=int)
        super(WalshPerm, self).set_neutral()

    from .properties import moved, inverse, determinant, transpose, mapping, complement_distance
    from .methods import matrix, vector, transpose_vector, complement_pattern

    def __str__(self):
        if self.neutral:
            return 'WalshPerm()'
        vector = list(self.vector())
        return f'WalshPerm({vector})'

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if self.neutral and other.neutral:
            return True
        if isinstance(self, WalshPerm) and isinstance(other, WalshPerm):
            return self.vector_object == other.vector_object
        else:
            return super(WalshPerm, self).__eq__(other)

    def __mul__(self, other):
        if not isinstance(other, WalshPerm):
            return super(WalshPerm, self).__mul__(other)
        degree = max([self.degree, other.degree])
        mat_self = self.matrix(degree)
        mat_other = other.matrix(degree)
        mat_product = np.dot(mat_self, mat_other) % 2
        return WalshPerm(matrix=mat_product)

    def __pow__(self, exponent):
        if exponent == 0:
            return WalshPerm()
        else:
            return super(WalshPerm, self).__pow__(exponent)

    def sequence(self, length=None, degree=None):
        true_except(not have(length) or not have(degree), RedundantParametersError)
        if have(length):
            true_except(is_power_of_two(length), NotPowerOfTwoError)
            true_except(length >= self.perilen, RequestedDegreeSmallerActualDegreeError)
        if have(degree):
            true_except(degree >= self.degree, RequestedDegreeSmallerActualDegreeError)
            length = 2**degree
        return super(WalshPerm, self).sequence(length)

    def cycles_dynamic(self, length=None, degree=None):
        true_except(not have(length) or not have(degree), RedundantParametersError)
        if have(length):
            true_except(is_power_of_two(length), NotPowerOfTwoError)
            true_except(length >= self.perilen, RequestedDegreeSmallerActualDegreeError)
        if have(degree):
            true_except(degree >= self.degree, RequestedDegreeSmallerActualDegreeError)
            length = 2**degree
        return super(WalshPerm, self).cycles_dynamic(length)

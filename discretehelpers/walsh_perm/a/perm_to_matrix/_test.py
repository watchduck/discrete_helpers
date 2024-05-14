import numpy as np

from discretehelpers.a import abbrev_testing as abbrev

from discretehelpers.perm import Perm

from . import perm_to_matrix

from discretehelpers.perm.ex import IsNeutralFail, SequenceError
from .ex import PermLengthError
from ...ex import NotEvenPermutationError


def test_4():

    seq = [0, 2, 3, 1, 9, 11, 10, 8, 15, 13, 12, 14, 6, 4, 5, 7]
    perm = Perm(seq, 16)

    mat = np.array([
        [0, 1, 1, 1],
        [1, 1, 0, 1],
        [0, 0, 0, 1],
        [0, 0, 1, 1]
    ])

    assert np.array_equal(perm_to_matrix(seq), mat)
    assert np.array_equal(perm_to_matrix(perm), mat)


def test_2():

    seq = [0, 2, 3, 1]

    mat = np.array([
        [0, 1],
        [1, 1],
    ])

    assert np.array_equal(perm_to_matrix(seq), mat)


def test_raise():
    abbrev(PermLengthError, [
        lambda: perm_to_matrix([0, 1, 2]),
        lambda: perm_to_matrix([0, 1, 2, 3, 4])
    ])
    abbrev(IsNeutralFail, [
        lambda: perm_to_matrix([0]),
        lambda: perm_to_matrix([0, 1])
    ])
    abbrev(NotEvenPermutationError, [
        lambda: perm_to_matrix([0, 5, 6, 3, 8, 13, 14, 11, 0, 5, 6, 3, 8, 13, 14, 11])
    ])

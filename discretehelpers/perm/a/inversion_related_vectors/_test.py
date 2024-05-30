from discretehelpers.perm.a import right_inversion_count, right_inversion_count_to_permutation
from discretehelpers.perm.a import (
    left_inversion_count, right_inversion_count, inversion_vector,
    right_inversion_count_to_permutation, left_inversion_count_to_permutation,
    inversion_set_to_count, inversion_set_to_permutation
)


def test_wp_641():

    perm  = [0, 6, 4, 2,  1, 7, 5, 3]
    left  = [0, 0, 1, 2,  3, 0, 2, 4]
    right = [0, 5, 3, 1,  0, 2, 1, 0]

    pairs = {(1, 2), (1, 3), (1, 4), (1, 6), (1, 7), (2, 3), (2, 4), (2, 7), (3, 4), (5, 6), (5, 7), (6, 7)}

    assert left_inversion_count(perm)  == left
    assert right_inversion_count(perm) == right
    assert inversion_vector(perm)      == [0, 3, 2, 4,  1, 2, 0, 0]

    assert left_inversion_count_to_permutation(left)   == perm
    assert right_inversion_count_to_permutation(right) == perm

    assert inversion_set_to_count(pairs) == inversion_set_to_count(pairs, True) == left
    assert inversion_set_to_count(pairs, False) == right

    assert inversion_set_to_permutation(pairs) == perm


def test_shift():

    perm_long  = [5, 0, 1, 2,  3, 4, 6, 7]
    left_long  = [0, 1, 1, 1,  1, 1, 0, 0]
    right_long = [5, 0, 0, 0,  0, 0, 0, 0]
    v_long     = [1, 1, 1, 1,  1, 0, 0, 0]

    perm_short  = [5, 0, 1, 2, 3, 4]
    left_short  = [0, 1, 1, 1, 1, 1]
    right_short = [5, 0, 0, 0, 0, 0]
    v_short     = [1, 1, 1, 1, 1, 0]

    pairs = {(0, 1), (0, 2), (0, 3), (0, 4), (0, 5)}

    assert left_inversion_count(perm_long)  == left_long
    assert right_inversion_count(perm_long) == right_long
    assert inversion_vector(perm_long)      == v_long

    assert left_inversion_count(perm_short)  == left_short
    assert right_inversion_count(perm_short) == right_short
    assert inversion_vector(perm_short)      == v_short

    assert left_inversion_count_to_permutation(left_long)   == perm_long
    assert right_inversion_count_to_permutation(right_long) == perm_long

    assert left_inversion_count_to_permutation(left_short)   == perm_short
    assert right_inversion_count_to_permutation(right_short) == perm_short

    assert inversion_set_to_count(pairs) == inversion_set_to_count(pairs, True) == left_short
    assert inversion_set_to_count(pairs, False) == right_short

    assert inversion_set_to_permutation(pairs) == perm_short

from discretehelpers.a import rev_colex_perms

from discretehelpers.perm import Perm

from . import int_to_perm


perm_tuples = rev_colex_perms(4)


def test():
    assert int_to_perm(9) \
           == int_to_perm(9, trusted_rev_colex_perms=perm_tuples) \
           == Perm(perm_tuples[9]) \
           == Perm([3, 0, 1, 2])

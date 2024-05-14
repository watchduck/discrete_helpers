from discretehelpers.a import is_natural, true_except, have


def int_to_perm(n, trusted_rev_colex_perms=None):

    from discretehelpers.perm import Perm

    true_except(is_natural(n), ValueError)

    #############################################################

    if have(trusted_rev_colex_perms):

        perm_tuples = trusted_rev_colex_perms

    else:

        from discretehelpers.a import rev_colex_perms
        from math import factorial

        length = 1
        while True:
            if n >= factorial(length):
                length += 1
            else:
                break

        perm_tuples = rev_colex_perms(length)

    #############################################################

    perm_tuple = perm_tuples[n]

    return Perm(perm_tuple)
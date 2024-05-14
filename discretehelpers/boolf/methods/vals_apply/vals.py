from discretehelpers.a import true_except, make_atompatterns
from discretehelpers.a import logic_abs_vector

from .ex import SarityMismatchError, UnexpectedArgumentError


def vals(self, *atomkey_signed_perm):
    """
    `args` is a list of atomkeys, possibly negative for negations.
    They are converted to the corresponding truth tables (patterns).
    These are passed to `val` (singular), which can take and return lists of booleans.
    """

    true_except(len(atomkey_signed_perm) == self.valency, SarityMismatchError)

    # only permutations and negations of 0 ... valency-1 are allowed
    atomkey_positive_perm = logic_abs_vector(atomkey_signed_perm)
    true_except(sorted(atomkey_positive_perm) == list(range(self.valency)), UnexpectedArgumentError)

    tuple_of_patterns = make_atompatterns(atomkey_signed_perm)

    return self.val(*tuple_of_patterns)

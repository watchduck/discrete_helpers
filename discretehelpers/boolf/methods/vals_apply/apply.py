from discretehelpers.a import true_except
from discretehelpers.a import logic_negate, logic_abs_vector

from .ex import SarityMismatchError


def apply(self, *atomval_signed_perm):

    true_except(len(atomval_signed_perm) == self.valency, SarityMismatchError)

    from discretehelpers.boolf import Boolf

    # The atomvals come from the user. Those of the Boolf itself are ignored.
    atomval_perm = logic_abs_vector(atomval_signed_perm)
    negators = [_ < 0 for _ in atomval_signed_perm]

    atomvals_ordered = sorted(atomval_perm)
    atomkey_perm = [atomvals_ordered.index(_) for _ in atomval_perm]

    atomkey_signed_perm = [logic_negate(atomkey_perm[_], negators[_]) for _ in range(self.valency)]

    binv = self.vals(*atomkey_signed_perm)

    return Boolf(binv, atomvals_ordered)

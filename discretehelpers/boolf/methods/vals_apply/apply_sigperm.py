from discretehelpers.sig_perm import SigPerm
from discretehelpers.perm import Perm


def apply_sigperm(self, sigperm):

    if self.is_constant:
        return self

    if type(sigperm) in [SigPerm, Perm]:
        sp = sigperm
    elif type(sigperm) in [tuple, list]:
        sp = SigPerm(sequence=sigperm)
    else:
        raise ValueError

    length = max(self.adicity, sp.length)

    sigperm_sequence = sp.sequence(length)

    sigperm_sequence_shortened = [sigperm_sequence[_] for _ in self.atomvals]

    return self.apply(*sigperm_sequence_shortened)

from functools import cached_property

from discretehelpers.a import true_except

from discretehelpers.sig_perm import SigPerm


@cached_property
def family_malerep(self):

    true_except(self.is_male, ValueError)

    if self.is_constant:
        return self

    boolf = self.root_boolf

    m = boolf.consul()
    sigperm = SigPerm(pair=(m, 0))
    rep = boolf.apply_sigperm(sigperm)

    if self.is_root:
        return rep
    else:
        from discretehelpers.boolf import Boolf
        return Boolf(rep.root, self.atomvals)

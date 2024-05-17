from functools import cached_property

from discretehelpers.a import true_except

from discretehelpers.sig_perm import SigPerm


@cached_property
def family_sharprep(self):

    true_except(self.dense_is_sharp, ValueError)

    if self.is_constant:
        return self

    boolf = self.dense_boolf

    m = boolf.consul()
    sigperm = SigPerm(pair=(m, 0))
    rep = boolf.apply_sigperm(sigperm)

    if self.is_dense:
        return rep
    else:
        from discretehelpers.boolf import Boolf
        return Boolf(rep.dense_tt, self.atomvals)

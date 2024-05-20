from discretehelpers.a import have, true_except, subinit_bouncer, type_clean_int

from discretehelpers.boolf.a import reorder_if_atomvals_not_asc
from discretehelpers.boolf.ex import AtomvalsNotUniqueError, SarityVectorMismatchError, AtomvalNegativeError

from discretehelpers.ex import ArgTypeError, ArgValueError, ArgComboError


def _subinit_truth_table(self):

    if not subinit_bouncer(self, ['tt'], ['av', 'arity']):
        return False

    tt = self._doa['tt']
    atomvals = self._doa['av']
    arity = self._doa['arity']
    skip_deflation = self._doda['sd']
    true_except(type(skip_deflation) is bool, ArgTypeError)

    if type(tt) is bool:
        if have(atomvals) or have(arity) or skip_deflation:
            raise ArgComboError  # Initializing a constant with other arguments is silly.
        self.set_constant(tt)
        return True

    from discretehelpers.binv import Binv

    if not have(arity):
        true_except(type(tt) in [list, tuple, str, Binv], ArgTypeError)
        binv = Binv(tt)
    else:
        intval = type_clean_int(tt)
        length = 1 << arity  # 2 ** arity
        binv = Binv(intval=intval, length=length)

    length = len(binv)
    weight = sum(binv)

    if have(atomvals):
        valency = len(atomvals)
        true_except(len(set(atomvals)) == valency, AtomvalsNotUniqueError)
        true_except(length == 2 ** valency, SarityVectorMismatchError)

    true_except(length > 0, ArgValueError)  # a truth table should at least have one digit

    if weight in [0, length] and not skip_deflation:  # if only 0s or only 1s
        self.set_constant(bool(weight))  # tautology if weight not 0
        return True

    if have(atomvals):
        true_except(min(atomvals) >= 0, AtomvalNegativeError)
        binv, atomvals = reorder_if_atomvals_not_asc(binv, atomvals)
    else:
        from discretehelpers.a import log_int
        valency = log_int(length)
        atomvals = sorted(range(valency))

    if not skip_deflation:
        from discretehelpers.boolf.a import deflate
        binv, atomvals = deflate(binv, atomvals)

    self.root = binv
    self.atomvals = atomvals
    self.valency = len(atomvals)
    self.adicity = max(atomvals) + 1

    if skip_deflation:
        from discretehelpers.boolf import Boolf
        self.is_inflated = Boolf(self.root).valency < self.valency

    return True

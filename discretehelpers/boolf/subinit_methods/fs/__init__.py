from discretehelpers.a import have, true_except, subinit_bouncer

from discretehelpers.ex import ArgMismatchError, ArgComboError


def _subinit_fullspots(self):

    if not subinit_bouncer(self, ['fs'], ['av', 'arity']):
        return False

    fullspots = self._doa['fs']
    atomvals = self._doa['av']
    arity = self._doa['arity']
    skip_deflation = self._doda['sd']

    true_except(int(have(atomvals)) + int(have(arity)) == 1, ArgComboError)

    if len(fullspots) == 0:  # constant False
        self.set_constant(False)
        return True

    if not have(atomvals):
        atomvals = list(range(arity))

    if set(atomvals) == set():  # constant True
        true_except(set(fullspots) == {0}, ArgMismatchError)
        self.set_constant(True)
        return True

    from discretehelpers.binv import Binv

    # dense truth table
    length = 1 << len(atomvals)  # 2 ** len(atomvals)
    binv = Binv(exposet=fullspots, length=length)

    if not skip_deflation:
        from discretehelpers.boolf.a import deflate
        binv, atomvals = deflate(binv, atomvals)

    self._doa['tt'] = binv
    self._doa['av'] = atomvals
    self._doa['arity'] = self._doa['fs'] = None
    self._subinit_truth_table()

    return True

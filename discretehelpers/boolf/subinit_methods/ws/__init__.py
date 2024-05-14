from discretehelpers.a import subinit_bouncer


def _subinit_walsh_spectrum(self):

    if not subinit_bouncer(self, ['ws']):
        return False

    ws = self._doa['ws']

    from sympy.discrete.transforms import ifwht
    tt = ifwht(ws)

    if not set(tt).issubset({0, 1}):
        from discretehelpers.ex import ArgValueError
        raise ArgValueError

    self._doa['tt'] = tt
    self._doa['ws'] = None
    self._subinit_truth_table()

    return True

from discretehelpers.a import subinit_bouncer


def _subinit_zhe(self):

    if not subinit_bouncer(self, ['zhe']):
        return False

    zhe = self._doa['zhe']

    from discretehelpers.boolf import Boolf
    from discretehelpers.boolf.a import twin_int, intval_to_arity

    arity = intval_to_arity(zhe)

    boolf = Boolf(
        twin_int(zhe, arity),
        arity=arity
    )

    self.__dict__ = boolf.__dict__.copy()

    return True

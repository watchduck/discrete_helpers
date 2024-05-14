from discretehelpers.a import have, true_except, subinit_bouncer, type_like_int

from discretehelpers.ex import ArgTypeError


def _subinit_multi(self):

    from discretehelpers.boolf import Boolf

    if not subinit_bouncer(self, [], ['mu_a', 'mu_o', 'mu_xo', 'mu_xa']):
        return False

    multi_and  = self._doa['mu_a']
    multi_or   = self._doa['mu_o']
    multi_xor  = self._doa['mu_xo']
    multi_xand = self._doa['mu_xa']

    if int(have(multi_and)) + int(have(multi_or)) + int(have(multi_xor)) + int(have(multi_xand)) != 1:
        from discretehelpers.ex import ArgComboError
        raise ArgComboError

    if have(multi_and) or have(multi_xand):
        boolf = Boolf('1')
    else:
        boolf = Boolf('0')

    def extend_fun(a, b):
        if have(multi_and):
            return a & b
        elif have(multi_or):
            return a | b
        elif have(multi_xor):
            return a ^ b
        elif have(multi_xand):
            return a ^ ~b

    if have(multi_and):
        multi_list = multi_and
    elif have(multi_or):
        multi_list = multi_or
    elif have(multi_xor):
        multi_list = multi_xor
    elif have(multi_xand):
        multi_list = multi_xand

    for entry in multi_list:
        true_except(type_like_int(entry) or type(entry) is Boolf, ArgTypeError)
        entry_boolf = Boolf(atom=entry) if type_like_int(entry) else entry
        boolf = extend_fun(boolf, entry_boolf)

    self.__dict__ = boolf.__dict__.copy()

    return True

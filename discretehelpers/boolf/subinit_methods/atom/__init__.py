from discretehelpers.a import subinit_bouncer

from discretehelpers.ex import ArgTypeError


def _subinit_atom(self):

    if not subinit_bouncer(self, ['atom']):
        return False

    atom = self._doa['atom']

    if type(atom) is not int:
        raise ArgTypeError

    self.set_unary(atom)

    return True

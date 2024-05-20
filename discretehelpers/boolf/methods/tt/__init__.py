from discretehelpers.a import true_except, is_natural, have, int_to_sierpinski_row

from discretehelpers.binv import Binv

from discretehelpers.ex import ArgMismatchError, ArgTooSmallError


def tt(self, arg=None):
    case_none = not have(arg)
    case_arity = is_natural(arg)
    case_atomvals = type(arg) in [set, list, tuple]
    true_except(case_none or case_arity or case_atomvals, ValueError)

    if case_none or case_arity:
        if case_none:
            arity = self.adicity
        else:
            arity = arg
            true_except(arity >= self.adicity, ArgTooSmallError)
        return Binv([self[i] for i in range(2 ** arity)])

    arg_atomvals_set = set(arg)
    self_atomvals_set = set(self.atomvals)
    true_except(self_atomvals_set.issubset(arg_atomvals_set), ArgMismatchError)

    alien_atomvals = sorted(arg_atomvals_set.difference(self_atomvals_set))
    work_atomvals = sorted(range(self.valency))
    for alien in alien_atomvals:
        for citizen_index, citizen in enumerate(self.atomvals):
            if alien < citizen:
                work_atomvals[citizen_index] += 1

    atomvals_integer = Binv(exposet=work_atomvals).intval
    atomvals_sierpinski = int_to_sierpinski_row(exposet=work_atomvals)
    return Binv([self.root[atomvals_sierpinski.index(key & atomvals_integer)] for key in range(2 ** len(arg_atomvals_set))])

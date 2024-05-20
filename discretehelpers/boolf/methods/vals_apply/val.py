from discretehelpers.a import true_except

from discretehelpers.binv import Binv

from .ex import SarityMismatchError, UnexpectedArgumentError


def val(self, *args):

    true_except(len(args) == self.valency, SarityMismatchError)

    first_arg = args[0]
    case_single = type(first_arg) in [int, bool] and int(first_arg) in [0, 1]
    case_multiple = type(first_arg) in [list, Binv]
    true_except(case_single or case_multiple, UnexpectedArgumentError)

    if case_single:
        true_except(set(args).issubset({0, 1}), UnexpectedArgumentError)
        key = Binv(args).intval
        return self.root[key]

    if case_multiple:
        vals_list = []
        for i in range(len(first_arg)):
            args_i = [arg_list[i] for arg_list in args]
            vals_list.append(self.val(*args_i))
        return Binv(vals_list)

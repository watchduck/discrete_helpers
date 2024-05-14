from discretehelpers.a import logic_abs_increase, logic_abs, true_except

from discretehelpers.ex import ArgValueError


def spread_sigperm_to_sigvar(sigperm, spread):

    true_except(len(sigperm) == len(spread), ArgValueError)
    length = len(sigperm)

    perm = [logic_abs(_) for _ in sigperm]

    return [logic_abs_increase(sigperm[i], spread[perm[i]]) for i in range(length)]

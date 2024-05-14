from discretehelpers.a import int_to_weight, true_except

from discretehelpers.ex import ArgValueError


def index_to_evil(i):
    true_except(i >= 0, ArgValueError)
    index_depravity = int_to_weight(i) % 2
    return 2 * i + index_depravity


def index_to_odious(i):
    true_except(i >= 0, ArgValueError)
    index_depravity = int_to_weight(i) % 2
    negated_index_depravity = int(not index_depravity)
    return 2 * i + negated_index_depravity


def evil_to_index(evil):
    true_except(evil >= 0, ArgValueError)
    true_except(int_to_weight(evil) % 2 == 0, ArgValueError)
    return evil >> 1


def odious_to_index(odious):
    true_except(odious >= 0, ArgValueError)
    true_except(int_to_weight(odious) % 2 == 1, ArgValueError)
    return odious >> 1

from collections import defaultdict

from discretehelpers.a import true_except
from discretehelpers.ex import ArgTypeError


def inventory_dict(arg):

    type_arg = type(arg)
    true_except(type_arg in [list, dict, defaultdict], ArgTypeError)

    if type(arg) == defaultdict:
        arg = dict(arg)

    result = dict()

    if type_arg == list:

        values = sorted(set(arg))
        for value in values:
            result[value] = arg.count(value)

    else:

        arg_values = list(arg.values())
        values = sorted(set(arg_values))
        for value in values:
            result[value] = arg_values.count(value)

    return result

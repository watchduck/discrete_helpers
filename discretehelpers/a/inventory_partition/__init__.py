from collections import defaultdict

from discretehelpers.a import true_except
from discretehelpers.ex import ArgTypeError


def inventory_partition(arg):

    from discretehelpers.set_part import SetPart

    type_arg = type(arg)
    true_except(type_arg in [list, tuple, dict, defaultdict], ArgTypeError)

    if type(arg) == defaultdict:
        arg = dict(arg)

    if type_arg in [list, tuple]:

        domain = sorted(range(len(arg)))
        result = SetPart([], domain=domain)

        for key, value in enumerate(arg):
            result.add_label_to_element(key, value)

    else:

        domain = sorted(arg.keys())
        result = SetPart([], domain=domain)

        for key, value in arg.items():
            result.add_label_to_element(key, value)

    return result

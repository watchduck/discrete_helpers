from discretehelpers.a import walsh_function_to_index

from discretehelpers.ex import ArgValueError


def linear_to_walsh_and_oddness(arg, trust=False):

    from discretehelpers.binv import Binv
    from discretehelpers.boolf import Boolf

    arg_type = type(arg)

    if arg_type is Boolf:
        binv = arg.tt()
    elif arg_type is Binv:
        binv = arg
    elif arg_type in [str, list, tuple]:
        binv = Binv(arg)
    else:
        raise ArgValueError

    is_odd = int(binv[0])
    even_binv = ~binv if is_odd else binv
    walsh_index = walsh_function_to_index(even_binv, trust=trust)
    return walsh_index, is_odd


def linear_to_leader_and_quadrant(arg, trust=False):

    from discretehelpers.a import int_to_weight, evil_to_index, odious_to_index

    walsh_index, is_odd = linear_to_walsh_and_oddness(arg, trust)

    walsh_index_is_odious = int_to_weight(walsh_index) % 2
    is_odious = walsh_index_is_odious ^ is_odd  # depravity of the linear Boolean function
    quadrant = is_odd + 2 * is_odious

    leader_index = odious_to_index(walsh_index) if walsh_index_is_odious else evil_to_index(walsh_index)

    return leader_index, quadrant

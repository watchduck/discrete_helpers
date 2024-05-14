from discretehelpers.a import have, true_except, logic_abs, logic_negate, is_natural, logic_str

from discretehelpers.ex import ArgTypeError, ArgValueError


def logic_abs_increase(a, b, want_string=False):
    """
    :param a: the integer whose abs is to be increased by `b`
        (which means decreased, if `b` is negative)
    :param b: integer (can be negative, but only so negative, that the abs of the result sinks to 0)
    :param want_string: return string if true
    :return: integer with the same logical sign as `a` (i.e. natural or negative)
    """
    true_except(type(a) == int and type(b) == int and type(want_string) == bool, ArgTypeError)
    a_abs = logic_abs(a)
    result_abs = a_abs + b
    true_except(is_natural(result_abs), ArgValueError)
    result_value = ~result_abs if a < 0 else result_abs
    return logic_str(result_value) if want_string else result_value


def logic_abs_increase_vector(a, b, want_string=False):
    """
    :param a: vector of integers
    :param b: vector of integers (of the same length)
    :param want_string: return string if true
    :return: vector of resulting integers
    """
    true_except(len(a) == len(b), ArgValueError)
    length = len(a)
    result_vector = [logic_abs_increase(a[i], b[i], want_string) for i in range(length)]
    if not want_string:
        return result_vector
    else:
        return "[" + ', '.join(result_vector) + "]"

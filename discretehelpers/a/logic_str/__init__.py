from discretehelpers.a import logic_abs, true_except

from discretehelpers.ex import ArgTypeError


def logic_str(n):
    true_except(type(n) == int, ArgTypeError)
    abs_n = logic_abs(n)
    s = str(abs_n)
    return '~' + s if n < 0 else s


def logic_str_vector(vector):
    list_of_strings = [logic_str(_) for _ in vector]
    return "[" + ', '.join(list_of_strings) + "]"

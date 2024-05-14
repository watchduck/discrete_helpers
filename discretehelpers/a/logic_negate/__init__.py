from discretehelpers.a import have, true_except

from discretehelpers.ex import ArgComboError, ArgMismatchError, ArgValueError


def logic_negate(value, do_it=True, want_string=False):
    true_except(type(value) == int and do_it in [False, 0, '0', True, 1, '1'], ArgValueError)
    result_value = ~value if do_it else value
    if not want_string:
        return result_value
    else:
        from discretehelpers.a import logic_abs
        a = logic_abs(result_value)
        return '~' + str(a) if result_value < 0 else str(a)


def logic_negate_vector(values, where=None, which=None, want_string=False):
    """
    Return `values` with some `n` changed to `~n`, based on places in `where` or on values in `which`.
    Initial values may be negative. They will be changed, when their positive equivalents are in `which`.
    """

    if have(values) and have(where) and not have(which):
        case = 'where'
    elif have(values) and not have(where) and have(which):
        case = 'which'
    else:
        raise ArgComboError

    if case == 'where':
        true_except(len(values) == len(where), ArgMismatchError)
        true_except(set([int(_) for _ in where]).issubset({0, 1}), ArgValueError)
        if not want_string:
            return [~values[_] if where[_] else values[_] for _ in range(len(values))]
        else:
            list_of_strings = [
                logic_negate(values[_], want_string=True)
                if where[_]
                else logic_negate(values[_], do_it=False, want_string=True)
                for _ in range(len(values))
            ]
            return '[' + ", ".join(list_of_strings) + ']'
    elif case == 'which':
        true_except(all([_ >= 0 for _ in which]), ArgValueError)
        from discretehelpers.a import logic_abs_vector
        abs_values = logic_abs_vector(values)
        true_except(set(which).issubset(set(abs_values)), ArgMismatchError)
        if not want_string:
            return [~values[_] if abs_values[_] in which else values[_] for _ in range(len(values))]
        else:
            list_of_strings = [
                logic_negate(values[_], do_it=True, want_string=True)
                if abs_values[_] in which
                else logic_negate(values[_], do_it=False, want_string=True)
                for _ in range(len(values))
            ]
            return '[' + ", ".join(list_of_strings) + ']'

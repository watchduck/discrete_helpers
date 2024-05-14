from operator import __and__, __or__, __xor__

from discretehelpers.ex import ArgValueError


def multigrade_bitwise(integers, operator):

    vector = list(integers)

    if operator == 'and':
        op = __and__
    elif operator == 'or':
        op = __or__
    elif operator == 'xor':
        op = __xor__
    else:
        raise ArgValueError

    if len(vector) < 2:

        return vector

    else:

        current = vector[0]
        for i in range(1, len(vector)):
            entry = vector[i]
            current = op(current, entry)

        return current

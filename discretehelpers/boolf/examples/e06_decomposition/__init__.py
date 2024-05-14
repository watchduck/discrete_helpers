from discretehelpers.boolf import Boolf


_frame_ab = Boolf('1000', [2, 3])
_frame_c = Boolf('0010 0000', [0, 1, 3])
_frame_d = Boolf('1000 0000', [0, 1, 2])


def _formula(var_ab, var_c, var_d):
    ab = Boolf(var_ab, [0, 1])
    c = Boolf(var_c, [2])
    d = Boolf(var_d, [3])

    return (ab & _frame_ab) | (c & _frame_c) | (d & _frame_d)


kibime = _formula('1111', '11', '11')  # white

murife = _formula('1101', '01', '11')

menabe = _formula('0111', '11', '01')

tefabi = _formula('0101', '01', '01')

fobope = _formula('1111', '10', '11')  # not the same Euler shape

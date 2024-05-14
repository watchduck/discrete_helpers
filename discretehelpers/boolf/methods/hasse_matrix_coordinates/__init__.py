from discretehelpers.binv import Binv


def hasse_matrix_coordinates(self, arity=None):

    tt = self.tt(arity)

    length = len(tt)
    half_length = length // 2

    i = Binv(tt[0:half_length]).intval
    j = Binv(tt[half_length:length][::-1]).intval

    return i, j

from discretehelpers.boolf.a import mod_tt_neg
from discretehelpers.binv import Binv


def test():
    binv = Binv('0110 0000 0110 0000')
    assert mod_tt_neg(binv, 1) == Binv('1001 0000 1001 0000')
    assert mod_tt_neg(binv, 7) == Binv('0000 0110 0000 0110')

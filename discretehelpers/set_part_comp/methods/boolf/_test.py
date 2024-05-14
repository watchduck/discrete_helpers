from discretehelpers.boolf import Boolf
from ... import SetPartComp


def test():
    assert SetPartComp([[10, 20]]).boolf() == Boolf('1001', [10, 20])
    assert SetPartComp([[10, 20]], {(20, 30)}).boolf() == Boolf('0001 1000', [10, 20, 30])

from discretehelpers.boolf.examples import medusa, farofe, dukeli, faradi
from discretehelpers.boolf import Boolf


def test():
    assert Boolf('0') == Boolf('0')
    assert Boolf('1') == Boolf('1')
    assert Boolf('0001') == Boolf('0001')
    assert medusa.faction_minrep.zhe == 34945
    assert farofe.faction_minrep.zhe == 2209
    assert dukeli.faction_minrep.zhe == 2761
    assert faradi.faction_minrep.zhe == 43775

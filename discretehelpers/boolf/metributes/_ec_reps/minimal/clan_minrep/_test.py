from discretehelpers.boolf.examples import medusa, farofe, dukeli, bavori


def test():
    assert medusa.clan_minrep.zhe == 32777
    assert farofe.clan_minrep.zhe == 2209
    assert dukeli.clan_minrep.zhe == 2290
    assert bavori.clan_minrep.zhe == 104


def test_prototype():
    assert medusa._clan_minrep_prototype.zhe == 32777
    assert farofe._clan_minrep_prototype.zhe == 2209
    assert dukeli._clan_minrep_prototype.zhe == 2290
    assert bavori._clan_minrep_prototype.zhe == 104

from discretehelpers.boolf import Boolf


def test():
    assert Boolf(False).is_noble()
    assert Boolf(True).is_noble()

    assert Boolf(zhe=6).is_noble()
    assert Boolf(zhe=168).is_noble()
    assert Boolf(zhe=168).is_noble(3)
    assert Boolf(zhe=37150).is_noble()

    assert not Boolf(zhe=168).is_noble(4)

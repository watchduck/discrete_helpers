from discretehelpers.boolf.examples import selera, pelele, nemeke, foravo, bunese, safoko, kinide


def test():
    assert selera.is_symmetric
    assert pelele.is_symmetric
    assert nemeke.is_symmetric
    assert foravo.is_symmetric
    assert bunese.is_symmetric

    assert not safoko.is_symmetric
    assert not kinide.is_symmetric

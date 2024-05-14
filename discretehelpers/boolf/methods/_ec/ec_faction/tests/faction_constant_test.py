from discretehelpers.set_part import SetPart


def test():

    from discretehelpers.boolf import Boolf

    f = Boolf('0')
    t = Boolf('1')

    fa = f.ec_faction()
    fb = f.ec_faction(4)
    fc = f.ec_faction(4, suppress_abbreviation=True)

    ta = t.ec_faction()
    tb = t.ec_faction(4)
    tc = t.ec_faction(4, suppress_abbreviation=True)

    ####################################################################################################################

    block_list_24 = list(range(24))
    domain_24 = set(range(24))

    assert fa == ta == SetPart([], {0})
    assert fb == tb == SetPart([], {(0, 0)})
    assert fc == tc == SetPart([block_list_24], domain_24)

    ####################################################################################################################

    block_tuple_24 = tuple(range(24))

    assert fa.block_labels == {(0,): f}
    assert fb.block_labels == {((0, 0),): f}
    assert fc.block_labels == {block_tuple_24: f}

    assert ta.block_labels == {(0,): t}
    assert tb.block_labels == {((0, 0),): t}
    assert tc.block_labels == {block_tuple_24: t}

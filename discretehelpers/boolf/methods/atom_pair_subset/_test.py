from discretehelpers.boolf.examples import vumali


def test_true():
    assert vumali.atom_pair_subset(4, 3)  # E, D
    assert vumali.atom_pair_subset(7, 6)  # H, G


def test_false():
    assert not vumali.atom_pair_subset(3, 4)  # D, E
    assert not vumali.atom_pair_subset(6, 7)  # G, H
    assert not vumali.atom_pair_subset(0, 4)  # A, E
    assert not vumali.atom_pair_subset(4, 0)  # E, A

from discretehelpers.a import abbrev_testing as abbrev

from discretehelpers.perm import Perm

from discretehelpers.perm.ex import LengthTooSmallError, LengthMismatchPerilenError, NotPeriodicError


def test():

    a_fini = Perm([1, 0, 2,   4, 3, 5,   7, 6, 8,   10, 9, 11,   13, 12, 14])
    b_fini = Perm([0, 1, 4, 3, 2,   5, 6, 9, 8, 7,   10, 11, 14, 13, 12])

    a_peri = Perm([1, 0, 2], 3)
    b_peri = Perm([0, 1, 4, 3, 2], 5)

    ab_fini = a_fini * b_fini
    ba_fini = b_fini * a_fini

    ab_peri = a_peri * b_peri
    ba_peri = b_peri * a_peri

    ab_sequence = [1, 0, 3, 4, 2, 5, 7, 10, 8, 6, 9, 11, 14, 12, 13]
    ba_sequence = [1, 0, 4, 2, 3, 5, 9, 6, 8, 10, 7, 11, 13, 14, 12]

    ab_cycles = [[0, 1], [2, 3, 4], [6, 7, 10, 9], [12, 14, 13]]
    ba_cycles = [[0, 1], [2, 4, 3], [6, 9, 10, 7], [12, 13, 14]]

    assert ab_fini.perilen is None and ba_fini.perilen is None
    assert ab_peri.perilen == ba_peri.perilen == 15

    assert ab_fini.sequence() == ab_peri.sequence() == ab_sequence
    assert ba_fini.sequence() == ba_peri.sequence() == ba_sequence

    assert ab_fini.cycles == ab_peri.cycles == ab_peri.cycles_dynamic() == ab_peri.cycles_dynamic(15) == ab_cycles
    assert ba_fini.cycles == ba_peri.cycles == ba_peri.cycles_dynamic() == ba_peri.cycles_dynamic(15) == ba_cycles

    assert ab_peri.cycles_dynamic(30) == ab_cycles + [[_ + 15 for _ in cycle] for cycle in ab_cycles]
    assert ba_peri.cycles_dynamic(30) == ba_cycles + [[_ + 15 for _ in cycle] for cycle in ba_cycles]

    assert ab_fini.sequence(20) == ab_sequence + [15, 16, 17, 18, 19]

    assert ab_peri.sequence() == ab_peri.sequence(15) == ab_sequence
    assert ab_peri.sequence(30) == ab_sequence + [_ + 15 for _ in ab_sequence]

    assert ab_fini.inverse == ba_fini
    assert ab_peri.inverse == ba_peri

    abbrev(LengthTooSmallError, [
        lambda: ab_fini.sequence(14)
    ])
    abbrev(LengthMismatchPerilenError, [
        lambda: ab_peri.sequence(14),
        lambda: ab_peri.sequence(16),
        lambda: ab_peri.sequence(25),
        lambda: ab_peri.cycles_dynamic(14),
        lambda: ab_peri.cycles_dynamic(16),
        lambda: ab_peri.cycles_dynamic(25)
    ])
    abbrev(NotPeriodicError, [
        lambda: ab_fini.cycles_dynamic(30)  # This method works only for periodic permutations.
    ])

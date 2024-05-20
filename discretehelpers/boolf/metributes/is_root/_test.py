from discretehelpers.a import abbrev_testing as abbrev

from discretehelpers.boolf import Boolf

from discretehelpers.boolf.examples.e09_gap_variants_grids import manila


def test():
    abbrev(True, [
        Boolf('0').is_root,
        Boolf('1').is_root,
        Boolf('01').is_root,
        Boolf('10').is_root,
        Boolf('0001').is_root,
        Boolf('0110').is_root,
        manila.root_boolf.is_root
    ])

    abbrev(False, [
        Boolf('01', [1]).is_root,
        Boolf('10', [123]).is_root,
        Boolf('0001', [1, 2]).is_root,
        Boolf('0110', [123, 456]).is_root,
        manila.is_root
    ])

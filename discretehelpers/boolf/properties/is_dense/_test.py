from discretehelpers.a import abbrev_testing as abbrev

from discretehelpers.boolf import Boolf

from discretehelpers.boolf.examples.e09_gap_variants_grids import manila


def test():
    abbrev(True, [
        Boolf('0').is_dense,
        Boolf('1').is_dense,
        Boolf('01').is_dense,
        Boolf('10').is_dense,
        Boolf('0001').is_dense,
        Boolf('0110').is_dense,
        manila.dense_boolf.is_dense
    ])

    abbrev(False, [
        Boolf('01', [1]).is_dense,
        Boolf('10', [123]).is_dense,
        Boolf('0001', [1, 2]).is_dense,
        Boolf('0110', [123, 456]).is_dense,
        manila.is_dense
    ])

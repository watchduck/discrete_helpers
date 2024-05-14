from discretehelpers.a import abbrev_testing as abbrev

from discretehelpers.binv import Binv

from discretehelpers.boolf.examples.e02_val_apply_ec import kusaga_binv, kusaga, damela_binv, damela_spread, damela

from discretehelpers.boolf.methods.vals_apply.ex import SarityMismatchError, UnexpectedArgumentError


def test_kusaga():

    # first four digits
    # separate
    assert kusaga.val(0, 0, 0, 0)
    assert kusaga.val(1, 0, 0, 0)
    assert kusaga.val(0, 1, 0, 0)
    assert not kusaga.val(1, 1, 0, 0)
    # together
    assert kusaga.val([0, 1, 0, 1], [0, 0, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0]) \
           == kusaga.val(Binv('0101'), Binv('0011'), Binv('0000'), Binv('0000')) \
           == Binv('1110')

    # mat 0 and 2, row 0
    m0_r0 = kusaga.vals(0, 1, 2, 3)  # A B C D
    m2_r0 = kusaga.vals(0, 2, 1, 3)  # A C B D
    assert m0_r0 == m2_r0 == kusaga_binv == kusaga.dense_tt == kusaga.tt()

    # mat 0 and 2, row 3
    m0_r3 = kusaga.vals(~0, ~1, 2, 3)  # ~A ~B C D
    m2_r3 = kusaga.vals(~0, 2, ~1, 3)  # ~A C ~B D
    assert m0_r3 == m2_r3 == Binv('0111 0001 0010 0100')

    # mat 19 and 22, row 12
    m19_r12 = kusaga.vals(~2, 1, ~3, 0)  # ~C B ~D A
    m22_r12 = kusaga.vals(~2, ~3, 1, 0)  # ~C ~D B A
    assert m19_r12 == m22_r12 == Binv('0000 1001 1100 1010')


def test_damela():

    # mat 0 and 2, rows 0 and 14
    dense_m0_r0 = damela.vals(0, 1, 2, 3)  # A B C D
    dense_m2_r0 = damela.vals(0, 2, 1, 3)  # A C B D
    dense_m0_r14 = damela.vals(0, ~1, ~2, ~3)  # A ~B ~C ~D
    dense_m2_r14 = damela.vals(0, ~2, ~1, ~3)  # A ~C ~B ~D

    spread_m0_r0 = damela_spread.vals(0, 1, 2, 3)  # A B C D
    spread_m2_r0 = damela_spread.vals(0, 2, 1, 3)  # A C B D
    spread_m0_r14 = damela_spread.vals(0, ~1, ~2, ~3)  # A ~B ~C ~D
    spread_m2_r14 = damela_spread.vals(0, ~2, ~1, ~3)  # A ~C ~B ~D

    assert spread_m0_r0 == spread_m2_r0 == spread_m0_r14 == spread_m2_r14 == damela_binv == damela_spread.dense_tt \
           == dense_m0_r0 == dense_m2_r0 == dense_m0_r14 == dense_m2_r14 \
           == damela_binv == damela.dense_tt == damela.tt()  # but not `damela_spread.tt()`

    # mat 9 and 11, rows 3 and 4
    dense_m9_r3 = damela.vals(3, ~0, ~1, 2)  # D ~A ~B C
    dense_m11_r3 = damela.vals(3, ~1, ~0, 2)  # D ~B ~A C
    dense_m9_r4 = damela.vals(3, 0, 1, ~2)  # D A B ~C
    dense_m11_r4 = damela.vals(3, 1, 0, ~2)  # D B A ~C

    spread_m9_r3 = damela_spread.vals(3, ~0, ~1, 2)  # D ~A ~B C
    spread_m11_r3 = damela_spread.vals(3, ~1, ~0, 2)  # D ~B ~A C
    spread_m9_r4 = damela_spread.vals(3, 0, 1, ~2)  # D A B ~C
    spread_m11_r4 = damela_spread.vals(3, 1, 0, ~2)  # D B A ~C

    assert spread_m9_r3 == spread_m11_r3 == spread_m9_r4 == spread_m11_r4 == \
           dense_m9_r3 == dense_m11_r3 == dense_m9_r4 == dense_m11_r4 \
           == Binv('0111 1110 0001 1000')

    abbrev(SarityMismatchError, [
        lambda: damela_spread.val(),
        lambda: damela_spread.val([]),
        lambda: damela_spread.val(0, 0, 0),
        lambda: damela_spread.val(0, 0, 0, 0, 0),
        lambda: damela_spread.vals(),
        lambda: damela_spread.vals([]),
        lambda: damela_spread.vals([0, 0], [0, 0], [0, 0]),
        lambda: damela_spread.vals([0, 0], [0, 0], [0, 0], [0, 0], [0, 0])
    ])

    abbrev(UnexpectedArgumentError, [
        lambda: damela_spread.val(99, 99, 99, 99),
        lambda: damela_spread.vals(10, 11, 12, 13),
        lambda: damela_spread.vals(0, ~1, 2, ~5)
    ])

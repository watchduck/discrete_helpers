from discretehelpers.a import abbrev_testing as abbrev

from discretehelpers.binv import Binv

from discretehelpers.a._atompatterns import make_atompattern_gen, make_atompattern, make_atompatterns, atompattern_to_signed_index


def test_generator():
    a = make_atompattern_gen(0, 2, False)  # not negated
    b = make_atompattern_gen(~0, 2, True)  # twice negated
    assert list(a) == list(b) == [False, True, False, True]

    a = make_atompattern_gen(~0, 2, False)  # negated with tilda
    b = make_atompattern_gen(0, 2, True)  # negated with argument
    assert list(a) == list(b) == [True, False, True, False]

    assert [int(_) for _ in make_atompattern_gen(0, 3)] == [0, 1, 0, 1, 0, 1, 0, 1]
    assert [int(_) for _ in make_atompattern_gen(3, 4)] == [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]


def test_singular():
    # arity 1
    assert make_atompattern(0, 1) == Binv('01')

    assert make_atompattern(~0, 1) == Binv('10')

    # arity 2
    assert make_atompattern(0, 2) == Binv('0101')
    assert make_atompattern(1, 2) == make_atompattern(~1, 2, True) == Binv('0011')
    assert make_atompattern(~1, 2) == make_atompattern(1, 2, True) == Binv('1100')

    # arity 3
    assert make_atompattern(0, 3) == Binv('0101 0101')
    assert make_atompattern(1, 3) == Binv('0011 0011')
    assert make_atompattern(2, 3) == Binv('0000 1111')

    assert make_atompattern(~0, 3) == Binv('1010 1010')
    assert make_atompattern(~1, 3) == Binv('1100 1100')
    assert make_atompattern(~2, 3) == Binv('1111 0000')


def test_plural():

    assert make_atompatterns(1) == make_atompatterns([0]) == [Binv('01')]

    assert make_atompatterns(3) == make_atompatterns([0, 1, 2]) == [
        Binv('0101 0101'),
        Binv('0011 0011'),
        Binv('0000 1111')
    ]

    assert make_atompatterns([1, ~0, 2]) == [
        Binv('0011 0011'),
        Binv('1010 1010'),
        Binv('0000 1111')
    ]

    assert make_atompatterns([~3, ~2, 1, 0]) == [
        Binv('1111 1111 0000 0000'),
        Binv('1111 0000 1111 0000'),
        Binv('0011 0011 0011 0011'),
        Binv('0101 0101 0101 0101')
    ]


def test_raise():
    abbrev(AssertionError, [
        # arity needs to be positive
        lambda: make_atompattern(0, 0),
        lambda: make_atompatterns(0),

        # atomval too big for arity
        lambda: make_atompattern(1, 1),
        lambda: make_atompattern(2, 2),

        # input is not atompattern
        lambda: atompattern_to_signed_index(Binv('0')),
        lambda: atompattern_to_signed_index(Binv('0110 1001'))
    ])


def test_atompattern_to_signed_index():
    binv_0_1 = Binv('01')
    binv_0_2 = Binv('0101')
    binv_0_3 = Binv('0101 0101')
    binv_1_2 = Binv('0011')
    binv_1_3 = Binv('0011 0011')
    assert atompattern_to_signed_index( binv_0_1) == atompattern_to_signed_index( binv_0_2) == atompattern_to_signed_index( binv_0_3) == (0, False)
    assert atompattern_to_signed_index(~binv_0_1) == atompattern_to_signed_index(~binv_0_2) == atompattern_to_signed_index(~binv_0_3) == (0, True )
    assert atompattern_to_signed_index( binv_1_2) == atompattern_to_signed_index( binv_1_3) == (1, False)
    assert atompattern_to_signed_index(~binv_1_2) == atompattern_to_signed_index(~binv_1_3) == (1, True )

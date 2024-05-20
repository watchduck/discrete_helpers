from fractions import Fraction

from discretehelpers.a import abbrev_testing as abbrev

from discretehelpers.binv import Binv
from discretehelpers.boolf import Boolf

from discretehelpers.boolf.ex import SarityVectorMismatchError, AtomvalsNotUniqueError
from discretehelpers.boolf.examples import vinona, vinone, gilipi


def test_constant():
    yay = Boolf('1')
    nope = Boolf('0')
    assert yay.is_constant and nope.is_constant
    assert yay.valency == nope.valency == 0
    assert yay.atomvals == nope.atomvals == []
    assert yay.root == Binv('1')
    assert nope.root == Binv('0')
    assert yay == Boolf(True)
    assert nope == Boolf(False)


def test_unary():
    for i in range(3):
        assert Boolf(atom=i) == Boolf('01', [i])
        assert Boolf(atom=~i) == Boolf('10', [i])

    assert Boolf(atom=2) & Boolf(atom=~3) == Boolf('0100', [2, 3])
    assert Boolf('1110') & Boolf(atom=~2) & Boolf(atom=~3) == Boolf('1110 0000 0000 0000')


def test_cases():
    atoms_0_1 = [Boolf(atom=0), Boolf(atom=1)]
    assert Boolf('0001') == Boolf('0001', [0, 1]) == Boolf(multi_and=[0, 1])  == Boolf(multi_and=atoms_0_1)
    assert Boolf('0111') == Boolf('0111', [0, 1]) == Boolf(multi_or=[0, 1])   == Boolf(multi_or=atoms_0_1)
    assert Boolf('0110') == Boolf('0110', [0, 1]) == Boolf(multi_xor=[0, 1])  == Boolf(multi_xor=atoms_0_1)
    assert Boolf('1001') == Boolf('1001', [0, 1]) == Boolf(multi_xand=[0, 1]) == Boolf(multi_xand=atoms_0_1)

    assert Boolf( multi_and=[1, 2]).tt(3) == Binv('0000 0011')
    assert Boolf(  multi_or=[1, 2]).tt(3) == Binv('0011 1111')
    assert Boolf( multi_xor=[1, 2]).tt(3) == Binv('0011 1100')
    assert Boolf(multi_xand=[1, 2]).tt(3) == Binv('1100 0011')


def test_reorder_if_atomvals_not_asc():
    assert Boolf([0, 1, 0, 0], [1, 0]) == Boolf([0, 0, 1, 0], [0, 1])
    assert Boolf([0, 1, 0, 0], [5, 2]) == Boolf([0, 0, 1, 0], [2, 5])

    assert Boolf('0100 1011', [2, 0, 1]) == Boolf('0110 0101', [0, 1, 2])
    assert Boolf('0100 1011', [5, 1, 3]) == Boolf('0110 0101', [1, 3, 5])


def test_deflate():
    assert Boolf([1, 1, 1, 1]) == Boolf([1, 1, 1, 1], [77, 99]) == Boolf([1], []) == Boolf([True])
    assert Boolf([0, 0, 0, 0, 0, 0, 0, 0], [1, 3, 5]) == Boolf([0], []) == Boolf([False])

    assert Boolf('1010') == Boolf('10')
    assert Boolf('1100') == Boolf('10', [1])

    assert Boolf('0101 1010') == Boolf('0110', [0, 2])
    assert Boolf('0011 0011', [1000, 3000, 5000]) == Boolf('01', [3000])

    assert Boolf('0000 0000 0000 1111') == Boolf('0000 0011', [1, 2, 3]) == Boolf('0001', [2, 3])
    assert Boolf('0001 1000 0001 1000', [2, 5, 8, 99]) == Boolf('0001 1000', [2, 5, 8])

    assert vinone.is_inflated
    assert not vinona.is_inflated
    assert Boolf(vinone.root).root == vinona.root == Binv('1110')


def test_deflate_fullspots():
    boolf = Boolf(fullspots={0, 1, 2, 3, 4, 6}, atomvals=[10, 20, 40])
    assert boolf.fullspots == {0, 1, 2}
    assert boolf.atomvals == [10, 40]
    assert boolf.spread_vector == [10, 39]


def test_getitem():
    v1 = Binv('0100 1001 0101 1101')
    v2 = Binv('0110 1001 0110 1001')
    v3 = Binv('0011 0011 0011 0011')
    v4 = Binv('0000 0000 0000 0000')

    b1 = Boolf(v1)
    b2 = Boolf(v2)
    b3 = Boolf(v3)
    b4 = Boolf(v4)

    for i in range(16):
        assert b1[i] == v1[i]
        assert b2[i] == v2[i]
        assert b3[i] == v3[i]
        assert b4[i] == v4[i]


def test_fractions():
    boolf = Boolf('0')
    assert boolf.value_fract() == 0
    assert boolf.weight_fract == 0

    boolf = Boolf('10')
    assert boolf.value_fract() == Fraction(2, 3)
    assert boolf.weight_fract == 1/2

    boolf = Boolf('0001')
    assert boolf.value_fract() == Fraction(1, 15)
    assert boolf.weight_fract == 1/4

    boolf = Boolf('0111')
    assert boolf.value_fract() == Fraction(7, 15)
    assert boolf.weight_fract == 3/4

    boolf = Boolf('0110 1001')
    assert boolf.value_fract() == Fraction(7, 17)
    assert boolf.weight_fract == 1/2

    boolf = Boolf('1')
    assert boolf.value_fract() == 1
    assert boolf.weight_fract == 1


def test_raise():
    abbrev(SarityVectorMismatchError, [
        lambda: Boolf('1', [123]),
        lambda: Boolf('01', []),
        lambda: Boolf('01', [123, 456]),
        lambda: Boolf('0110', [123]),
        lambda: Boolf('0110', [123, 456, 789]),
    ])
    abbrev(AtomvalsNotUniqueError, [
        lambda: Boolf('01', [3, 3]),
        lambda: Boolf('0110', [3, 3, 5]),
    ])


def test_str():
    a = Boolf('0101 1010 0011 1000')
    assert str(a)  == "Boolf('0101 1010 0011 1000')"
    assert str(~a) == "Boolf('1010 0101 1100 0111')"
    assert eval(str(a)) == ~eval(str(~a)) == a

    b = Boolf('0101 1010 0011 1000', [1, 3, 5, 7])
    assert str(b)  == "Boolf('0101 1010 0011 1000', [1, 3, 5, 7])"
    assert str(~b) == "Boolf('1010 0101 1100 0111', [1, 3, 5, 7])"
    assert eval(str(b)) == ~eval(str(~b)) == b

    c = Boolf('0101 1010 0011 1000  1111 1010 0000 0000')
    assert str(c)  ==  "Boolf(fullspots=[1, 3, 4, 6, 10, 11, 12, 16, 17, 18, 19, 20, 22], arity=5)"
    assert str(~c) == "~Boolf(fullspots=[1, 3, 4, 6, 10, 11, 12, 16, 17, 18, 19, 20, 22], arity=5)"
    assert eval(str(c)) == ~eval(str(~c)) == c

    d = Boolf('0101 1010 0011 1000  1111 1010 0000 0000', [1, 3, 5, 7, 9])
    str_d = "Boolf(fullspots=[1, 3, 4, 6, 10, 11, 12, 16, 17, 18, 19, 20, 22], atomvals=[1, 3, 5, 7, 9])"
    assert str(d) ==  str_d
    assert str(~d) == '~' + str_d
    assert eval(str(d)) == ~eval(str(~d)) == d


def test_walsh_spectrum():
    assert Boolf(walsh_spectrum=[0]) == Boolf(False)
    assert Boolf(walsh_spectrum=[1]) == Boolf(True)
    assert Boolf(walsh_spectrum=[2, 0, 2, 0]) == Boolf(atom=~1)  # 1100
    assert Boolf(walsh_spectrum=[3, 1, 1, -1]) == vinona  # 1110
    assert Boolf(walsh_spectrum=[4, 2, 0, -2, 0, 2, 0, 2]) \
           == Boolf(walsh_spectrum=[8, 4, 0, -4, 0, 4, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0]) == gilipi  # 1010 0110

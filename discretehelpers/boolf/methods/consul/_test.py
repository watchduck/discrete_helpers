from discretehelpers.a import arity_to_walsh_matrix
from discretehelpers.boolf.examples import bamako
from discretehelpers.boolf import Boolf


sequence = [0, 0, 1, 1, 2, 2, 3, 3, 3, 3, 2, 2, 1, 1, 0, 0]


def test_sequence():
    for arity in range(3):
        for i in range(2 ** 2 ** arity):
            boolf = Boolf(i, arity=arity)
            entry = sequence[i]
            assert boolf.consul(arity) == entry
            assert boolf.consul_slow(arity) == entry


def test():

    mat_2 = arity_to_walsh_matrix(2)
    mat_3 = arity_to_walsh_matrix(3)
    mat_4 = arity_to_walsh_matrix(4)
    mat_5 = arity_to_walsh_matrix(5)
    mat_6 = arity_to_walsh_matrix(6)
    mat_7 = arity_to_walsh_matrix(7)

    assert bamako.consul(4) == bamako.consul_slow(4, prefab_matrix=mat_4) == 0
    assert bamako.consul(5) == bamako.consul_slow(5, prefab_matrix=mat_5) == 16
    assert bamako.consul(6) == bamako.consul_slow(6, prefab_matrix=mat_6) == 0
    assert bamako.consul(7) == bamako.consul_slow(7, prefab_matrix=mat_7) == 0
    assert [bamako.consul_weight(arity) for arity in [4, 5, 6, 7]] == [0, 1, 0, 0]

    boolf = Boolf('1001 0100')
    assert boolf.consul(3) == boolf.consul_slow(3, prefab_matrix=mat_3) == 6
    assert boolf.consul(4) == boolf.consul_slow(4, prefab_matrix=mat_4) == 8
    assert boolf.consul(5) == boolf.consul_slow(5, prefab_matrix=mat_5) == 0
    assert boolf.consul(6) == boolf.consul_slow(6, prefab_matrix=mat_6) == 0
    assert [boolf.consul_weight(_) for _ in [3, 4, 5, 6]] == [2, 1, 0, 0]

    boolf = Boolf('1010 0000')
    assert boolf.consul(3) == boolf.consul_slow(3, prefab_matrix=mat_3) == 2
    assert boolf.consul(4) == boolf.consul_slow(4, prefab_matrix=mat_4) == 0
    assert boolf.consul(5) == boolf.consul_slow(5, prefab_matrix=mat_5) == 0
    assert [boolf.consul_weight(_) for _ in [3, 4, 5]] == [1, 0, 0]

    boolf = Boolf('0001')
    assert boolf.consul(2) == boolf.consul_slow(2, prefab_matrix=mat_2) == 3
    assert boolf.consul(3) == boolf.consul_slow(3, prefab_matrix=mat_3) == 4
    assert boolf.consul(4) == boolf.consul_slow(4, prefab_matrix=mat_4) == 0
    assert boolf.consul(5) == boolf.consul_slow(5, prefab_matrix=mat_5) == 0
    assert [boolf.consul_weight(_) for _ in [2, 3, 4, 5]] == [2, 1, 0, 0]

    assert Boolf('0').consul() == Boolf('1').consul() == 0

from discretehelpers.boolf import Boolf


def test():

    expected_leader = Boolf(70, arity=3)
    assert expected_leader.leader(3) == expected_leader
    assert Boolf(71, arity=3).leader(3) == expected_leader
    assert Boolf(184, arity=3).leader(3) == expected_leader
    assert Boolf(185, arity=3).leader(3) == expected_leader

    expected_leader = Boolf(30, arity=3)
    assert expected_leader.leader(3) == expected_leader
    assert Boolf(31, arity=3).leader(3) == expected_leader
    assert Boolf(224, arity=3).leader(3) == expected_leader
    assert Boolf(225, arity=3).leader(3) == expected_leader

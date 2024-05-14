import pytest

from discretehelpers.boolf import Boolf

from discretehelpers.a import linear_to_walsh_and_oddness, linear_to_leader_and_quadrant


def test():
    assert Boolf('1011 0010').prefect_walsh_and_oddness == (5, False)
    assert Boolf('0111 0110').prefect_walsh_and_oddness == (7, True)


@pytest.mark.parametrize('tt', ['0', '1', '01', '10', '0110', '1001 0110 0110 1001'])
def test_linear(tt):
    boolf = Boolf(tt)
    assert boolf.prefect_walsh_and_oddness == linear_to_walsh_and_oddness(tt)
    assert boolf.prefect_leader_and_quadrant == linear_to_leader_and_quadrant(tt)

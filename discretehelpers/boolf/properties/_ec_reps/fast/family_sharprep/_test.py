import pytest

from discretehelpers.boolf import Boolf
from discretehelpers.boolf.examples import medusa, tabita, nitako, sopuda


@pytest.mark.parametrize('boolf', [medusa, tabita])
def test(boolf):
    rep = boolf.family_sharprep
    for boolf in boolf.ec_family().block_labels.values():
        assert boolf.family_sharprep == rep


@pytest.mark.parametrize('boolf', [nitako, sopuda])
def test_error(boolf):
    with pytest.raises(ValueError):
        boolf.family_sharprep


@pytest.mark.parametrize('atomvals', [(0, 1), (2, 5), (88, 99)])
def test_spread(atomvals):
    boolf = Boolf('0010', atomvals)
    assert boolf.family_sharprep == Boolf('1000', atomvals)

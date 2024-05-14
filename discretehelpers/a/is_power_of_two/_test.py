import pytest

from . import is_power_of_two


@pytest.mark.parametrize('val', [1, 2, 4, 8, 16, 32])
def test_true(val):
    assert is_power_of_two(val)


@pytest.mark.parametrize('val', [-4, -2, -1, 0, -.5, .5, 3, 5])
def test_false(val):
    assert not is_power_of_two(val)

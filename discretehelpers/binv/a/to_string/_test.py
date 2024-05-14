import pytest
from . import to_string


@pytest.mark.parametrize(
    'candidate',
    [[0, 1], (0, 1), [False, True], (False, True), '01'],
    ids=str
)
def test(candidate):
    assert to_string(candidate) == '01'

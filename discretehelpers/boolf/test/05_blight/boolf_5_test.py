import pytest

from discretehelpers.set_part_comp import SetPartComp
from discretehelpers.boolf import Boolf


array_any = [
    [
        Boolf('0001001010001100'),  # {3, 6, 8, 12, 13}
        Boolf('0110', [1, 4]),
        Boolf('00010010000000000000000010001100')  # {3, 6, 24, 28, 29}
    ], [  # like above, but with gaps
        Boolf('0001001010001100', [1, 3, 5, 7]),  # {3, 6, 8, 12, 13}
        Boolf('0110', [3, 9]),
        Boolf('00010010000000000000000010001100', [1, 3, 5, 7, 9])  # {3, 6, 24, 28, 29}
    ], [
        Boolf('0001001010001100'),  # {3, 6, 8, 12, 13}
        Boolf('1001', [0, 4]),
        Boolf('00000010100010000001000000000100')  # {6, 8, 12, 19, 29}
    ], [
        Boolf('0110'),  # {1, 2}
        Boolf('0110', [1, 2]),
        Boolf('00100100')  # {2, 5}
    ], [
        Boolf('0110'),
        Boolf('1001'),
        Boolf('0')  # because the bloat (0 equal 1) )contradicts the initial statement (0 complement 1)
    ]
]

last_example_fullspots = {1105, 1106, 1107, 1108, 1111, 1112, 1114, 1119, 1953, 1954, 1955, 1956, 1959, 1960, 1962, 1967, 2129, 2130, 2131, 2132, 2135, 2136, 2138, 2143, 2977, 2978, 2979, 2980, 2983, 2984, 2986, 2991}

array_bloatless = [
    [
        Boolf('0111001010000000'),  # {1, 2, 3, 6, 8}
        Boolf('0110', [1, 4]),
        Boolf('00110010000000000100000010000000')  # {2, 3, 6, 17, 24}
    ], [  # like above, but with gaps
        Boolf('0111001010000000', [1, 3, 5, 7]),  # {1, 2, 3, 6, 8}
        Boolf('0110', [3, 9]),
        Boolf('00110010000000000100000010000000', [1, 3, 5, 7, 9])  # {2, 3, 6, 17, 24}
    ], [
        Boolf('1011001110110100'),  # {0, 2, 3, 6, 7, 8, 10, 11, 13}
        Boolf('0010100000010100', [0, 1, 4, 5]),  # {2, 4, 11, 13}, (1 complement 4) and (0 equal 5)
        Boolf('0010001000100000100000001000000000010001000100000000000000000100')  # {2, 6, 10, 16, 24, 35, 39, 43, 61}
    ], [
        Boolf('01101110'),  # {1, 2, 4, 5, 6}
        Boolf('0110', [0, 3]),
        Boolf('0100010000101010')  # {1, 5, 10, 12, 14}
    ], [
        Boolf('1'),
        SetPartComp([[0, 2]], {(0, 1)}).boolf(),  # (0 complement 1) and (1 complement 2)
        Boolf('00100100')  # {2, 5}
    ], [  # like above, but with gaps
        Boolf('1'),
        SetPartComp([[1, 5]], {(1, 3)}).boolf(),  # (1 complement 3) and (3 complement 5)
        Boolf('00100100', [1, 3, 5])  # {2, 5}
    ], [
        Boolf('01110001'),
        Boolf('1'),
        Boolf('01110001')
    ], [
        Boolf('0111100110100001'),
        SetPartComp([[4, 6], [5, 7, 8, 9]], {(4, 5), (10, 11)}).boolf(),
        Boolf(fullspots=last_example_fullspots, atomvals=[_ for _ in range(12)])
    ], [  # like above, but with gaps
        Boolf('0111100110100001', [0, 10, 20, 30]),
        SetPartComp([[40, 60], [50, 70, 80, 90]], {(40, 50), (100, 110)}).boolf(),
        Boolf(fullspots=last_example_fullspots, atomvals=[10*_ for _ in range(12)])
    ]
]


@pytest.mark.parametrize('candidate', array_bloatless + array_any)
def test_any(candidate):
    # `component`: any boolf (possibly bloated)
    # `added_bloat`: bloat boolf to be added (possibly contradicting the component)
    # `merge`: expected conjunction of the two
    component, added_bloat, merge = candidate
    component_bloatless, component_bloat = component.bloatless_boolf, component.bloat_boolf
    assert component_bloatless & component_bloat == component

    merge_bloat = component_bloat & added_bloat  # conjunction of old and new bloat
    assert component_bloatless & merge_bloat == merge

    assert component & added_bloat == merge

    assert merge.bloatless_boolf & merge.bloat_boolf == merge


@pytest.mark.parametrize('candidate', array_bloatless)
def test_bloatless(candidate):
    # `bloatless`: boolf without bloat
    # `bloat`: bloat boolf not contradicting `bloatless`
    # `merge`: expected conjunction of the two
    bloatless, bloat, merge = candidate
    assert bloatless.bloat == SetPartComp()  # no bloat

    assert bloatless & bloat == merge
    assert merge.bloatless_boolf == bloatless
    assert merge.bloat_boolf == bloat

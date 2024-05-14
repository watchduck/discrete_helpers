import pytest

from discretehelpers.boolf.examples.e10_gap_variants_basiga import *


names = ['torova', 'kulika', 'dinado', 'giteli', 'doguva', 'kokabi', 'teloti', 'sarina', 'sarina', 'pamoda', 'futare', 'bitada', 'duvola', 'geteso']


@pytest.mark.parametrize('name', names)
def test_all_fullspots(name):
    boolf, fullspots = eval(name), eval(name + '_fs')
    assert boolf.fullspots == fullspots

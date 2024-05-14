from discretehelpers.boolf.examples import vumali


def test():

    assert vumali.bundles_pretty() == [['A', 'B', 'C', 'D', 'E'], ['F', 'G'], ['H']]

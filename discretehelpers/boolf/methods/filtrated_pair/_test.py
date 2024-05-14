from discretehelpers.boolf.examples import tinora


def test():

    assert tinora.filtrated_pair(1, 3) == '1101'  # B is superset of D
    assert tinora.filtrated_pair(3, 1) == '1011'  # D is subset of B

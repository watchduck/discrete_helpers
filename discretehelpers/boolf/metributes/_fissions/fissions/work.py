from discretehelpers.a import make_atompatterns, vector_zip_apart
from discretehelpers.boolf.a import flat_to_layered


def work(self):

    n = self.adicity
    assert n > 0  # constants can not be fissioned
    atompatterns = make_atompatterns(n)
    tt = self.tt()

    assert len(tt) == 2 ** n

    result_main = []
    result_layered = []

    for atompattern in atompatterns:
        a, b = vector_zip_apart(tt, atompattern)
        result_main.append([a, b])
        result_layered.append([
            flat_to_layered([int(_) for _ in a]),
            flat_to_layered([int(_) for _ in b])
        ])

    return result_main, result_layered

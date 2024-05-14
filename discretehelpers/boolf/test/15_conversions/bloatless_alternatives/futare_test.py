from discretehelpers.boolf.examples import futare


x = futare.bloatless_boolf                   # bloatless default     (B instead of E)
y = futare.filtrated_boolf([0, 4, 5, 6, 7])  # bloatless alternative (E instead of B)


def test_samples():
    assert x.apply(4, ~0, 5, 6, 7) == x.apply(7, ~5, 0, ~6, 4) == y
    assert y.apply(0, ~1, 5, 6, 7) == y.apply(7, 5, 0, ~6, ~1) == x

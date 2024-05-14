from discretehelpers.boolf.examples import tokosi


def test():
    assert tokosi.filtrated_pairs == {
        (0, 1): '1111',  # red, green
        (0, 2): '1111',  # red, blue
        (0, 3): '1111',  # red, brown
        (0, 4): '1111',  # red, orange
        (1, 2): '1111',  # green, blue
        (1, 3): '0110',  # green, brown   (complements)
        (1, 4): '0110',  # green, orange  (complements)
        (2, 3): '1111',  # blue, brown
        (2, 4): '1111',  # blue, orange
        (3, 4): '1001'  # brown, orange   (equal)
    }

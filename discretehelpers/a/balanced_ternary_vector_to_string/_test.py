from . import balanced_ternary_vector_to_string


def test():
    assert balanced_ternary_vector_to_string([-1, 0, 1, 0]) == '−0+0'

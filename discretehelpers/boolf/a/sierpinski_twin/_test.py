from discretehelpers.boolf.a import sierpinski_twin, vector_to_twin_gen
from discretehelpers.binv import Binv


def test():
    # column 0
    small_tt = '1001 0001 0000 0100'
    result = sierpinski_twin(small_tt, 0, 4)
    same_result = list(vector_to_twin_gen(small_tt, 4))
    assert result == same_result == [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0]
    assert Binv(result).pretty == '1110 1111 1110 1010'

    # column 3
    result = sierpinski_twin('1100', 3, 4)
    same_result = list(vector_to_twin_gen('1000 1000 0000 0000', 4))
    assert result == same_result
    assert Binv(result).pretty == '1111 0000 1111 0000'

    # column 8
    result = sierpinski_twin('0000 0100', 8, 4)
    same_result = list(vector_to_twin_gen('0000 0100 0000 0000', 4))
    assert result == same_result
    assert Binv(result).pretty == '0000 0101 0000 0101'

    # column 13
    result = sierpinski_twin('10', 13, 4)
    same_result = list(vector_to_twin_gen('1000 0000 0000 0000', 4))
    assert result == same_result
    assert Binv(result).pretty == '1111 1111 1111 1111'

from discretehelpers.perm import Perm
from discretehelpers.walsh_perm import WalshPerm


def test_gray_code():
    gray_seq = [0, 1, 3, 2, 6, 7, 5, 4, 12, 13, 15, 14, 10, 11, 9, 8]
    wp_gray = WalshPerm([1, 3, 6, 12])
    wp_gray_inv = WalshPerm([1, 3, 7, 15])
    p_gray = Perm(gray_seq, 16)
    assert wp_gray.sequence() == gray_seq
    assert wp_gray.inverse == wp_gray_inv
    assert p_gray == wp_gray
    assert p_gray.inverse == wp_gray.inverse == wp_gray_inv

    assert wp_gray.mapping == {2: 3, 3: 2, 4: 6, 5: 7, 6: 5, 7: 4, 8: 12, 9: 13, 10: 15, 11: 14, 12: 10, 13: 11, 14: 9, 15: 8}
    assert wp_gray.moved == set(range(2, 16))

    wp_gray_square = wp_gray**2
    assert wp_gray_square.inverse == wp_gray_square
    assert wp_gray_square.mapping == {4: 5, 5: 4, 6: 7, 7: 6, 8: 10, 9: 11, 10: 8, 11: 9, 12: 15, 13: 14, 14: 13, 15: 12}
    assert wp_gray_square.moved == set(range(4, 16))

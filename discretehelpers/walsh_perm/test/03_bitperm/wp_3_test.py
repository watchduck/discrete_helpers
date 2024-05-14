from discretehelpers.binv import Binv
from discretehelpers.perm import Perm
from discretehelpers.walsh_perm import WalshPerm


def test_bitperm():

    assert WalshPerm([2, 4, 1]) == Perm([0, 2, 4, 6, 1, 3, 5, 7], 8)  # 3
    assert WalshPerm([2, 4, 8, 1]) == Perm([0, 2, 4, 6, 8, 10, 12, 14, 1, 3, 5, 7, 9, 11, 13, 15], 16)  # 16

    p_3 = WalshPerm([4, 1, 2, 8])
    p_8 = WalshPerm([1, 8, 2, 4])
    p_17 = WalshPerm([8, 4, 1, 2])
    p_18 = WalshPerm([2, 4, 8, 1])
    p_7 = WalshPerm([2, 1, 8, 4])
    assert p_17 * p_18 == p_3
    assert p_18 * p_17 == p_8
    assert p_17 ** 2 == p_7
    assert p_7 ** -1 == p_7


def test_bitperm_vectors():

    p_3_sequence = [2, 0, 1]
    p_3 = Perm(p_3_sequence)

    wp_0_vector = [1, 2, 4]
    wp_3_vector = p_3.inverse.apply_on_vector(wp_0_vector)
    wp_4_vector = p_3.apply_on_vector(wp_0_vector)

    assert wp_3_vector == [4, 1, 2]
    assert wp_4_vector == [2, 4, 1]

    wp_3 = WalshPerm(wp_3_vector)
    wp_4 = WalshPerm(wp_4_vector)
    assert wp_3.inverse == wp_4

    wp_3_sequence = [0, 4, 1, 5, 2, 6, 3, 7]
    wp_4_sequence = [0, 2, 4, 6, 1, 3, 5, 7]
    assert wp_3.sequence() == wp_3_sequence
    assert wp_4.sequence() == wp_4_sequence

    fin_perm = p_3
    bit_perm = wp_4

    # reorder integers with finite permutation
    natural_order_binary = [Binv(intval=i, length=3).vector for i in range(8)]
    fin_permuted_binary = [fin_perm.apply_on_vector(v) for v in natural_order_binary]
    fin_permuted = [Binv(v).intval for v in fin_permuted_binary]

    # reorder integers with bit permutation
    bit_permuted = bit_perm.apply_on_vector(list(range(8)))

    assert fin_permuted == bit_permuted == wp_3_sequence

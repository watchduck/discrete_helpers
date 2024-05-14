from itertools import product


def reverse_cartesean_product(pairs):

    left_set = set()
    right_set = set()

    for left_item, right_item in pairs:
        left_set.add(left_item)
        right_set.add(right_item)

    assert sorted(product(left_set, right_set)) == sorted(pairs)

    return tuple(sorted(left_set)), tuple(sorted(right_set))

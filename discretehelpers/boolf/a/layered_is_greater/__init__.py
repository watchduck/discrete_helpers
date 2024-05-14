from discretehelpers.a import sort_together


def layered_is_greater(a, b):

    if a == b:
        return False

    a_sums = [sum(_) for _ in a]
    b_sums = [sum(_) for _ in b]

    a_sum = sum(a_sums)
    b_sum = sum(b_sums)

    sorted_lists = sort_together(
        [a_sum, b_sum],
        [a_sums, b_sums],
        [a, b]
    )

    return sorted_lists[2][1] == a

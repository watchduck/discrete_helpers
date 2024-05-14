from discretehelpers.a import int_to_weight, log_int
from discretehelpers.boolf.a import sierpinski_partition, vector_to_twin_gen


def sierpinski_twin(small_tt, sierpinski_index, big_arity):

    if type(small_tt) == str:
        small_tt = [int(_) for _ in small_tt.replace(' ', '')]

    weight = int_to_weight(sierpinski_index)
    small_arity = log_int(len(small_tt))
    assert weight + small_arity == big_arity

    small_twin = list(vector_to_twin_gen(small_tt, small_arity))

    if sierpinski_index == 0:
        return small_twin

    partition = sierpinski_partition(sierpinski_index, big_arity)
    blocks = partition.blocks
    assert len(blocks) == len(small_twin) == len(small_tt)

    big_length = 1 << big_arity  # 2 ** big_arity
    big_twin = [0] * big_length

    for small_key, val in enumerate(small_twin):
        block = blocks[small_key]
        for big_key in block:
            big_twin[big_key] = val

    return big_twin

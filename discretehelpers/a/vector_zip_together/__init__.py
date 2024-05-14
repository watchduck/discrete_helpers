def vector_zip_together(short_vectors, pattern):
    from discretehelpers.binv import Binv

    """
    :param short_vectors: entries in separate lists,             e.g. [[10, 12, 14], [11, 13], [15]]
    :param pattern: exposet to the list `short_vectors`,         e.g. [0, 1, 0, 1, 0, 2]
    :return: entries from `short_vectors` in one long vector,    e.g. [10, 11, 12, 13, 14, 15]
    inverse of vector_zip_apart
    """
    assert type(pattern) in [list, tuple, Binv]
    assert type(short_vectors) in [list, tuple]
    assert len(pattern) == sum(len(_) for _ in short_vectors)
    for short_vector in short_vectors:
        assert type(short_vector) in [list, tuple]

    # copy to avoid destruction by `pop`, also convert tuples to lists if needed
    _short_vectors = [list(_) for _ in short_vectors]

    result = []

    for i in pattern:
        result.append(
            _short_vectors[i].pop(0)
        )

    if type(short_vectors[0]) == tuple:
        return tuple(result)
    else:
        return result

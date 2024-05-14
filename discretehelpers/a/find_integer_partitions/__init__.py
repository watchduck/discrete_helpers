def find_integer_partitions(n):
    result = set()
    result.add((n, ))
    for x in range(1, n):
        for y in find_integer_partitions(n - x):
            result.add(tuple(sorted((x, ) + y)))
    return result

def int_to_factoradic(n):

    value = n
    divisor = 1
    result = []

    while value > 0:
        result.append(value % divisor)
        value //= divisor
        divisor += 1

    return tuple(result)

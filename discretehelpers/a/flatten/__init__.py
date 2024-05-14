def flatten(container):

    result = []

    for element in container:
        if type(element) in [list, tuple]:
            result += flatten(element)
        else:
            result.append(element)

    return tuple(result)

def sort_each_layer(layered):
    result = []
    for layer in layered:
        result.append(tuple(sorted(layer)))
    return tuple(result)

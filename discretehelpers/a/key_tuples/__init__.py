from discretehelpers.a import true_except

from .ex import ArgNotContainerError, ItemNotContainerFail, ItemEmptyContainerFail


def key_tuples(container, recursive=False):

    not_container_exception = ItemNotContainerFail if recursive else ArgNotContainerError
    true_except(type(container) in [list, dict], not_container_exception)

    container_empty = len(container) == 0

    if not recursive and container_empty:
        return []

    true_except(not container_empty, ItemEmptyContainerFail)  # non recursive case is caught before, so this must be recursive

    result = []

    container_key_val = enumerate(container) if type(container) == list else container.items()
    for key, val in container_key_val:
        try:                                               # assume that `val` is a non-empty container
            nested_tuples = key_tuples(val, True)
            for nested_tuple in nested_tuples:
                result.append(
                    tuple(
                        [key] + list(nested_tuple)
                    )
                )
        except (ItemNotContainerFail, ItemEmptyContainerFail):     # actually it is something else (weak exceptions used for control flow)
            result.append(
                (key, )
            )

    return result

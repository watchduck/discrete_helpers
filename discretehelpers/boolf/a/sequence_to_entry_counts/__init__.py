from collections import defaultdict


def sequence_to_entry_counts(sequence):

    element_to_count = defaultdict(int)

    result = []
    for element in sequence:
        result.append(element_to_count[element])
        element_to_count[element] += 1

    return result

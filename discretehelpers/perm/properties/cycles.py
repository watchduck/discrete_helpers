from functools import cached_property


@cached_property
def cycles(self):

    if self.neutral:
        self.cycles = []
        return []

    mapping = self.mapping.copy()
    result = []
    while len(mapping) > 0:
        cycle = []
        key = sorted(mapping.keys())[0]
        cycle.append(key)
        while True:
            old_key = key
            key = mapping[key]
            del mapping[old_key]
            if key not in cycle:
                cycle.append(key)
            else:
                result.append(cycle)
                break

    return result

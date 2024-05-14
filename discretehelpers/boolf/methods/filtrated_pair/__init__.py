def filtrated_pair(self, a, b):

    assert a < self.valency and b < self.valency

    if a < b:

        return self.filtrated_pairs[(a, b)]

    else:

        raw_result = self.filtrated_pairs[(b, a)]

        if raw_result in ['1011', '1101']:  # subset, superset
            return raw_result[::-1]
        else:
            return raw_result

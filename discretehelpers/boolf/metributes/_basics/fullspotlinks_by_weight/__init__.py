from itertools import product

from discretehelpers.a import have


# fullspotlinks by weight
@property
def fullspotlinks_by_weight(self):
    return self._fullspotlinks_by_weight


@fullspotlinks_by_weight.setter
def fullspotlinks_by_weight(self, val):
    self._fullspotlinks_by_weight = val


@fullspotlinks_by_weight.getter
def fullspotlinks_by_weight(self):
    if have(self._fullspotlinks_by_weight):
        return self._fullspotlinks_by_weight

    some_magic(self)
    return self.fullspotlinks_by_weight


# number of fullspotlinks
@property
def number_of_fullspotlinks(self):
    return self._number_of_fullspotlinks


@number_of_fullspotlinks.setter
def number_of_fullspotlinks(self, val):
    self._number_of_fullspotlinks = val


@number_of_fullspotlinks.getter
def number_of_fullspotlinks(self):
    if have(self._number_of_fullspotlinks):
        return self._number_of_fullspotlinks

    some_magic(self)
    return self.number_of_fullspotlinks


# function to create both metributes
def some_magic(self):

    weights = self.fullspot_weights

    result_main = dict()
    result_count = 0

    number_of_weights = len(weights)

    for i in range(number_of_weights - 1):
        if weights[i + 1] == weights[i] + 1:
            lower_weight = weights[i]
            upper_weight = lower_weight + 1

            lower_dict = self.fullspots_by_weight[lower_weight]
            upper_dict = self.fullspots_by_weight[upper_weight]

            lower_spotints = lower_dict.keys()
            upper_spotints = upper_dict.keys()

            candidate_pairs = product(lower_spotints, upper_spotints)

            actual_pairs = []
            for a, b in candidate_pairs:
                lower_atomkeys = set(lower_dict[a])
                upper_atomkeys = set(upper_dict[b])
                if lower_atomkeys.issubset(upper_atomkeys):
                    actual_pairs.append((a, b))
                    result_count += 1

            result_main[lower_weight] = sorted(actual_pairs)

    self.fullspotlinks_by_weight = result_main
    self.number_of_fullspotlinks = result_count

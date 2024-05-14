from itertools import product


def ec_clan_partitioned(self):

    negperm = self.ec_clan()
    negperm_set = set(negperm.block_labels.values())
    cardinality = len(negperm_set)

    ##############################################################################################

    set_of_perm_tuples = set()
    perm_sum = 0
    for boolf in negperm_set:
        perm = boolf.ec_faction()
        perm_tuple = tuple(sorted(perm.block_labels.values()))
        if perm_tuple not in set_of_perm_tuples:
            set_of_perm_tuples.add(perm_tuple)
            perm_sum += len(perm_tuple)
            if perm_sum == cardinality:
                break

    set_of_neg_tuples = set()
    neg_sum = 0
    for boolf in negperm_set:
        neg = boolf.ec_family()
        neg_tuple = tuple(sorted(neg.block_labels.values()))
        if neg_tuple not in set_of_neg_tuples:
            set_of_neg_tuples.add(neg_tuple)
            neg_sum += len(neg_tuple)
            if neg_sum == cardinality:
                break

    ##############################################################################################

    perm_min_to_set = dict()
    for perm_tuple in set_of_perm_tuples:
        perm_set = set()
        for boolf in perm_tuple:
            perm_set.add(boolf.zhe)
        perm_min_to_set[min(perm_set)] = perm_set

    neg_min_to_set = dict()
    for neg_tuple in set_of_neg_tuples:
        neg_set = set()
        for boolf in neg_tuple:
            neg_set.add(boolf.zhe)
        neg_min_to_set[min(neg_set)] = neg_set

    ##############################################################################################

    splinter_dict = dict()
    faction_reps = sorted(perm_min_to_set)
    family_reps = sorted(neg_min_to_set)
    for perm_min, neg_min in product(faction_reps, family_reps):
        perm_set = perm_min_to_set[perm_min]
        neg_set = neg_min_to_set[neg_min]
        splinter_dict[(perm_min, neg_min)] = sorted(perm_set.intersection(neg_set))

    ##############################################################################################

    faction_dict = dict()
    for perm_min in faction_reps:
        faction_dict[perm_min] = sorted(perm_min_to_set[perm_min])

    family_dict = dict()
    for neg_min in family_reps:
        family_dict[neg_min] = sorted(neg_min_to_set[neg_min])

    return faction_reps, family_reps, faction_dict, family_dict, splinter_dict

from collections import defaultdict


def ec_family_splinters(self):

    family = self.ec_family()

    raw_result = defaultdict(list)

    for boolf in family.block_labels.values():
        faction_rep = boolf.faction_minrep.zhe
        raw_result[faction_rep].append(boolf.zhe)

    result = dict()

    for faction_rep in sorted(raw_result.keys()):
        splinter_zhes = sorted(raw_result[faction_rep])
        splinter_rep = min(splinter_zhes)
        result[splinter_rep] = splinter_zhes

    return result

from collections import defaultdict


def ec_clan_factions(self, arity):

    clan = self.ec_clan(arity)

    raw_result = defaultdict(list)

    for boolf in clan.block_labels.values():
        faction_rep = boolf.faction_minrep.zhe
        raw_result[faction_rep].append(boolf.zhe)

    result = dict()

    for faction_rep in sorted(raw_result.keys()):
        faction_zhes = sorted(raw_result[faction_rep])
        assert faction_rep == min(faction_zhes)
        result[faction_rep] = faction_zhes

    return result

from discretehelpers.boolf.examples import menose

from ec_variables import family_dict, clan_3_dict, clan_4_dict_triples, clan_4_dict_pairs


def test_family():
    family = menose.ec_family()
    assert dict(family.block_labels) == family_dict


def test_clan_3():
    clan_3 = menose.ec_clan()
    assert dict(clan_3.block_labels) == clan_3_dict


def test_clan_4_triples():
    clan_4_triples = menose.ec_clan(4)
    assert dict(clan_4_triples.block_labels) == clan_4_dict_triples


def test_clan_4_pairs():
    clan_4_pairs = menose.ec_clan(4, suppress_abbreviation=True)
    assert dict(clan_4_pairs.block_labels) == clan_4_dict_pairs

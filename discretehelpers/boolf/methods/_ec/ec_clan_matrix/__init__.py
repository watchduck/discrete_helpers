import numpy as np
from collections import defaultdict

from discretehelpers.a import have, true_except, sort_together, sort_cols_together, multi_lcm
from discretehelpers.sig_perm import SigPerm
from discretehelpers.binv import Binv

from discretehelpers.boolf.ex import NotSpreadlessError


def dict_of_sets_to_dict_of_lists(dict_of_sets):
    dict_of_lists = dict()
    for key in sorted(dict_of_sets.keys()):
        dict_of_lists[key] = sorted(dict_of_sets[key])
    return dict_of_lists


def ec_clan_matrix(self):
    from discretehelpers.boolf import Boolf

    true_except(self.is_dense, NotSpreadlessError)
    
    clan = self.ec_clan()

    faction_reps, family_reps, faction_rep_to_row, family_rep_to_col, reps_to_raw_splinter = self.ec_clan_partitioned()

    #####################################################################################

    faction_rep_to_weight = dict()
    for faction_rep in faction_reps:
        row = faction_rep_to_row[faction_rep]
        weight = None
        for zhe in row:
            _weight = Binv(intval=zhe).weight
            if have(weight):
                assert _weight == weight
            else:
                weight = _weight
        faction_rep_to_weight[faction_rep] = weight

    #####################################################################################

    faction_rep_to_keyneg_exposet = defaultdict(set)
    family_rep_to_perm_exposet = defaultdict(set)
    zhe_to_keyneg_exposet = defaultdict(set)
    zhe_to_valneg_exposet = defaultdict(set)
    zhe_to_index_triples = defaultdict(set)

    for (faction_rep, family_rep), splinter in reps_to_raw_splinter.items():
        for zhe in splinter:
            boolf = Boolf(zhe=zhe)
            sigperm_pairs = clan.get_block_from_label(boolf)
            for valneg_index, perm_index in sigperm_pairs:
                sigperm = SigPerm(valneg_index=valneg_index, perm_index=perm_index)
                keyneg_index = sigperm.keyneg_index
                faction_rep_to_keyneg_exposet[faction_rep].add(keyneg_index)
                family_rep_to_perm_exposet[family_rep].add(perm_index)
                zhe_to_keyneg_exposet[zhe].add(keyneg_index)
                zhe_to_valneg_exposet[zhe].add(valneg_index)
                zhe_to_index_triples[zhe].add((keyneg_index, perm_index, valneg_index))

    #####################################################################################

    perm_exposet_to_family_rep = defaultdict(set)
    for family_rep, perm_exposet in family_rep_to_perm_exposet.items():
        perm_exposet_to_family_rep[tuple(sorted(perm_exposet))].add(family_rep)
    assert len(perm_exposet_to_family_rep.keys()) == len(perm_exposet_to_family_rep.values())

    # perm_exposets = []
    # family_rep_sets = []
    # for perm_exposet, family_rep_set in perm_exposet_to_family_rep.items():
    #     perm_exposets.append(perm_exposet)
    #     family_rep_sets.append(sorted(family_rep_set))
    # family_rep_sets, perm_exposets = sort_together(family_rep_sets, perm_exposets)

    #####################################################################################

    faction_splinter_sizes = dict()
    family_rep = min(family_reps)
    for faction_rep in faction_reps:
        faction_splinter_sizes[faction_rep] = len(reps_to_raw_splinter[(faction_rep, family_rep)])

    #####################################################################################

    faction_needs_reordering = set()
    for faction_rep in faction_reps:
        if faction_splinter_sizes[faction_rep] > 1:
            if Boolf(zhe=faction_rep).perm_symmetry_partition.intval:
                faction_needs_reordering.add(faction_rep)

    #####################################################################################

    rep_pair_to_splinter = reps_to_raw_splinter.copy()

    for family_rep in family_reps:
        symset_to_splinters = defaultdict(dict)  # implicitly initialize `faction_rep_to_splinter` for each symset
        for faction_rep in faction_reps:
            if faction_rep in faction_needs_reordering:
                splinter_zhes = reps_to_raw_splinter[(faction_rep, family_rep)]
                splinter_syms = [Boolf(zhe=_).perm_symmetry_partition.intval for _ in splinter_zhes]
                splinter_syms, splinter_zhes = sort_together(splinter_syms, splinter_zhes)
                symset_to_splinters[tuple(splinter_syms)][faction_rep] = splinter_zhes  # splinters are sorted based on symmetry

        for symset, faction_rep_to_splinter in symset_to_splinters.items():
            splinter_size = len(symset)
            number_of_splinters = len(faction_rep_to_splinter)
            splinter_rows = np.zeros([number_of_splinters, splinter_size], dtype=int)
            symset_faction_reps = sorted(faction_rep_to_splinter.keys())
            for i, symset_faction_rep in enumerate(symset_faction_reps):
                splinter_rows[i, :] = faction_rep_to_splinter[symset_faction_rep]
            splinter_rows = sort_cols_together(splinter_rows)[0]
            for i, splinter in enumerate(splinter_rows):
                symset_faction_rep = symset_faction_reps[i]
                rep_pair_to_splinter[(symset_faction_rep, family_rep)] = [int(_) for _ in splinter]

    #####################################################################################

    faction_rep_to_keyneg_exposet = dict_of_sets_to_dict_of_lists(faction_rep_to_keyneg_exposet)
    family_rep_to_perm_exposet = dict_of_sets_to_dict_of_lists(family_rep_to_perm_exposet)
    zhe_to_keyneg_exposet = dict_of_sets_to_dict_of_lists(zhe_to_keyneg_exposet)
    zhe_to_valneg_exposet = dict_of_sets_to_dict_of_lists(zhe_to_valneg_exposet)
    zhe_to_index_triples = dict_of_sets_to_dict_of_lists(zhe_to_index_triples)

    lcm_of_splinter_sizes = multi_lcm(faction_splinter_sizes.values())

    return faction_reps, family_reps, faction_rep_to_row, family_rep_to_col, rep_pair_to_splinter, \
        faction_splinter_sizes, lcm_of_splinter_sizes, \
        faction_rep_to_weight, faction_rep_to_keyneg_exposet, family_rep_to_perm_exposet, \
        zhe_to_keyneg_exposet, zhe_to_valneg_exposet, zhe_to_index_triples

from discretehelpers.binv import Binv

from .ex import *

from .a import reorder_if_atomvals_not_asc, deflate


class Boolf(object):

    def __init__(
        self, tt=None, atomvals=None, atom=None, arity=None, fullspots=None,
        multi_and=None, multi_or=None, multi_xor=None, multi_xand=None,
        zhe=None,  # Zhegalkin index,
        walsh_spectrum=None,
        skip_deflation=False
    ):

        self._doa = {  # dict of args
            'tt': tt, 'av': atomvals, 'atom': atom, 'arity': arity, 'fs': fullspots,
            'mu_a': multi_and, 'mu_o': multi_or, 'mu_xo': multi_xor, 'mu_xa': multi_xand,
            'zhe': zhe, 'ws': walsh_spectrum
        }
        self._doda = {  # dict of default args
            'sd': skip_deflation
        }

        self.is_constant = False
        self.is_inflated = False

        while True:
            if self._subinit_atom():
                break
            if self._subinit_truth_table():
                break
            if self._subinit_fullspots():
                break
            if self._subinit_zhe():
                break
            if self._subinit_walsh_spectrum():
                break
            if self._subinit_multi():
                break

        self.set_dummies()

    # end of init method ###############################################################################################

    def set_unary(self, arg):
        if arg < 0:
            atom = ~arg
            vector = Binv('10')
        else:
            atom = arg
            vector = Binv('01')
        self.root = vector
        self.atomvals = [atom]
        self.valency = 1
        self.adicity = atom + 1
        self.set_dummies()

    def set_constant(self, val):
        self.root = Binv([val])
        self.atomvals = []
        self.valency = 0
        self.adicity = 0
        self.is_constant = True
        self.set_dummies()

    def set_dummies(self):
        metribute_names = [
            'fullspotlinks_by_weight', 'number_of_fullspotlinks',
            'fullspots_by_weight', 'layered_fullspots', 'fullspot_weights',
            'faction_luckyrep', 'faction_luckyrep_binv', 'faction_luckyrep_fuzzyperm', 'faction_luckyrep_candidates',
            'fission_walsh_spectra', 'fission_walsh_spectra_abs', 'fission_walsh_spectra_layered', 'fission_walsh_spectra_layered_abs',
            'fission_walsh_spectra_zipped', 'fission_walsh_spectra_abs_zipped',
            'fissions', 'fissions_layered',
            'fissions_weight', 'fissions_weight_layered',
            'layered_tt', 'layered_weight',
            'splits_equality_blocks', 'splits_preferred_side',
            'splits_equal', 'splits_onesided',

            # obsolete
            'spot_atoms', 'spot_atoms_simple',
            'spotlinks_by_weight', 'number_of_spotlinks',
            'spots_by_weight', 'spot_weights',
            'diagonal_count'
        ]
        for name in metribute_names:
            setattr(self, '_' + name, None)

    # While the dummies are set within `__init__()`, this section is outside of it.
    from .metributes import complement, atomvals_integer, atomvals_sierpinski, weight_fract, fullspots, \
        splits, splits_overlap_counts, splits_equal, splits_onesided, splits_equality_blocks, \
        bloat, splits_preferred_side, number_of_distinct_splits, bloatless_boolf, bloat_boolf, bloatless_atomkeys_undeflated, \
        bundles, bundle_overlap_counts, bundle_grid_partitions, split_pairs_with_3_overlaps, gapless_boolf, \
        onesided_atomkeys, onesided_is_universe, blight, blight_boolf, blightless_atomkeys, blightless_boolf,\
        is_bloatless, is_blightless, bloatless_atomkeys_deflated, \
        filtrated_pairs, hypersplits, hypersplits_detailed, \
        is_bundle, is_root, atom_to_crossing_atoms, \
        root_boolf, blot, blot_boolf, is_blotless, \
        fullspot_atoms, fullspots_by_weight, fullspot_weights, layered_fullspots,\
        fullspotlinks_by_weight, number_of_fullspotlinks, spread_vector, \
        zhe, \
        layered_tt, layered_weight, is_symmetric, \
        hypersplits_potential_cores, symmetric_spots, perm_symmetry_partition, \
        family_malerep, family_minrep, faction_minrep, clan_minrep, _clan_minrep_prototype, \
        prefect_tt, prefect_boolf, prefect_walsh_and_oddness, prefect_leader_and_quadrant, \
        fissions, fissions_layered, fissions_weight, fissions_weight_layered, \
        fission_walsh_spectra, fission_walsh_spectra_abs, fission_walsh_spectra_layered, fission_walsh_spectra_layered_abs, \
        fission_walsh_spectra_zipped, fission_walsh_spectra_abs_zipped, \
        is_odd, is_odious, is_ugly, is_male, family_is_self_complementary, \
        is_linear, quadrant, reverse

    from .subinit_methods import _subinit_atom, _subinit_truth_table, _subinit_fullspots, _subinit_zhe, \
        _subinit_walsh_spectrum, _subinit_multi

    from .methods.bitwise import __and__, __or__, __xor__, bitwise_lt, bitwise_gt, bitwise_le, bitwise_ge, __invert__
    from .methods.str import __str__, __repr__, __hash__, __lt__, __gt__, __le__, __ge__
    from .methods.tt import tt
    from .methods.vals_apply import val, vals, apply, apply_sigperm
    from .methods.value_fract import value_fract
    from .methods._ec import (
        ec_family, ec_faction, ec_clan,
        ec_clan_partitioned, ec_clan_matrix, ec_clan_matrix_wiki,
        ec_family_splinters, ec_clan_factions
    )
    from .methods.bloatless_spotint import bloatless_spotint
    from .methods.blightless_spotint import blightless_spotint
    from .methods.inflated_fullspots import inflated_fullspots
    from .methods.filtrated_boolf import filtrated_boolf
    from .methods.wiki_table_row import wiki_table_row
    from .methods.atom_pair_subset import atom_pair_subset
    from .methods.atom_pair_intersect import atom_pair_intersect
    from .methods.atom_pair_crossing import atom_pair_crossing
    from .methods.atom_border_in_atom_side import atom_border_in_atom_side
    from .methods.diagonal_adjacency_matrix import diagonal_adjacency_matrix
    from .methods.splits_combined import splits_combined
    from .methods._pretty.filtrated_pairs_pretty import filtrated_pairs_pretty
    from .methods._pretty.fullspot_atoms_pretty import fullspot_atoms_pretty
    from .methods._pretty.fullspotlinks_by_atom_pretty import fullspotlinks_by_atom_pretty
    from .methods._pretty.bundles_pretty import bundles_pretty
    from .methods._pretty.hypersplits_pretty import hypersplits_pretty
    from .methods._pretty.hypersplits_potential_cores_pretty import hypersplits_potential_cores_pretty
    from .methods.filtrated_pair import filtrated_pair
    from .methods.find_segments import find_segments
    from .methods.walsh_spectrum import walsh_spectrum, walsh_spectrum_layered, walsh_spectrum_abs, walsh_spectrum_abs_layered
    from .methods.consul import consul_weight, consul, consul_slow
    from .methods.hasse_matrix_coordinates import hasse_matrix_coordinates
    from .methods.walsh_distances import walsh_distances
    from .methods._hyperfission import hyperfission, hyperfission_walsh_spectra, \
        hyperfission_walsh_spectra_abs, hyperfission_walsh_spectra_layered_abs, \
        hyperfission_walsh_spectra_zipped, hyperfission_walsh_spectra_labeled
    from .methods._patron import patron_int, patron_index, patron_boolf, \
        patron_royal, patron_quadrant, patron_king_index_and_quadrant
    from .methods.twin import twin
    from .methods.noble_quadrant import noble_quadrant
    from .methods.is_noble import is_noble
    from .methods._foibles import is_sharp, is_acute, is_rude, is_rough, is_solid
    from .methods._quadrant_extensions import weight_quadrant, acute_quadrant, octant
    from .methods.leader import leader

    def __getitem__(self, key):
        key = key & self.atomvals_integer
        key = self.atomvals_sierpinski.index(key)
        return self.root[key]

    def __eq__(self, other):
        return self.root == other.root and self.atomvals == other.atomvals

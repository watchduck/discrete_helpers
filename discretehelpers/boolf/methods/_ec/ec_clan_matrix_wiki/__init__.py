import numpy as np
from collections import defaultdict

from discretehelpers.binv import Binv
from discretehelpers.sig_perm import SigPerm
from discretehelpers.a import have, sort_together, logic_abs


def index_triples_to_valneg_html(keyneg_exposet, valneg_exposet, index_triples, arity):
    keyneg_weights = [Binv(intval=_).weight for _ in keyneg_exposet]
    keyneg_weights, keyneg_exposet = sort_together(keyneg_weights, keyneg_exposet)

    valneg_weights = [Binv(intval=_).weight for _ in valneg_exposet]
    valneg_weights, valneg_exposet = sort_together(valneg_weights, valneg_exposet)

    ##############

    rows_with_border = []
    last_weight = None
    for i, weight in enumerate(keyneg_weights):
        if have(last_weight) and weight != last_weight:
            rows_with_border.append(i)
        last_weight = weight

    cols_with_border = []
    last_weight = None
    for j, weight in enumerate(valneg_weights):
        if have(last_weight) and weight != last_weight:
            cols_with_border.append(j)
        last_weight = weight

    ##############

    height = len(keyneg_exposet)
    width = len(valneg_exposet)
    matrix = np.zeros([height, width], dtype=object)
    matrix[:] = None

    for keyneg_index, perm_index, valneg_index in index_triples:
        i = keyneg_exposet.index(keyneg_index)
        j = valneg_exposet.index(valneg_index)
        if have(matrix[i, j]):
            matrix[i, j].add(perm_index)
        else:
            matrix[i, j] = {perm_index}

    ##############

    html_icons = '<span class="number-icons">'
    html_table_header = '<tr class="top-labels"><th class="left-label"></th>'
    for j, valneg_index in enumerate(valneg_exposet):
        col_has_border = j in cols_with_border
        icon_separator = '[[File:1x1.png|2px|link=]]' if col_has_border else ''
        html_icons += f'{icon_separator}[[File:Cube vertex number {valneg_index}.svg|20px|link=]]'
        border_class = ' class="border-left"' if col_has_border else ''
        html_table_header += f'<th{border_class}>[[File:Cube vertex number {valneg_index}.svg|20px|link=]]</th>'
    html_icons += '</span>'
    html_table_header += '</tr>'

    html_table_body = ''
    for i, keyneg_index in enumerate(keyneg_exposet):
        row_has_border = i in rows_with_border
        border_class = ' class="border-top"' if row_has_border else ''
        html_table_body += f'<tr{border_class}><th class="left-label">[[File:Cube vertex number {keyneg_index} in square.svg|20px|link=]]</th>'
        for j, valneg_index in enumerate(valneg_exposet):
            col_has_border = j in cols_with_border
            border_class = ' class="border-left"' if col_has_border else ''
            html_table_body += f'<td{border_class}>'
            if have(matrix[i, j]):
                perm_exposet = sorted(matrix[i, j])
                for p, perm_index in enumerate(perm_exposet):
                    br = '<br>' if p < len(perm_exposet) - 1 else ''
                    perm_icon = f'[[File:Finite permutation number {perm_index}.svg|20px|link=]]'
                    sigperm_sequence_raw = SigPerm(pair=(valneg_index, perm_index)).sequence(arity)
                    sigperm_sequence_html = '<span class="sequence">('
                    for sequence_key, sequence_entry_raw in enumerate(sigperm_sequence_raw):
                        negator_class = ' negated' if sequence_entry_raw < 0 else ''
                        comma = ', ' if sequence_key < len(sigperm_sequence_raw) - 1 else ''
                        sequence_entry_abs = logic_abs(sequence_entry_raw)
                        sigperm_sequence_html += f'<span class="entry{negator_class}">{sequence_entry_abs}</span>{comma}'
                    sigperm_sequence_html += ')</span>'
                    html_table_body += f'<span class="icon-and-sequence">{perm_icon}{sigperm_sequence_html}</span>{br}'
            html_table_body += '</td>'
        html_table_body += '</tr>'

    html_table = f'<table class="valneg-hover">{html_table_header}{html_table_body}</table>'
    return f'<div class="valneg-wrapper">{html_icons}{html_table}</div>'

########################################################################################################################


def ec_clan_matrix_wiki(self):
    from discretehelpers.boolf import Boolf

    def keyneg_table(_faction_rep):
        weight_row = '<tr class="weights">'
        index_row = '<tr class="indices">'
        _keyneg_exposet = faction_rep_to_keyneg_exposet[_faction_rep]
        weight_to_exposet = defaultdict(set)
        for _keyneg_index in _keyneg_exposet:
            weight_to_exposet[Binv(intval=_keyneg_index).weight].add(_keyneg_index)
        weights = sorted(weight_to_exposet.keys())
        for weight in weights:
            _keyneg_exposet = sorted(weight_to_exposet[weight])
            weight_row += f'<td>{weight}</td>'
            index_row += f'<td><span class="number-icons">'
            for _keyneg_index in _keyneg_exposet:
                index_row += f'[[File:Cube vertex number {_keyneg_index} in square.svg|25px]]'
            index_row += '</span></td>'
        weight_row += '</tr>'
        index_row += '</tr>'
        table = f'<table class="keyneg-indices">{weight_row}{index_row}</table>'
        weights_str = ''.join([str(_) for _ in weights])
        sortkey = f'<span class="invisible-sortkey">&{sum(weights)}_{weights_str}</span>'
        return f'{sortkey}{table}'

    #####################################################################################

    def print_cell(_faction_rep, _zhe, cell_has_border):
        zhe_binary = Binv(intval=_zhe, length=2 ** self.valency).pretty
        boolf = Boolf(zhe=_zhe)
        tt_binary = boolf.tt().pretty

        if self.adicity == 3:
            venn_string = f'[[File:Venn {tt_binary}.svg|25px]]<br>'
        elif self.adicity == 2:
            venn_string = f'[[File:Venn{tt_binary}.svg|25px]]<br>'
        else:
            venn_string = ''

        index_triples = zhe_to_index_triples[_zhe]
        cell_is_base = (0, 0, 0) in index_triples
        cell_classes = {
            (False, False): '',
            (False, True): 'class="base"',
            (True, False): 'class="border"',
            (True, True): 'class="border base"'
        }[(cell_has_border, cell_is_base)]
        family_rep_class = ' neg-ec-min' if _zhe in family_reps else ''
        faction_rep_class = ' perm-ec-min' if _zhe in faction_reps else ''

        splinter_size = faction_splinter_sizes[_faction_rep]
        colspan = lcm_of_splinter_sizes // splinter_size

        cell_string = f'|colspan="{colspan}" {cell_classes}|{venn_string} <abbr class="zhegalkin{family_rep_class}{faction_rep_class}" title="{zhe_binary}&#10;{tt_binary}">{_zhe}</abbr>'

        cell_string += index_triples_to_valneg_html(
            zhe_to_keyneg_exposet[_zhe], zhe_to_valneg_exposet[_zhe], index_triples, self.adicity
        )

        print(cell_string)

    #####################################################################################

    faction_reps, family_reps, faction_rep_to_row, family_rep_to_col, rep_pair_to_splinter, \
        faction_splinter_sizes, lcm_of_splinter_sizes, \
        faction_rep_to_weight, faction_rep_to_keyneg_exposet, family_rep_to_perm_exposet, \
        zhe_to_keyneg_exposet, zhe_to_valneg_exposet, zhe_to_index_triples = self.ec_clan_matrix()

    #####################################################################################

    print('<templatestyles src="Studies of Euler diagrams/NP tables/style.css" />')
    print('{| class="wikitable sortable np" style="text-align: center;"\n|-')
    print('! <abbr class="hint" title="binary weight of the Zhegalkin indices in that row">W</abbr>')
    print('! <abbr class="hint" title="cardinality of the permutation equivalence class&#10;(number of different functions in that row)">C</abbr>')
    print('!')
    print('!')

    for family_rep in family_reps:
        perm_exposet = family_rep_to_perm_exposet[family_rep]
        _s = f'!colspan="{lcm_of_splinter_sizes}" class="unsortable border"| <span class="number-icons">'
        for perm_index in perm_exposet:
            _s += f'[[File:Finite permutation number {perm_index}.svg|25px]]'
        _s += f'</span><br><span class="neg-ec-min ec-min-side">{family_rep}</span>'
        print(_s)

    for faction_rep in faction_reps:
        cardinality = faction_splinter_sizes[faction_rep] * len(family_reps)
        print(f'|-')
        print(f'|class="zhegalkin-weight"| {faction_rep_to_weight[faction_rep]}')
        print(f'|class="cardinality"| {cardinality}')
        print(f'|class="perm-ec-min ec-min-side"| {faction_rep}')
        print(f'! {keyneg_table(faction_rep)}')
        for family_rep in family_reps:
            splinter = rep_pair_to_splinter[(faction_rep, family_rep)]
            for i, zhe in enumerate(splinter):
                cell_has_border = i == len(splinter) - 1
                print_cell(faction_rep, zhe, cell_has_border)

    if self.valency == 4:
        arity_suffix = '; 4-ary'
    else:
        arity_suffix = ''
    print('|}' + f'<noinclude>[[Category:Studies of Euler diagrams; templates; NP tables{arity_suffix}]]</noinclude>')

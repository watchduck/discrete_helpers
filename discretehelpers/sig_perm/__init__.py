import numpy as np

from discretehelpers.a import true_except, have, have_only, logic_abs, logic_negate
from discretehelpers.sig_perm.a import schoute_to_finite_inverse

from discretehelpers.binv import Binv
from discretehelpers.perm import Perm

from discretehelpers.ex import ArgComboError, ArgValueError

from .a import matrix_to_sequence, sequence_to_matrix


class SigPerm(Perm):

    def __init__(
        self, 
        valneg=None, valneg_index=None,
        keyneg=None, keyneg_index=None,
        perm=None, perm_index=None,
        pair=None,
        sequence=None, matrix=None,
        schoute_perm=None,
        trusted_rev_colex_perms=None
    ):

        all_args = [
            valneg, valneg_index, keyneg, keyneg_index, perm, perm_index, pair,
            sequence, matrix, schoute_perm, trusted_rev_colex_perms
        ]

        if have(keyneg):
            if type(keyneg) in [list, tuple]:
                keyneg = Binv(keyneg)
            elif type(keyneg) is set:
                keyneg = Binv(exposet=keyneg)

        if have(valneg):
            if type(valneg) in [list, tuple]:
                valneg = Binv(valneg)
            elif type(valneg) is set:
                valneg = Binv(exposet=valneg)

        if have(perm):
            if type(perm) in [list, tuple]:
                perm = Perm(perm)

        if have_only([pair], all_args):
            valneg_index, perm_index = pair

        if have(valneg_index):
            valneg = Binv(intval=valneg_index)

        if have(keyneg_index):
            keyneg = Binv(intval=keyneg_index)

        if have(perm_index):
            from discretehelpers.a import int_to_perm
            perm = int_to_perm(perm_index, trusted_rev_colex_perms)  # second argument can remain `None`

        ###################################################################################################

        if have(valneg) and have(perm):
            case = 'valneg_perm'
        elif have(keyneg) and have(perm):
            length = max(keyneg.required_length, perm.length)
            sequence = []
            for key in range(length):
                perm_val = perm[key]
                do_negate = keyneg.has_index(key)
                sigperm_val = logic_negate(perm_val, do_it=do_negate)
                sequence.append(sigperm_val)
            case = 'sequence'
        elif have(sequence):
            case = 'sequence'
        elif have(matrix):
            sequence = matrix_to_sequence(matrix)
            case = 'sequence'
        elif have(schoute_perm):
            inverse_sequence = schoute_to_finite_inverse(schoute_perm)
            matrix = sequence_to_matrix(sequence=inverse_sequence, inverse=True)
            sequence = matrix_to_sequence(matrix)
            case = 'sequence'
        else:
            raise ArgComboError

        ###################################################################################################

        if case == 'valneg_perm':

            if type(valneg) == Binv:
                raw_binv = valneg
            elif type(valneg) == set:
                raw_binv = Binv(exposet=valneg)
            elif type(valneg) in [str, list, tuple]:
                raw_binv = Binv(vector=valneg)

            self.perm = perm if type(perm) is Perm else Perm(perm)

        elif case == 'sequence':

            natural_sequence = [logic_abs(_) for _ in sequence]
            self.perm = Perm(natural_sequence)
            negator_exposet = [~_ for _ in sequence if _ < 0]
            raw_binv = Binv(exposet=negator_exposet)

        self.length = max(raw_binv.required_length, self.perm.length)
        missing_length = self.length - raw_binv.length
        self.binv = Binv(raw_binv.vector + [False] * missing_length)

        self.unsigned = self.binv.intval == 0
        self.unmoved = self.perm.neutral
        self.neutral = self.unsigned and self.unmoved

    def __getitem__(self, i):
        return self.sequence_minimal[i]

    def __eq__(self, other):
        true_except(isinstance(other, SigPerm) or isinstance(other, Perm), ValueError)
        if self.neutral and other.neutral:
            return True
        if isinstance(other, SigPerm):
            return self.perm == other.perm and self.binv == other.binv
        if isinstance(other, Perm):
            if self.binv.intval != 0:
                return False
            return self.perm == other

    def __str__(self):
        return f'SigPerm(sequence={self.sequence_string()})'

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return hash(self.__str__())

    def __mul__(self, other):  # a * b means a after b (function composition)
        size = max(self.length, other.length)
        matrix = np.dot(self.matrix(size), other.matrix(size))
        return SigPerm(matrix=matrix)

    def __pow__(self, exponent):
        pass

    from .metributes import inverse, sequence_minimal, \
        keyneg_index, valneg_index, perm_index, pair

    def sequence(self, length=None):
        if have(length):
            true_except(length >= self.length, ValueError)
        else:
            length = self.length
        return self.sequence_minimal + list(range(self.length, length))

    def sequence_string(self, length=None, round_parentheses=False):
        string_entries = []
        for signed_entry in self.sequence(length):
            natural_entry = logic_abs(signed_entry)
            s = '~' if signed_entry < 0 else ''
            s += str(natural_entry)
            string_entries.append(s)
        result = '[' + ', '.join(string_entries) + ']'
        if round_parentheses:
            result = result.replace('[', '(').replace(']', ')')
        return result

    def matrix(self, size=None):
        if have(size):
            true_except(size >= self.length, ValueError)
        else:
            size = self.length
        return sequence_to_matrix(self.sequence(size))

    def apply_on_vector(self, vector):
        arg_type = type(vector)
        length = len(vector)
        inverse_sequence = self.inverse.sequence(length)
        result_vector = []
        for signed_entry in inverse_sequence:
            natural_entry = logic_abs(signed_entry)
            v_raw = vector[natural_entry]
            v = ~v_raw if signed_entry < 0 else v_raw  # The negation with tilda is correct.
            result_vector.append(v)
        return arg_type(result_vector)

    def apply_on_natural_number(self, n):
        binv = Binv(intval=n, minimal_length=self.length)
        old_vector = binv.vector
        new_vector = [_ % 2 for _ in self.apply_on_vector(old_vector)]
        return Binv(new_vector).intval

from discretehelpers.a import true_except

from discretehelpers.binv import Binv

from .ex import BlightMismatchError


def blightless_spotint(self, spotint):

    bloatless_spotint = self.bloatless_spotint(spotint)
    bloatless_valency = len(self.bloatless_atomkeys_undeflated)
    bloatless_vector = Binv(intval=bloatless_spotint, length=bloatless_valency).vector

    blightless_vector = []
    for i in range(bloatless_valency):
        atomkey = self.bloatless_atomkeys_undeflated[i]
        truth_value = bloatless_vector[i]
        if atomkey in self.blightless_atomkeys:
            blightless_vector.append(truth_value)
        else:
            # just check, if the truth value matches the information in `blight`
            if atomkey in self.onesided_atomkeys:
                true_except(
                    self.blight.are_equal(-1, atomkey) == truth_value,  # iff this set is the universe, the respective binary digit is 1
                    BlightMismatchError
                )

    return Binv(blightless_vector).intval

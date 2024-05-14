from discretehelpers.binv import Binv


def mod_tt_neg(tt, signet):

    if type(signet) == int:
        signet_index = signet
    elif type(signet) == list:
        signet_binv = Binv(signet)
        signet_index = signet_binv.index
    elif type(signet) == Binv:
        signet_index = signet.index

    perm = [_ ^ signet_index for _ in range(len(tt))]

    return Binv([tt[_] for _ in perm])

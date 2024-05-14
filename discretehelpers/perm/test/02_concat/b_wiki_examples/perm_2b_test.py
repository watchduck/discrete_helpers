from discretehelpers.perm import Perm
from discretehelpers.binv import Binv


def test_wiki_examples():
    p = Perm([1, 3, 0, 2, 4])
    q = Perm([4, 3, 2, 1, 0])
    r = Perm([3, 1, 4, 2, 0])
    s = Perm([4, 2, 0, 3, 1])

    p_inv = Perm([2, 0, 3, 1, 4])
    r_inv = Perm([4, 1, 3, 0, 2])
    s_inv = Perm([2, 4, 1, 3, 0])

    v = ['0', '1', '2', '3', '4']

    assert p_inv == p.inverse
    assert q == q.inverse
    assert r_inv == r.inverse
    assert s_inv == s.inverse

    assert p * q == s
    assert q * p == r
    assert p.inverse * q.inverse == r.inverse

    x = ['2', '0', '3', '1', '4']
    y = ['4', '1', '3', '0', '2']
    assert p.apply_on_vector(v) == x
    assert q.apply_on_vector(x) == y
    assert r.apply_on_vector(v) == y

    assert p.apply_on_vector(Binv('00011')) == Binv('00101')

    # https://en.wikiversity.org/wiki/Permutation_notation#Aigner_2007
    s = Perm([0, 2, 3, 4, 1, 6, 5])
    t = Perm([0, 1, 3, 4, 5, 2, 6])
    ts = Perm([0, 3, 4, 5, 1, 6, 2])
    st = Perm([0, 2, 4, 1, 6, 3, 5])
    assert s * t == st
    assert t * s == ts

    # https://en.wikiversity.org/wiki/Permutation_notation#Knuth_1973
    assert Perm([[0, 5], [1, 4], [2, 3]]) * Perm([[0, 2], [1, 5, 3]]) == Perm([[0, 3, 4, 1], [2, 5]])

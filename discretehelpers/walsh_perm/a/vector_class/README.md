This class is used for the two vectors of a `WalshPerm` object.<br>
Its purpose is to store only the beginning,
and to fill up powers of two when higher lengths are requested.

The length of the vector can be smaller than the degree of the `WalshPerm`.<br>
E.g. wp(7, 6, 4) has degree 3, but the vector has length 2.<br>
Therefore `ExtendedLengthTooSmallError` is only used internally, and not important.<br>
Actual problems are prevented by `SizeSmallerDegreeError` in [walsh_perm/ex.py](../../ex.py).
from discretehelpers.binv import Binv
from discretehelpers.boolf import Boolf


miniri = Boolf(fullspots={0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 14, 16, 17, 24}, arity=5)
medusa = Boolf('1111 1111 1110 1010')
tabora = Boolf('0110 0011')  # EC 6 (like `takate`, `gilera`)
netuno = Boolf('1010 1011 0010 0011')  # EC 203 (like `dukeli`, `pamina`)
samara = Boolf('0101 0110 0000 0010')
savona = Boolf('0100 0000 0110 1010')
fatale = Boolf('1111 1101 1011 0000')  # like `fatima`
dolore = Boolf('1111 1011 1101 0000')
palato = Boolf('0101 0001 0100 1111')  # like `patina`
minase = Boolf('1001 0000')  # like `menose`
taroka = Boolf('1010 1001')  # like `takate`
rotovo = Boolf('0001 0000 0001 1111')  # like `ratava`, complement of `petula`
karate = Boolf(fullspots={1, 2, 4, 6, 7, 8,  9, 19, 27, 28, 29, 30, 31}, arity=5)  # like `rakete`
rakete = Boolf(fullspots={1, 2, 4, 5, 7, 8, 10, 19, 27, 28, 29, 30, 31}, arity=5)  # like `karate`
patata = Boolf('0110 1101 1010 0000')  # like `patati`
vinone = Boolf('1111 1010', skip_deflation=True)  # inflated `vinona`
pamera = Boolf('1111 1100 1010 0000')  # like `pamina`
pesari = Boolf('1110 0001 0111 1000')  # like `pesano`
dakete = Boolf('1110 1100 1010 1100')  # like `dakota`
tatago = Boolf('1110 1100')  # like `tatami`
rutavo = Boolf('1101 0011 1100 1000')  # like `ruteve`
rutoga = Boolf('1110 0011 1100 0100')  # like `ruteve`
rafemo = Boolf('0111 0100 1010 0000')  # like `rafisa
kisegi = Boolf('1111 0001 0010 1111')  # like `kisago`
dosale = Boolf('0011 0111 1110 1100')  # like `dosori`
ketibi = Boolf('1110 0000 0000 0111')  # bloated
ketago = Boolf('1100 1000 0001 0011')  # like `ketibi`
sopuki = Boolf('1111 1111 1000 0001')  # like `sopuda`
vidute = Boolf(fullspots={0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 16, 17, 18}, arity=5)
gudeba = Boolf('0000 0101 0101 1101')  # like `noliga`
faradi = Boolf('1101 0000 0000 0000')

babeku = Boolf(fullspots={1, 2, 4, 7, 8, 14, 25, 27, 28, 29, 31, 36, 38, 39, 41, 44, 52, 53, 54, 56, 57, 59, 60, 61, 62, 63, 64, 66, 72, 73, 74, 75, 76, 77, 79, 85, 86, 88, 90, 94, 97, 98, 99, 100, 101, 105, 107, 109, 110, 111, 113, 115, 118, 121, 122, 123, 124, 125, 126, 127, 129, 132, 133, 134, 137, 138, 141, 143, 144, 147, 148, 155, 157, 158, 159, 165, 167, 168, 170, 171, 175, 178, 180, 182, 185, 186, 187, 190, 193, 194, 197, 201, 202, 204, 207, 208, 211, 214, 216, 217, 218, 219, 220, 222, 223, 224, 225, 226, 228, 230, 232, 233, 235, 236, 238, 240, 243, 245, 247, 248, 249, 251, 252, 253, 254, 257, 258, 259, 261, 262, 264, 268, 269, 271, 272, 273, 274, 275, 277, 278, 282, 284, 286, 287, 290, 291, 292, 293, 294, 295, 298, 302, 309, 311, 312, 314, 316, 320, 322, 323, 326, 327, 328, 329, 330, 332, 333, 335, 337, 338, 339, 345, 347, 349, 351, 356, 360, 361, 362, 367, 373, 380, 381, 382, 383, 389, 394, 395, 396, 397, 398, 399, 402, 403, 404, 406, 407, 410, 411, 413, 417, 418, 421, 424, 428, 429, 430, 433, 434, 435, 437, 441, 443, 450, 454, 458, 460, 461, 464, 466, 467, 471, 473, 475, 476, 479, 480, 481, 484, 486, 487, 490, 491, 492, 495, 496, 499, 501, 502, 504, 505, 506, 507, 508, 510, 511}, arity=9)

########################################################

toledo = Boolf(fullspots={13, 14, 15, 19, 22, 23, 25, 27}, arity=5)
tamara = Boolf(fullspots={13, 14, 15, 19, 21, 23, 26, 27}, arity=5)
teresa = Boolf(fullspots={7, 13, 15, 22, 23, 25, 26, 27}, arity=5)

novara = Boolf(fullspots={11, 14, 15, 19, 21, 23, 27, 28}, arity=5)
nabuco = Boolf(fullspots={11, 13, 15, 19, 22, 23, 27, 28}, arity=5)
neruda = Boolf(fullspots={7, 11, 15, 21, 23, 26, 27, 28}, arity=5)

somali = Boolf(fullspots={13, 14, 15, 19, 22, 23, 25, 27, 29, 30}, arity=5)
serena = Boolf(fullspots={7, 14, 15, 19, 23, 25, 27, 28, 29, 30}, arity=5)
sibila = Boolf(fullspots={7, 14, 15, 21, 23, 25, 26, 27, 29, 30}, arity=5)

########################################################

barogi = Boolf('1111 1111 1010 1010')

bareto = Boolf(fullspots={2, 3, 4, 5, 10, 12}, arity=4)  # a, b, c, d

_b_nor_c = Boolf('1000', [1, 2])
_e_nor_f = Boolf('1000', [4, 5])
_a_nand_d = Boolf('1110', [0, 3])
barita = (_b_nor_c | _e_nor_f) & _a_nand_d

########################################################

basori_fs = {0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 14, 24, 26, 28, 30}
_basori_binv = Binv(exposet=basori_fs, length=32)
basori = Boolf(_basori_binv)

_ade = Boolf('1110 0010', [0, 3, 4])
_fgh = Boolf('1000 0000', [5, 6, 7])  # nor
_fh = Boolf('1110', [5, 7])  # nand
_abcde = Boolf(multi_and=[~0, 1, ~2, 3, ~4])
basiga = (_ade & _fgh) | (_fh & _abcde)
basiga_fs = {0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 14, 24, 26, 28, 30, 42, 74, 106, 138, 202}

########################################################

_a_nand_c = Boolf('1110', [0, 2])
_b_nand_d = Boolf('1110', [1, 3])
putuki = _a_nand_c & _b_nand_d

dukeli = Boolf('1111 1010 1000 1000')

dobipi = Boolf('1101 0100')
givero = Boolf('0101 0011')
dukove = Boolf(fullspots={0, 1, 2, 3, 4, 5, 8, 10}, arity=4)
badugo = Boolf(fullspots={2, 0, 8, 3, 1, 9, 7, 5, 13}, arity=4)
godogi = Boolf(fullspots={0, 1, 2, 5, 6, 7, 8, 10, 12, 14}, arity=4)

from discretehelpers.boolf import Boolf
from discretehelpers.binv import Binv

# clan 383
kusaga_binv = Binv('1110 1000 0100 0010')
kusaga = Boolf(kusaga_binv)

# clan 306
damela_binv = Binv('1110 1000 0010 1011')
damela_spread = Boolf(damela_binv, [10, 20, 30, 40])
damela = damela_spread.root_boolf

# clan 8
menose = Boolf('0110 0000')


# filtrates of barita

seduki = Boolf('1111 1010 1100 1000', [0, 2, 3, 5])
sedofu = Boolf('1111 1000 1000 1000', [1, 2, 4, 5])
sediri = Boolf(fullspots={0, 1, 2, 3, 4, 6, 8, 9, 12, 16, 17, 20, 24, 25, 28}, atomvals=[0, 2, 3, 4, 5])

from discretehelpers.boolf import Boolf


bunese = Boolf('1111 1110')
foravo = Boolf('0111 1110')
logota = Boolf('0101 1100 0011 1010')

kagusi = Boolf('0111 0000 1000 1100')
piferi = Boolf('0111 1010 1100 1000')

kabine = Boolf(fullspots={0, 2, 3, 19, 51, 115, 243, 242, 240, 244, 252, 124, 60, 28, 12, 4}, atomvals=list(range(8)))
kasete = Boolf(fullspots={0, 2, 18, 19, 51, 115, 243, 242, 240, 112, 116, 124, 60, 28, 12, 4}, atomvals=list(range(8)))

pelele = Boolf('0110 1001')
selera = pelele.complement

potula = Boolf('1110 0010')
kinide = Boolf('1110 0110')
gilipi = Boolf('1010 0110')
gelade = Boolf('1010 1110')

vanatu = Boolf('1001 0101 0010 1010')
vidita = Boolf('1011 1111 0010 1010')
darimi = Boolf('1111 0100 0000 0011', [1, 2, 3, 4])

tavoku = Boolf(fullspots={0, 1, 2, 3, 4, 5, 6, 7, 10, 14}, arity=4)
dagoro = Boolf(fullspots={1, 3, 4, 5, 7, 10, 14}, arity=4)
tinora = Boolf(fullspots={1, 2, 3, 4, 5, 6, 7, 10, 14}, arity=4)

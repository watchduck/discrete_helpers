from discretehelpers.boolf import Boolf


tokosi = Boolf('0001 0010 0000 0000  0000 0000 1000 1100', [1, 3, 5, 7, 9])
tokosi_bloatless = tokosi.bloatless_boolf


# splits equality blocks and preferred side
rudafi = Boolf(fullspots={4, 6, 9, 17}, atomvals=list(range(5)))
rigeko = Boolf(fullspots={4, 6, 11, 17}, atomvals=list(range(5)))
megomi = Boolf(fullspots={3, 4, 6, 12, 17}, atomvals=list(range(5)))
demole = Boolf(fullspots={4, 6, 12, 17}, atomvals=list(range(5)))

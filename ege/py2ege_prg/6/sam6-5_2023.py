"""
(Демо-2023) Миша заполнял таблицу истинности логической функции
F = ¬(y → x) \/ (z → w) \/ ¬z,
но успел заполнить лишь фрагмент из трёх её различных строк, даже не указав,
какому столбцу таблицы соответствует каждая из переменных x, y, z, w.
?	?	?	?	F
	0			0
0	1			0
1			0	0
Определите, какому столбцу таблицы соответствует каждая из переменных x, y, z, w.
(Ответ: yxzw)
"""
from itertools import product, permutations

def F( x, y, z, w ):
  return not(y <= x) or (z <= w) or not z

def callF( v, row ):
  return F( **dict( zip(v, row) ) )

from itertools import product, permutations

for a, b, c, d, e, f, g in product([0,1], repeat=7):
  table = [ (a, 0, b, c),
            (0, 1, d, e),
            (1, f, g, 0) ]
  if len(table) != len(set(table)): continue
  for v in permutations("xyzw"):
    valF = [ callF(v, row) for row in table ]
    if valF == [0, 0, 0]:
      print( ''.join(v) )



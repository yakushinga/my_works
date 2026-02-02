"""
(Демо-2021) Миша заполнял таблицу истинности логической функции
F = (x \/ y) /\ ¬(y = z) /\ ¬w,
но успел заполнить лишь фрагмент из трёх её различных строк, даже не указав,
какому столбцу таблицы соответствует каждая из переменных x, y, z, w.
?	?	?	?	F
1		1		1
0	1		0	1
	1	1	0	1
Определите, какому столбцу таблицы соответствует каждая из переменных x, y, z, w.
(Ответ: zyxw)
"""
from itertools import product, permutations

def F( x, y, z, w ):
  return (x or y) and not(y == z) and not w

def callF( v, row ):
  return F( **dict( zip(v, row) ) )

from itertools import product, permutations

for a, b, c, d in product([0,1], repeat=4):
  table = [ (1, a, 1, b),
            (0, 1, c, 0),
            (d, 1, 1, 0) ]
  if len(table) != len(set(table)): continue
  for v in permutations("xyzw"):
    valF = [ callF(v, row) for row in table ]
    if valF == [1, 1, 1]:
      print( ''.join(v) )



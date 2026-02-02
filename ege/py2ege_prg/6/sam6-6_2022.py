"""
(Демо-2022) Миша заполнял таблицу истинности логической функции
F = ¬(y → (x = w)) /\ (z → x),
но успел заполнить лишь фрагмент из трёх её различных строк, даже не указав,
какому столбцу таблицы соответствует каждая из переменных x, y, z, w.
?	?	?	?	F
	1	1		1
0			0	1
	0	1	0	1
Определите, какому столбцу таблицы соответствует каждая из переменных x, y, z, w.
(Ответ: wxyz)
"""
from itertools import product, permutations

def F( x, y, z, w ):
  return not(y <= (x == w)) and (z <= x)

def callF( v, row ):
  return F( **dict( zip(v, row) ) )

from itertools import product, permutations

for a, b, c, d, e in product([0,1], repeat=5):
  table = [ (a, 1, 1, b),
            (0, c, d, 0),
            (e, 0, 1, 0) ]
  if len(table) != len(set(table)): continue
  for v in permutations("xyzw"):
    valF = [ callF(v, row) for row in table ]
    if valF == [1, 1, 1]:
      print( ''.join(v) )



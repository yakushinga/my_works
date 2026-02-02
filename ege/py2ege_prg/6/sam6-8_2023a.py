"""
Логическая функция задаётся выражением
F = (x → y) /\ (¬y = z) /\ w,
На рисунке приведён частично заполненный фрагмент таблицы истинности
функции F, содержащий неповторяющиеся строки.
?	?	?	?	F
1	0			1
1	1			1
	1	1		1
Определите, какому столбцу таблицы соответствует каждая из переменных x, y, z, w.
(Ответ: wyxz)
"""
from itertools import product, permutations

def F( x, y, z, w ):
  return (x <= y) and ((not y) == z) and w

def callF( v, row ):
  return F( **dict( zip(v, row) ) )

from itertools import product, permutations

for a, b, c, d, e, f in product([0,1], repeat=6):
  table = [ (1, 0, a, b),
            (1, 1, c, d),
            (e, 1, 1, f) ]
  if len(table) != len(set(table)): continue
  for v in permutations("xyzw"):
    valF = [ callF(v, row) for row in table ]
    if valF == [1, 1, 1]:
      print( ''.join(v) )



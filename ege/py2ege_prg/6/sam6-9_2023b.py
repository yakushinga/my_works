"""
Логическая функция задаётся выражением
F = (x → (z = w)) \/ ¬(y → w),
На рисунке приведён частично заполненный фрагмент таблицы истинности
функции F, содержащий неповторяющиеся строки.
?	?	?	?	F
	1			0
0		0		0
	0	0		0
Определите, какому столбцу таблицы соответствует каждая из переменных x, y, z, w.
(Ответ: zwyx)
"""
from itertools import product, permutations

def F( x, y, z, w ):
  return (x <= (z == w)) or not(y <= w)

def callF( v, row ):
  return F( **dict( zip(v, row) ) )

from itertools import product, permutations

for a, b, c, d, e, f, g in product([0,1], repeat=7):
  table = [ (a, 1, b, c),
            (0, d, 0, e),
            (f, 0, 0, g) ]
  if len(table) != len(set(table)): continue
  for v in permutations("xyzw"):
    valF = [ callF(v, row) for row in table ]
    if valF == [0, 0, 0]:
      print( ''.join(v) )



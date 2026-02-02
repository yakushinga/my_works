"""
(Демо-2024) Миша заполнял таблицу истинности логической функции
F = (x & ¬y) or (y = z) or ¬w,
но успел заполнить лишь фрагмент из трёх её различных строк, даже не указав,
какому столбцу таблицы соответствует каждая из переменных x, y, z, w.
?	?	?	?	F
		0	0	0
1	0		0	0
1	0	1		0
Определите, какому столбцу таблицы соответствует каждая из переменных
x, y, z, w.
"""
from itertools import product, permutations

def F( x, y, z, w ):
  return (x and not y) or (y == z) or not w

def callF( names, values ):
  s = f"F( {names[0]}={values[0]}, " + \
         f"{names[1]}={values[1]}, " + \
         f"{names[2]}={values[2]}, " + \
         f"{names[3]}={values[3]} )"
  return eval(s)

from itertools import product, permutations

values = [0, 0, 0]
for a, b, c, d in product([0,1], repeat=4):
  table = [ (a, b, 0, 0),
            (1, 0, c, 0),
            (1, 0, 1, d) ]
  if len(table) != len(set(table)): continue
  for p in permutations("xyzw"):
    valP = [ callF(p, row) for row in table ]
    if valP == values:
      print( ''.join(p) )

#---------------------------------------------

def F( names, values ):
  var = dict( zip(names, values) )
  return (var['x'] and not var['y']) or \
         (var['y'] == var['z']) or not var['w']

values = [0, 0, 0]
for a, b, c, d in product([0,1], repeat=4):
  table = [ (a, b, 0, 0),
            (1, 0, c, 0),
            (1, 0, 1, d) ]
  if len(table) != len(set(table)): continue
  for p in permutations("xyzw"):
    valP = [ F(p, row) for row in table ]
    if valP == values:
      print( ''.join(p) )

"""
Вася заполнял таблицу истинности логической функции
F = x & (¬z → ¬y) & ¬w,
но успел заполнить лишь три её различных строки, даже не указав, какому
столбцу таблицы соответствует каждая из переменных x, y, z, w.
?	?	?	?	F
0	1	0	1	1
0	1	1	1	1
0	1	0	0	1
Определите, какому столбцу таблицы соответствует каж-дая из переменных x, y, z, w.
"""
print( 'x y z w F')
for x in 0, 1:
  for y in 0, 1:
    for z in 0, 1:
      for w in 0, 1:
        F = x and ((not z) <= (not y)) and not w
        if F:
          print( x, y, z, w, F )

print('------------------------------------')

from itertools import product
print( 'x y z w F')
for x, y, z, w in product( [0, 1], repeat=4 ):
  F = x and ((not z) <= (not y)) and not w
  if F:
    print( x, y, z, w, F )

print('------------------------------------')

def F( x, y, z, w ):
  return x and ((not z) <= (not y)) and (not w)

table = [ (0, 1, 0, 1), (0, 1, 1, 1), (0, 1, 0, 0) ]
values = [ 1, 1, 1]

from itertools import permutations

for p in permutations("xyzw"):
  valP = [ F( **dict( zip(p, row) ) )
           for row in table ]
  if valP == values:
     print( ''.join(p) )

print('------------------------------------')

def F( names, values ):
  var = dict( zip(names,values) )
  return int( var['x'] and ((not var['z']) <=
              (not var['y'])) and (not var['w']) )

from itertools import permutations
for p in permutations("xyzw"):
  valP = [ F(p, row) for row in table ]
  if valP == values:
     print( ''.join(p) )



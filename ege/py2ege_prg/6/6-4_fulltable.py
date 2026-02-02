"""
Логическая функция F задаётся выражением
(a → b) → (¬a ∧ c) .
Определите, какому столбцу таблицы истинности функции F соответствует
каждая из переменных a, b, c. В ответе напишите буквы a, b, c в том порядке,
в котором идут соответствующие им столбцы (без разделителей).
?	?	?	F
0	0	0	0
0	0	1	0
0	1	0	1
0	1	1	1
1	0	0	1
1	0	1	0
1	1	0	1
1	1	1	0
"""
def F( a, b, c ):
  return (a <= b) <= ( (not a) and c )

from itertools import product, permutations

table = list( product([0,1], repeat=3) )
values = [0, 0, 1, 1, 1, 0, 1, 0]
print( table )

for p in permutations("abc"):
  valP = []
  for row in table:
    s = f"F( {p[0]}={row[0]}," + \
           f"{p[1]}={row[1]}," + \
           f"{p[2]}={row[2]})"
    valP.append( eval(s) )
  if valP == values:
     print( ''.join(p) )

#----------------------------------------

def callF( names, values ):
  s = f"F({names[0]}={values[0]}, " + \
        f"{names[1]}={values[1]}, " + \
        f"{names[2]}={values[2]})"
  return eval(s)

for p in permutations("abc"):
  valP = [ callF(p, row) for row in table ]
  if valP == values:
     print( ''.join(p) )

#----------------------------------------

for p in permutations("abc"):
  valP = [ F( **dict( zip(p, row) ) )
           for row in table ]
  if valP == values:
     print( ''.join(p) )

#----------------------------------------

def F( names, values ):
  var = dict( zip(names,values) )
  return int( (var['a'] <= var['b']) <= ( (not var['a']) and var['c'] ) )

from itertools import permutations
for p in permutations("abc"):
  valP = [ F(p, row) for row in table ]
  if valP == values:
     print( ''.join(p) )

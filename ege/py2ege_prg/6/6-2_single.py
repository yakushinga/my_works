"""
Сколько различных решений имеет уравнение
(x1 & x2 -> x3) & (x2 & x3 -> x4) & (x3 & x4 -> x5) & (x4 & x5 -> x6) = 1
где x1, x2, ... x6 – логические переменные.
"""
def F( x ):
  res = True
  res = res and ((x[0] and x[1]) <= x[2])
  res = res and ((x[1] and x[2]) <= x[3])
  res = res and ((x[2] and x[3]) <= x[4])
  res = res and ((x[3] and x[4]) <= x[5])
  return res

def F( x ):
  res = True
  for x1, x2, x3 in zip(x, x[1:], x[2:]):
    res = res and ((x1 and x2) <= x3)
  return res

from itertools import product
count = 0
for x in product([0, 1], repeat=6):
  if F(x):
    count += 1
print( count )

#-------------------------------------------

print( len( [x for x in product([0, 1], repeat=6)
               if F(x) ] ) )

#-------------------------------------------

print( sum( 1 for x in product([0, 1], repeat=6)
              if F(x) ) )

#-------------------------------------------

print( sum( F(x) for x in product([0, 1], repeat=6) ) )


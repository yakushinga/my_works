"""
Сколько существует различных наборов значений логических переменных
x1, x2, ... x9, y1, y2, ... y9, которые удовлетворяют всем перечисленным
ниже условиям?
(¬(x1 = y1)) = (x2 = y2)
(¬(x2 = y2)) = (x3 = y3)
…
(¬(x8 = y8)) = (x9 = y9)
"""
def F( xy ):
  z = [ xi == yi for xi, yi in
                 zip(xy, xy[9:]) ]
  res = True
  for z1, z2 in zip(z, z[1:]):
    res = res and ((not z1) == z2)
  return res

def F( xy ):
  x, y = xy[:9], xy[9:]
  z = [ xi == yi for xi, yi in zip(x, y) ]
  res = True
  for z1, z2 in zip(z, z[1:]):
    res = res and ((not z1) == z2)
  return res

def F( xy ):
  x, y = xy[:9], xy[9:]
  res = True
  for i in range(8):
    res = res and ((x[i] != y[i]) == (x[i+1] == y[i+1]))
  return res

from itertools import product
count = 0
for xy in product( [0, 1], repeat=18 ):
  if F(xy):
    count += 1
print( count )

#-------------------------------------------

print( len( [xy for xy in product([0, 1], repeat=18)
               if F(xy) ] ) )

#-------------------------------------------

print( sum( 1 for xy in product([0, 1], repeat=18)
              if F(xy) ) )

#-------------------------------------------

print( sum( F(xy) for xy in product([0, 1], repeat=18) ) )


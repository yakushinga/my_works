"""
(Демо-2019) Сколько существует различных наборов значений логических
 переменных x1, x2, ... x9, y1, y2, ... y9, которые удовлетворяют всем
 перечисленным ниже условиям?
    (y1 → (y2 ∧ x1)) ∧ (x1 → x2) = 1
    (y2 → (y3 ∧ x2)) ∧ (x2 → x3) = 1
    …
    (y6 → (y7 ∧ x6)) ∧ (x6 → x7) = 1
    y7 → x7 = 1
(Ответ: 36)
"""
def F( xy ):
  x, y = xy[:7], xy[7:]
  res = True
  for i in range(6):
    res = res and (y[i] <= (y[i+1] and x[i])) and \
              (x[i] <= x[i+1])
  res = res and (y[6] <= x[6])
  return res

from itertools import product
count = 0
for xy in product( [0, 1], repeat=14 ):
  if F(xy):
    count += 1
print( count )

#-------------------------------------------

print( len( [xy for xy in product([0, 1], repeat=14)
               if F(xy) ] ) )

#-------------------------------------------

print( sum( 1 for xy in product([0, 1], repeat=14)
              if F(xy) ) )

#-------------------------------------------

print( sum( F(xy) for xy in product([0, 1], repeat=14) ) )


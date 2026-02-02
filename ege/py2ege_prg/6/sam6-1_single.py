"""
Сколько различных решений имеет уравнение
(x1 \/ x2) ∧ (x2 \/ x3) ∧ (x3 \/ x4) ∧ (x4 \/ x5) ∧ (x5 \/ x6) = 1,
где x1, x2, …, x6 – логические переменные.
(Ответ: 21)
"""
from itertools import product

def F( x ):
  res = True
  for x1, x2 in zip(x, x[1:]):
    res = res and (x1 or x2)
  return res

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


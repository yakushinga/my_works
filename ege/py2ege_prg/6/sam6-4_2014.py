"""
(Демо-2016) Сколько существует различных наборов значений логических переменных
x1, x2, ... x10 которые удовлетворяют всем перечисленным ниже условиям?
¬(x1 = x2) ∧ ( (x1 ∧ ¬x3) \/ (¬x1 ∧ x3) ) = 0
¬(x2 = x3) ∧ ( (x2 ∧ ¬x4) \/ (¬x2 ∧ x4) ) = 0
…
¬(x8 = x9) ∧ ( (x8 ∧ ¬x10) \/ (¬x8 ∧ x10) ) = 0
(Ответ: 20)
"""
def F( x ):
  res = True
  for i in range(8):
    res = res and not (
           (x[i] != x[i+1]) and
           ((x[i] and (not x[i+2])) or (not x[i]) and x[i+2]) )
  return res

from itertools import product
count = 0
for x in product( [0, 1], repeat=10 ):
  if F(x):
    count += 1
print( count )

#-------------------------------------------

print( len( [x for x in product([0, 1], repeat=10)
               if F(x) ] ) )

#-------------------------------------------

print( sum( 1 for x in product([0, 1], repeat=10)
              if F(x) ) )

#-------------------------------------------

print( sum( F(x) for x in product([0, 1], repeat=10) ) )


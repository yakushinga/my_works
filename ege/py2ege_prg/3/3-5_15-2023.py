"""
Для какого наименьшего целого неотрицательного числа A выражение
        (x + 2y < A) or (y > x) or (x > 60)
тождественно истинно, т.е. принимает значение 1 при любых целых
неотрицательных x и y?
(Ответ: 181)
"""
def F( A ):
  for x in range(100):
    for y in range(100):
      result = (x + 2*y < A) or (y > x) or (x > 60)
      if not result:
        return False
  return True

A = 0
while not F( A ):
  A += 1

print( A )

for A in range(1000):
  if F( A ):
    print( A )
    break

#----------------------------------------
from itertools import product
def F( A ):
  for x, y in product( range(100), repeat=2 ):
    result = (x + 2*y < A) or (y > x) or (x > 60)
    if not result:
      return False
  return True

A = 0
while not F( A ):
  A += 1

print( A )

#----------------------------------------
from itertools import product
A = 0
while not all( (x + 2*y < A) or (y > x) or (x > 60)
       for x, y in product( range(100), repeat=2 ) ):
  A += 1

print( A )

for A in range(1000):
  if all( (x + 2*y < A) or (y > x) or (x > 60)
          for x, y in product( range(100), repeat=2 ) ):
    print( A )
    break

"""
Сколько различных решений имеет уравнение
(a → b) or с → (¬a ∧ d)  = 0,
где a, b, c и d – логические переменные.
"""
count = 0
for a in [0, 1]:
  for b in [0, 1]:
    for c in [0, 1]:
      for d in [0, 1]:
        if not (((a <= b) or c) <= (not a and d)):
          count += 1

print( count )

#----------------------------------------

def F( a, b, c, d ):
  return ((a <= b) or c) <= (not a and d)

from itertools import product
count = 0
for a, b, c, d in product([0,1], repeat=4):
  if not F(a, b, c, d):
    count += 1

print( count )

#----------------------------------------

from itertools import product
results = [ p for p in product([0,1], repeat=4)
            if not F(*p) ]
print( len(results) )

print( len( [ p for p in product([0,1], repeat=4)
                if not F(*p) ] ) )

print( sum( 1 for p in product([0,1], repeat=4)
              if not F(*p) ) )

print( sum( not F(*p)
            for p in product([0,1], repeat=4) ) )

#----------------------------------------

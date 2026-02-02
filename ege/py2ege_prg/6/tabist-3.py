def F( a, b, c ):
  return (a or b) <= ( (not b) <= (not c))

print( 'a b c' )
for a in [False, True]:
  for b in [False, True]:
    for c in [False, True]:
      print( a, b, c, '|', F(a,b,c) )

print( 'a b c' )
values = [False, True]
for a in values:
  for b in values:
    for c in values:
      print( a, b, c, '|', F(a,b,c) )

def F( a, b, c ):
  return int( (a or b) <= ( (not b) <= (not c)) )

print( 'a b c   F' )
values = [0, 1]
for a in values:
  for b in values:
    for c in values:
      print( a, b, c, '|', F(a,b,c) )

from itertools import product
print( 'a b c   F' )
for a, b, c in product([0, 1], repeat=3 ):
  print( a, b, c, '|', F(a,b,c) )
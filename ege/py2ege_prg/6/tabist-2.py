def F1( a, b, c ):
  return int( a or b <= (not b) <= (not c) )

def F2( a, b, c ):
  return int( a or (b <= (not b) and (not b) <= (not c)) )

def F3( a, b, c ):
  return int( (a or b) <= (not b) <= (not c) )

def F4( a, b, c ):
  return int( (a or b) <= (not b) and (not b) <= (not c) )

from itertools import product
print( 'a b c' )
for a, b, c in product([0, 1], repeat=3 ):
  print( a, b, c, '|', F1(a,b,c), F2(a,b,c), '|', F3(a,b,c), F4(a,b,c) )
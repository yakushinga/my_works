from itertools import product

p = [1, 2]
xy = product( p, repeat=2 )
for x, y in xy:
  print( x + y )
  break

print( next(xy) )
print( next(xy) )
print( next(xy) )
print( next(xy) )
print( next(xy) )
print( next(xy) )


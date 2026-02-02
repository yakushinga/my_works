A = "АБВГД"
A = ( 'А', 'Б', 'В', 'Г', 'Д' )
A = [ 'А', 'Б', 'В', 'Г', 'Д' ]
A = { 'А', 'Б', 'В', 'Г', 'Д' }

for x in A:
  for y in A:
    for z in A:
      for w in A:
        print( x+y+z+w )

from itertools import product

for word in product(A, repeat=4):
  print( word)

A = "ГОРА"
A = ( 'Г', 'О', 'Р', 'А' )
A = [ 'Г', 'О', 'Р', 'А' ]

count = 0
for x in A:
  for y in A:
    for z in A:
      for w in A:
        if x != y and x != z and x != w and \
           y != z and y != w and z != w:
          print( x+y+z+w )
          count += 1
print( count )

A = "АБАК"
count = 0
rN = range(len(A))
for i in rN:
  for j in rN:
    for k in rN:
      for m in rN:
        if i != j and i != k and i != m and \
           j != k and j != m and k != m:
          print( A[i]+A[j]+A[k]+A[m] )
          count += 1
print( count )

A = { 'Г', 'О', 'Р', 'А' }

count = 0
for x in A:
  for y in A - {x}:
    for z in A - {x} - {y}:
      for w in A - {x} - {y} - {z}:
        print( x+y+z+w )
        count += 1
print( count )

from itertools import permutations
A = "ГОРА"
count = 0
for word in permutations(A):
  print( word)
  count += 1
print( count )

count = 0
for word in permutations(A, 2):
  print( word)
  count += 1
print( count )
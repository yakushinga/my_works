A = "9876543210"
A = ( '9', '8', '7', '6', '5', '4', '3', '2', '1', '0' )

count = 0
for i in range(7):
  for j in range(i+1,8):
    for k in range(j+1,9):
      for m in range(k+1,10):
        print( A[i]+A[j]+A[k]+A[m] )
        count += 1
print( count )

from itertools import combinations

count = 0
for word in combinations( A, 4 ):
  print( word)
  count += 1
print( count )

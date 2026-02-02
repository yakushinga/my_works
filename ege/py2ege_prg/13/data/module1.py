with open("data13-10.txt") as F:
  N, M = map(int, F.readline().split())
  data = [ int(s) for s in F ]

from random import randint

def dist( i, j ):
  d1 = abs(i - j)
  return min( d1, N-d1 )

data = data*2

with open("data13-10.txt", "w") as F:
   print( N, M, file=F )
   for i in range(N):
     if dist( i, 0 ) <= M:
       data[i] += randint(1, 10)
     print( data[i], file=F )


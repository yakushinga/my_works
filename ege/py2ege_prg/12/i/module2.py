from random import randint

N = 100
L = 500
M = 200

pos = []
data = []
for i in range(N):
  while (p := randint( 0, L-1 )) in pos:
    pass
  d = randint( 10, 100 )
  pos.append( p )
  data.append( d )

with open('data12-12.txt', 'w') as F:
  print( L, N, M, file=F )
  for i in range(N):
    print( pos[i], data[i], file=F )




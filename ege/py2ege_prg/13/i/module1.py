from random import choice, randint

with open('input_12.txt') as F:
  N, M = map( int, F.readline().split() )
  data = [ int(s) for s in F.read().split() ]

N = 300
M = 329*300//1500

with open('input_12.txt', 'w') as F:
  print( N, M, file=F )
  for i in range(N):
    print( data[i], file=F )

with open("data12-3.txt") as F:
  K = int( F.readline() )
  N = int( F.readline() )
  data = []
  for s in F:
    t0, t1 = map( int, s.split() )
    data.append( [t0, t1] )

from random import randint, shuffle

K = 200
N = 900
while len(data) > N:
  i = randint(0, len(data)-1)
  del data[i]

shuffle( data );

with open("data12-3a.txt", "w") as F:
   print( K, file=F )
   print( N, file=F )
   for i in range(N):
     data[i][0] += randint(-25, 25)
     data[i][1] += randint(-25, 25)
     if data[i][0] > 24*60 - 10:
       data[i][0] = 24*60 - 10
     if data[i][1] < data[i][0]+10:
       data[i][1] = data[i][0] + randint(10, 500)
     if data[i][1] > 24*60:
       data[i][1] = 24*60
     print( data[i][0], data[i][1],
            file=F )

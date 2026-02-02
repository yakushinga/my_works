from random import randint

def normal():
  if 0*randint(0,100):
    return sum( randint(1, 1440) for _ in range(12) ) // 12
  else:
    return randint(500, 1000)

N = 1000

while True:
  data = []
  count = [0]*1440
  for _ in range(N):
    m = normal()
    h = randint(1, 20)
    a = max( 1, m - h )
    b = min( 1440, m + h )
    data.append( (a, b) )
    for i in range(a, b+1):
      count[i-1] += 1

  mx = max(count)
  #print( mx )
  xx = [ x for x in count if x == mx ]
  if len(xx) > 8: break

with open('i/data12-5a.txt', 'w') as F:
  print( N, file=F)
  for d in data:
    print( *d, file=F)




with open("i/input_4.txt") as F:
  N = int( F.readline() )
  data = []
  for s in F:
    t0, t1 = map( int, s.split() )
    data.append( (t0, t1) )

maxCount = 0
maxSpan = 0
uu = []

def place( tFree, used, tail ):
  global uu, maxCount, maxSpan
  if len(used) >= maxCount:
    maxCount = len(used)
    if len(used) > 1:
      maxSpan = max( used[-1][0] - used[-2][1],  maxSpan )
  for i, t in enumerate(tail):
    if t[0] >= tFree:
      place( t[1], used+[t], tail[i+1:] )

place( 0, [], data )
print( maxCount, maxSpan )
print( uu )
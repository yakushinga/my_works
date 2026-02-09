with open('26-176.txt') as F:
  N = int(F.readline())
  data = []
  nTop = nBottom = 0
  for i in range(N):
    wait, active  = map(int, F.readline().split())
    if wait < active:
      data.append( (wait, 0, i+1) )
      nTop += 1
    else:
      data.append( (active, 1, i+1) )
      nBottom += 1

data = sorted( data )

last = data[-1]

print( last[2] )

if last[1] == 0:
   print( nBottom )
else:
   print( nBottom - 1 )


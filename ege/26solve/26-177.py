with open('26-177.txt') as F:
  N = int(F.readline())
  data = {}
  for i in range(N):
    order, house, flat  = map(int, F.readline().split())
    entr = 1 + (flat - 1) // 25
    if house in data:
      data[house]['entr'].add( entr )
      data[house]['maxOrder'] = max( data[house]['maxOrder'], order )
      data[house]['count'] += 1
    else:
      data[house] = { 'entr': {entr}, 'maxOrder': order, 'count': 1 }

stats = sorted( data.items(),
                key = lambda x: (-len(x[1]['entr']), x[1]['maxOrder']) )
for i in range(5):
  print( stats[i] )

print( stats[0][0], stats[0][1]['count'] )


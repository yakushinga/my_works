with open('26-177.txt') as F:
  N = int(F.readline())
  data = {}
  for i in range(N):
    order, house, flat  = map(int, F.readline().split())
    entr = 1 + (flat - 1) // 25
    if house in data:
      data[house]['entr'].add( entr )
      data[house]['maxOrder'] = max( data[house]['maxOrder'], order )
      data[house][entr] = data[house].get(entr, []) + [order]
      data[house]['count'] += 1
    else:
      data[house] = { 'entr': { entr }, 'maxOrder': order, entr: [order], 'count': 1 }

stats = sorted( data.items(),
                key = lambda x: (-x[1]['count'], x[1]['maxOrder']) )

for i in range(5):
  print( stats[i][0], stats[i][1]['count'], stats[i][1]['maxOrder'], stats[i][1][1] )

house = stats[0][0]

houseData = data[house]
print( houseData )

selectedEntr = 0
for entr in houseData:
  if type(entr) == int:
    if not selectedEntr or len(houseData[entr]) > len(houseData[selectedEntr]) or \
      (len(houseData[entr]) == len(houseData[selectedEntr]) and
       min(houseData[entr]) < min(houseData[selectedEntr])):
      selectedEntr = entr
      print( selectedEntr, len(houseData[selectedEntr]), min(houseData[selectedEntr]))

print( house, selectedEntr )






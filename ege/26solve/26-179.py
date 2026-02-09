with open('26-177.txt') as F:
  N = int(F.readline())
  data = {}
  minOrder = {}
  for i in range(N):
    order, house, flat  = map(int, F.readline().split())
    entr = 1 + (flat - 1) // 25
    if house in data:
      data[house].append( [entr, order] )
      minOrder[house] = min( minOrder[house], order )
    else:
      data[house] = [ [entr, order] ]
      minOrder[house] = order

maxCount = 0
selectedHouse = 0
for house, orderInfo in sorted(data.items()):
   orderInfo.sort()
   houseCount = count = 1
   for i in range(1,len(orderInfo)):
     if orderInfo[i][0] == orderInfo[i-1][0]:
       continue
     elif orderInfo[i][0] == orderInfo[i-1][0]+1:
       count += 1
       if count > houseCount:
         houseCount = count
     else:
       count = 1
   if houseCount > maxCount or\
      houseCount == maxCount and minOrder[house] < minOrder[selectedHouse]:
      maxCount = houseCount
      selectedHouse = house
      print( houseCount, selectedHouse, minOrder[selectedHouse] )

houseTotal = len( data[selectedHouse] )

print( selectedHouse, houseTotal )


"""from random import randint, choice, shuffle

with open('26-177.txt','w') as F:
  N = 10000
  numbers = []
  for _ in range(N):
    while True:
      n = randint( 100000, 400000 )
      if n not in numbers:
        numbers.append(n)
        break
  shuffle( numbers )
  print( N, file=F )
  for i in range(N):
    print( numbers[i], randint(1,200), randint(1, 200), file=F )
"""

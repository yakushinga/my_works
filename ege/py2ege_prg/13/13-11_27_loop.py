"""
На кольцевой дороге длиной L км находятся N заправочных станций. Нужно
разместить рядом с одной из заправочных станций бензохранилище так, чтобы
суммарная стои-мость доставки бензина на все станции была минимальной. Бензин
поставляется в цистернах объёмом V м3 каждая, затраты на доставку вычисляются
как произведение расстояния на количество поездок бензовоза. За один рейс
бензовоз доставляет бензин только на одну заправочную станцию. В первой
строке файла input.txt записаны натуральные числа N – количество заправочных
станций, L – длина дороги (чётное число) и V – объём цистерны. В каждой из
следующих N строк записаны два целых неотрицательных числа: расстояние от
очередной заправочной станции до нулевой отметки дороги (L-й километр
совпадает с нулевым) и количество бензина, которое туда нужно доставить с
бензохранилища. Определите минимальную общую стоимость доставки.

Ответ: 1268077
"""
with open("i/input_11.txt") as F:
  N, L, V = map( int, F.readline().split() )
  data = [0]*L
  for s in F:
    pos, x = map( int, s.split() )
    data[pos%L] = x//V + (x % V > 0)

data *= 2
p = [0]*(2*L+1)
for i in range(1,2*L+1):
  p[i] = p[i-1] + data[i-1]

cost = sum( min(i, L-i)*data[i] for i in range(L) )
minCost = cost if data[0] else float('inf')

for i in range(1,L):
  #s -= p[i+L//2] - p[i]
  #s += p[i+L] - p[i+L//2]
  cost += p[i] + p[i+L] - 2*p[i+L//2]
  if data[i]:  # можно ставить станцию?
    minCost = min(cost, minCost)
print( minCost )

print('------------------------------')

with open("i/input_11.txt") as F:
  N, L, V = map( int, F.readline().split() )
  position = []
  data = []
  for s in F:
    pos, x = map( int, s.split() )
    position.append( pos % L )
    data.append( x//V + (x % V > 0) )

def dist( i, j ):
  d1 = abs( position[i] - position[j] )
  return min( d1, L - d1 )

minCost = float('inf')
for i in range(N):
  cost = 0
  for j in range(N):
    cost += data[j] * dist( i, j )
  minCost = min( cost, minCost )

print( minCost )
"""
Вдоль кольцевой дороги длиной L расположены N хуторов, в которые нужно доставлять
товары с помощью роботов-доставщиков. У компании хватает денег только на один
пункт доставки. Зарядка робота ограничена, её хватает на то, чтобы проехать M км
в одну сторону и вернуться в пункт доставки для подзарядки. В первой строке
файла data13-9.txt записаны три натуральных числа: L - длина дороги, N -
количество хуторов, и M - максимальное расстояние, которое может пройти робот
в одну сторону). В каждой из следующих N строк записаны два натуральных
числа – километровая отметка, соответствующая хутору, и количество товаров,
которые нужно доставить на хутор. Определите, на каком хуторе нужно построить
пункт доставки, чтобы роботы смогли доставить наибольшее количество товаров.
В ответе запишите найденное количество товаров.

Ответ: 4254
"""
with open('data/data13-11.txt') as F:
  L, N, M = map( int, F.readline().split() )
  data = [0]*L
  #for s in F:
  for _ in range(N):
    s = F.readline()
    pos, count = map( int, s.split() )
    data[pos%L] = count

def dist( i, j ):
  d1 = abs( i - j )
  return min( d1, L-d1 )

s = sum( data[:2*M+1] )
maxSum = s if data[M] else 0

for i in range(1, L):
  s += data[(i+2*M)%L] - data[i-1]
  if data[(i+M)%L]:
    maxSum = max( s, maxSum )

print( maxSum )

print('-------------------------------------------')

with open('data/data13-11.txt') as F:
  L, N, M = map( int, F.readline().split() )
  position = []
  data = []
  for _ in range(N):
    pos, count = map(int, F.readline().split())
    position.append( pos )
    data.append( count )

def dist( i, j ):
  d1 = abs(position[i] - position[j])
  return min( d1, L-d1)

iMax, maxSum = 0, 0
for i in range(N):
  s = 0
  for j in range(N):
    if dist(i, j) <= M:
      s += data[j]
  if s > maxSum:
    iMax = position[i]
    maxSum = max( s, maxSum )

print( iMax, maxSum )

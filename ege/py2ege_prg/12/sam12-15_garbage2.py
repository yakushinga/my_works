"""
Вдоль кольцевой автодороги длиной L расположены N населённых пунктов, из
которых нужно вывозить мусор. Компания собирается построить два
мусороперерабатывающих завода, причём каждый из них сможет обработать мусор
с населённых пунктов, удалённых от него не более чем на M км. В первой строке
файла data12-15.txt записаны три натуральных числа: L – длина дороги,
N – количество насе-лённых пунктов и M – максимальное расстояние от населённого
пункта до завода. В каждой из следующих N строк записаны два натуральных
числа – километровая отметка, соответствующая населённому пункту, и количество
контейнеров мусора, которые нужно вывезти и переработать. Определите, в каких
населённых пунктах нужно построить заводы, чтобы они смогли обработать
наибольшее количество контейнеров с мусором. В ответе запишите найденное
количество контейнеров.
(Ответ: 2660)
"""
with open('data/data12-15.txt') as F:
  L, N, M = map( int, F.readline().split() )
  position = []
  data = []
  for s in F:
    pos, x = map( int, s.split() )
    position.append( pos % L )
    data.append( x )

import timeit

def dist( i, j ):
  d1 = abs(position[i] - position[j])
  return min( d1, L-d1 )

t0 = timeit.default_timer()

maxSum = 0
for i1 in range(N):
  for i2 in range(i1+1, N):
    if position[i2]-position[i1] < 2*M+1:
      continue
    s = 0
    for j in range(N):
      if dist( i1, j ) <= M or dist( i2, j ) <= M:
        s += data[j]
    #if s > maxSum:
    #  print( i1, i2, data[i1], data[i2], s )
    maxSum = max( s, maxSum )

print( maxSum, timeit.default_timer() - t0 )

print('----------------------------------')

t0 = timeit.default_timer()
maxSum = 0
for i1 in range(N):
  for i2 in range(i1+1, N):
    if position[i2]-position[i1] < 2*M+1:
      continue
    s = 0
    for j in range(N):
      if dist( i1, j ) <= M or \
         dist( i2, j ) <= M :
        s += data[j]
    #if s > maxSum:
    #  print( i1, i2, position[i1], position[i2], s )
    maxSum = max( s, maxSum )

print( maxSum, timeit.default_timer() - t0 )

print('----------------------------------')

t0 = timeit.default_timer()
maxSum = 0
for i1 in range(N):
  for i2 in range(i1+1, N):
    if position[i2]-position[i1] < 2*M+1:
      continue
    s = sum( data[j] for j in range(N)
             if dist( i1, j ) <= M or \
                dist( i2, j ) <= M )
    maxSum = max( s, maxSum )

print( maxSum, timeit.default_timer() - t0 )

print('----------------------------------')

t0 = timeit.default_timer()
maxSum = max( sum( data[j] for j in range(N)
                   if dist( i1, j ) <= M or \
                      dist( i2, j ) <= M )
              for i1 in range(N)
              for i2 in range(i1+1, N)
              if position[i2]-position[i1] >= 2*M+1 )

print( maxSum, timeit.default_timer() - t0 )

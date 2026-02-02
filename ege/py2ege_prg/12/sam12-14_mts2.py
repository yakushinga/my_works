"""
Вдоль прямой автодороги расположены N населённых пунктов, которые нужно обеспечить
сотовой связью. Компания собирается построить две вышки сотовой связи в
этом районе. Каждая вышка обеспечивает связь только в радиусе M км; вышки нужно
разместить в населённых пунктах. В первой строке файла data12-14.txt записаны
натуральные числа N – количество населённых пунктов, и M – радиус действия
сигнала. В каждой из следующих N строк записаны два натуральных числа –
километровая отметка, соответствующая населённому пункту (расстояние от
нулевой отметки дороги), и количество жителей в нём. Определите наибольшее
количество жителей, которых можно обеспечить сотовой связью.
(Ответ: 2874)
"""
with open('data/data12-14.txt') as F:
  N, M = map( int, F.readline().split() )
  position = []
  data = []
  for s in F:
    pos, x = map( int, s.split() )
    position.append( pos )
    data.append( x )

import timeit

t0 = timeit.default_timer()
maxSum = 0
for i1 in range(N):
  for i2 in range(i1+1, N):
    if position[i2]-position[i1] <= 2*M: continue
    s = 0
    for j in range(N):
      if abs(position[i1]-position[j]) <= M:
        s += data[j]
    for j in range(N):
      if abs(position[i2]-position[j]) <= M:
        s += data[j]
    maxSum = max( s, maxSum )

print( maxSum, timeit.default_timer() - t0 )

print('----------------------------------')

t0 = timeit.default_timer()
maxSum = 0
for i1 in range(N):
  for i2 in range(i1+1, N):
    if position[i2]-position[i1] <= 2*M: continue
    s = 0
    for j in range(N):
      if abs(position[i1]-position[j]) <= M or \
         abs(position[i2]-position[j]) <= M:
        s += data[j]
    maxSum = max( s, maxSum )

print( maxSum, timeit.default_timer() - t0 )

print('----------------------------------')

t0 = timeit.default_timer()
maxSum = 0
for i1 in range(N):
  for i2 in range(i1+1, N):
    if position[i2]-position[i1] <= 2*M: continue
    s = sum( data[j] for j in range(N)
             if abs(position[i1]-position[j]) <= M or \
                abs(position[i2]-position[j]) <= M )
    maxSum = max( s, maxSum )

print( maxSum, timeit.default_timer() - t0 )

print('----------------------------------')

t0 = timeit.default_timer()
maxSum = max( sum( data[j] for j in range(N)
                   if abs(position[i1]-position[j]) <= M or \
                      abs(position[i2]-position[j]) <= M )
              for i1 in range(N)
                for i2 in range(i1+1, N)
                  if position[i2]-position[i1] > 2*M )

print( maxSum, timeit.default_timer() - t0 )

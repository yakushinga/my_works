"""
Вдоль прямой автодороги расположены N населённых пунктов, которые нужно обеспечить
сотовой связью. У компании хватает денег только на две вышки сотовой связи в
этом районе. Каждая вышка обеспечивает связь только в радиусе M км; вышки нужно
разместить в населённых пунктах, причём для устойчивой работы каждый пункт должен
принимать сигнал только с одной вышки.. В первой строке файла data13-10.txt записаны
натуральные числа N – количество населённых пунктов, и M – радиус действия
сигнала. В каждой из следующих N строк записаны два натуральных числа –
километровая отметка, соответствующая населённому пункту (расстояние от
нулевой отметки дороги), и количество жителей в нём. Определите наибольшее
количество жителей, которых можно обеспечить сотовой связью.
(Ответ: 3150)
"""
with open('i/input_15.txt') as F:
  N, M = map( int, F.readline().split() )
  position = []
  data = []
  for s in F:
    pos, x = map( int, s.split() )
    position.append( pos )
    data.append( x )

temp = data[:]
N = max(position) + 1
data = [0]*(N+1)
for i, pos in enumerate(position):
  data[pos] = temp[i]

import timeit

t0 = timeit.default_timer()

s = [0]*N
s[0] = sum(data[0:2*M+1])
for i in range(1,N-M):
  s[i] = s[i-1] - data[i-1]
  if i+2*M < N:
    s[i] += data[i+2*M]

sMax = [0]*N
sMax[0] = s[0] if data[M] else 0
for i in range(1,N-M):
  sMax[i] = max( sMax[i-1], s[i] ) \
                 if data[i+M] else sMax[i-1]

s2Max = 0
for j in range(2*M+1,N-M):
  if data[j+M]:
    s2Max = max( s[j]+sMax[j-2*M-1], s2Max )

print( s2Max, timeit.default_timer() - t0 )

print('----------------------------------')

s = [0]*N
s[0] = sum(data[0:2*M+1])
sMax = [0]*N
sMax[0] = s[0] if data[M] else 0
for i in range(1,N-M):
  s[i] = s[i-1] - data[i-1]
  if i+2*M < N:
    s[i] += data[i+2*M]
  sMax[i] = max( sMax[i-1], s[i] ) \
            if data[i+M] else sMax[i-1]

s2Max = max( (s[j]+sMax[j-2*M-1]
             for j in range(2*M+1,N-M)
             if data[j+M]), default=0 )

print( s2Max, timeit.default_timer() - t0 )


print('----------------------------------')

data = temp
N = len(data)

t0 = timeit.default_timer()

maxSum = 0
for i1 in range(N):
  for i2 in range(i1+1, N):
    if position[i2]-position[i1] <= M: continue
    s = 0
    for j in range(N):
      if abs(position[i1]-position[j]) <= M or \
         abs(position[i2]-position[j]) <= M:
        s += data[j]
    if s > maxSum:
      maxSum = max( s, maxSum )

print( maxSum, timeit.default_timer() - t0 )

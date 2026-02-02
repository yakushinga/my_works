"""
Вдоль кольцевой автодороги длиной L расположены N населённых пунктов, из
которых нужно вывозить мусор. У компании хватает денег только на два
мусороперерабатывающих завода, причём каждый из них сможет обработать мусор
с населённых пунктов, удалённых от него не более чем на M км. В первой строке
файла data13-11.txt записаны три натуральных числа: L – длина дороги (чётное число),
N – количество населённых пунктов и M – максимальное расстояние от населённого
пункта до завода. В каждой из следующих N строк записаны два натуральных
числа – километровая отметка, соответствующая населённому пункту, и количество
контейнеров мусора, которые нужно вывезти и переработать. Определите, в каких
населённых пунктах нужно построить заводы, чтобы они смогли обработать
наибольшее количество контейнеров с мусором. В ответе запишите найденное
количество контейнеров.

Ответ: 2886
"""
with open('data/data13-13.txt') as F:
  L, N, M = map( int, F.readline().split() )
  position = []
  data = []
  for s in F:
    pos, x = map( int, s.split() )
    position.append( pos % L )
    data.append( x )

temp = data[:]
data = [0]*L
for i, pos in enumerate(position):
  data[pos % L] = temp[i]

import timeit

data = data*2

t0 = timeit.default_timer()

s = [0]*L
s[0] = sum(data[0:2*M+1])
for i in range(1,L):
  s[i] = s[i-1] - data[i-1]
  s[i] += data[i+2*M]

sMax = [ [0]*L for _ in range(2*M+1) ]
for k in range(2*M+1):
  sMax[k][k] = s[k] if data[k+M] else 0
  for i in range(k+1,L):
    sMax[k][i] = max( sMax[k][i-1], s[i] ) \
                      if data[i+M] else sMax[k][i-1]

s2Max = 0
for j in range(2*M+1,L):
  if data[j+M]:
    k = 0 if j+2*M < L else (j+2*M+1) % L
    s2Max = max( s[j]+sMax[k][j-2*M-1], s2Max )

print( s2Max, timeit.default_timer() - t0 )

print('----------------------------------')

data = temp
N = len(data)

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
    maxSum = max( s, maxSum )

print( maxSum, timeit.default_timer() - t0 )

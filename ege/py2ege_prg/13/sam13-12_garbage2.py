"""
На каждом километре кольцевой автодороги расположены населённые пункты, из
которых нужно вывозить мусор. У компании хватает денег только на два
мусороперерабатывающих завода, причём каждый из них сможет обработать мусор
с населённых пунктов, удалённых от него не более чем на M км. В первой строке
файла data13-10.txt записаны три натуральных числа: N – количество населённых
пунктов (чётное число) и M – максимальное расстояние от населённого пункта
до завода. В каждой из следующих N строк записано одно натуральное число –
количество контейнеров мусора, которые нужно вывезти и переработать. Определите,
в каких населённых пунктах нужно построить заводы, чтобы они смогли обработать
наибольшее количество контейнеров с мусором. В ответе запишите найденное
количество контейнеров.

Ответ: 16300
"""
with open('data/data13-12.txt') as F:
  N, M = map( int, F.readline().split() )
  data = [ int(s) for s in F ]

N, M = 8, 1
data = [6, 7, 1, 8, 9, 10, 2, 7]

import timeit

data = data*2

t0 = timeit.default_timer()

s = [0]*N
s[0] = sum(data[0:2*M+1])
for i in range(1,N):
  s[i] = s[i-1] - data[i-1]
  s[i] += data[i+2*M]

sMax = [ [0]*N for _ in range(2*M+1) ]
for k in range(2*M+1):
  sMax[k][k] = s[k] if data[k+M] else 0
  for i in range(k+1,N):
    sMax[k][i] = max( sMax[k][i-1], s[i] ) \
                      if data[i+M] else sMax[k][i-1]

s2Max = 0
for j in range(2*M+1,N):
  if data[j+M]:
    k = 0 if j+2*M < N else (j+2*M+1) % N
    s2Max = max( s[j]+sMax[k][j-2*M-1], s2Max )

print( s2Max, timeit.default_timer() - t0 )

print('----------------------------------')

data = data[:N]

def dist( i, j ):
  d1 = abs(i - j)
  return min( d1, N-d1 )

t0 = timeit.default_timer()

maxSum = 0
for i1 in range(N):
  for i2 in range(i1+2*M+1, N):
    s = 0
    for j in range(N):
      if dist( i1, j ) <= M or dist( i2, j ) <= M:
        s += data[j]
    maxSum = max( s, maxSum )

print( maxSum, timeit.default_timer() - t0 )

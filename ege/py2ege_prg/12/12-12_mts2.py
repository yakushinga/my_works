"""
На каждом километре прямой автодороги расположены N населённых пунктов, которые
нужно обеспечить сотовой связью. Компания собирается построить две вышки
сотовой связи в этом районе. Каждая вышка обеспечивает связь только в радиусе
M км; вышки нужно разместить в населённых пунктах. В первой строке файла
input.txt записаны натуральные числа N – количество населённых пунктов, и
M – радиус действия сигнала. В каждой из следующих N строк записано одно
натуральное число – количество жителей в населённом пункте.
Данные о населённых пунктах записаны по порядку, начиная с пункта, расположенного
на нулевой отметке дороги. Определите наибольшее количество жителей, которых
можно обеспечить сотовой связью.
(Ответ: 13981)
"""
with open('i/input_12.txt') as F:
  N, M = map( int, F.readline().split() )
  data = [ int(s) for s in F ]

import timeit

t0 = timeit.default_timer()
maxSum = 0
for i1 in range(N):
  for i2 in range(N):
    s = 0
    for j in range(N):
      if abs(i1-j) <= M or abs(i2-j) <= M:
        s += data[j]
    maxSum = max( s, maxSum )

print( maxSum, timeit.default_timer() - t0 )

print('----------------------------------')

t0 = timeit.default_timer()
maxSum = 0
for i1 in range(M,N-3*M-1):
  for i2 in range(i1+2*M+1, N-M):
    s = 0
    for j in range(N):
      if abs(i1-j) <= M or abs(i2-j) <= M:
        s += data[j]
    maxSum = max( s, maxSum )

print( maxSum, timeit.default_timer() - t0 )

print('----------------------------------')

t0 = timeit.default_timer()
maxSum = 0
for i1 in range(M,N-3*M-1):
  for i2 in range(i1+2*M+1, N-M):
    s = sum( data[j] for j in range(N)
             if abs(i1-j) <= M or abs(i2-j) <= M )
    maxSum = max( s, maxSum )

print( maxSum, timeit.default_timer() - t0 )

print('----------------------------------')

t0 = timeit.default_timer()
maxSum = max( sum( data[j] for j in range(N)
                   if abs(i1-j) <= M or abs(i2-j) <= M )
              for i1 in range(M,N-3*M-1)
              for i2 in range(i1+2*M+1, N-M) )

print( maxSum, timeit.default_timer() - t0 )

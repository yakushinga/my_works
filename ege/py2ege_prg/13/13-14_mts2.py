"""
На каждом километре прямой автодороги расположены N населённых пунктов, которые нужно
обеспечить сотовой связью. У компании хватает денег только на две вышки
сотовой связи в этом районе, причём каждая вышка обеспечивает связь только
в радиусе M км. В первой строке файла input.txt записаны натуральные числа
N – количество населённых пунктов, и M – радиус действия сигнала. В каждой
из следующих N строк записаны два натуральных числа – километровая отметка,
соответствующая населённому пункту, и количество жителей в нём. Определите
наибольшее количество жителей, которых можно обеспечить сотовой связью, если
разместить обе вышки в населённых пунктах.
(Ответ: 13981)
"""
with open('i/input_14.txt') as F:
  N, M = map( int, F.readline().split() )
  data = [ int(s) for s in F ]

s = [0]*N
s[0] = sum(data[0:2*M+1])
for i in range(1,N-M):
  s[i] = s[i-1] - data[i-1]
  if i+2*M < N:
    s[i] += data[i+2*M]

sMax = [0]*N
sMax[0] = s[0]
for i in range(1,N-M):
  sMax[i] = max( sMax[i-1], s[i] )

s2Max = 0
for j in range(2*M+1,N-M):
  s2Max = max( s[j]+sMax[j-2*M-1], s2Max )

print( s2Max )

print('----------------------------------------------')

s = [0]*N
s[0] = sum(data[0:2*M+1])
sMax = [0]*N
sMax[0] = s[0]
for i in range(1,N-M):
  s[i] = s[i-1] - data[i-1]
  if i+2*M < N:
    s[i] += data[i+2*M]
  sMax[i] = max( sMax[i-1], s[i] )

print( max( s[j]+sMax[j-2*M-1]
            for j in range(2*M+1,N-M) ) )


print('----------------------------------------------')

maxSum = 0
for i1 in range(N):
  for i2 in range(i1+2*M+1, N):
    s = 0
    for j in range(N):
      if abs(i1-j) <= M:
        s += data[j]
    for j in range(N):
      if abs(i2-j) <= M:
        s += data[j]
    maxSum = max( s, maxSum )

print( maxSum )

"""
print('----------------------------------------------')

maxSum = 0
for i1 in range(N):
  for i2 in range(i1+2*M+1, N):
    s = 0
    for j in range(N):
      if abs(i1-j) <= M:
        s += data[j]
    for j in range(N):
      if abs(i2-j) <= M:
        s += data[j]
    maxSum = max( s, maxSum )

print( maxSum )
"""
"""
(Демо-2022) Файл input.txt содержит последовательность натуральных чисел. В
первой строке файла записано число N – количество элементов последовательности;
каждая из следующих N строк содержит по одному натуральному числу.
Рассматриваются все её непрерывные подпоследовательности, такие что сумма
элементов каждой из них кратна K = 43. Найдите среди них подпоследовательность
с максимальной суммой, определите её длину. Если таких подпоследовательностей
найдено несколько, в ответе укажите количество элементов самой короткой из них.

Ответ: 1806387 185
"""
with open("i/input_6.txt") as F:
  N = int( F.readline() )
  data = [ int(s) for s in F ]

import timeit

t0 = timeit.default_timer()

K = 43
results = [(0,0)]*N
tailSum = [0] + [None]*(K-1)
tailPos = [-1] + [0]*(K-1)
totalSum = 0
for i in range(N):
  totalSum += data[i]
  r = totalSum % K
  if tailSum[r] is None:
    tailSum[r], tailPos[r] = totalSum, i
  else:
    results[i] = (totalSum - tailSum[r], i - tailPos[r])

results.sort( key = lambda p: (-p[0], p[1]) )

print( *results[0], timeit.default_timer() - t0 )


print('-----------------------------------------')

t0 = timeit.default_timer()

K = 43
results = [(0,0)]*N
tail = [(0,-1)] + [None]*(K-1)
totalSum = 0
for i in range(N):
  totalSum += data[i]
  r = totalSum % K
  if tail[r] is None:
    tail[r] = (totalSum, i)
  else:
    sumR, posR = tail[r]
    results[i] = (totalSum - sumR, i - posR)

results.sort( key = lambda p: (-p[0], p[1]) )

print( *results[0], timeit.default_timer() - t0 )


print('-----------------------------------------')

t0 = timeit.default_timer()

tailSum = [0] + [None]*(K-1)
tailPos = [-1] + [0]*(K-1)
maxSum = totalSum = 0
for i in range(N):
  totalSum += data[i]
  r = totalSum % K
  if tailSum[r] is None:
    tailSum[r], tailPos[r] = totalSum, i
  else:
    s = totalSum - tailSum[r]
    L = i - tailPos[r]
    if s > maxSum or \
       (s == maxSum and  L < minLen):
      maxSum = s
      minLen = L

print( maxSum, minLen, timeit.default_timer() - t0 )

print('-----------------------------------------')

t0 = timeit.default_timer()

tail = [(0,-1)] + [None]*(K-1)
maxSum = totalSum = 0
for i in range(N):
  totalSum += data[i]
  r = totalSum % K
  if tail[r] is None:
    tail[r] = (totalSum, i)
  else:
    s = totalSum - tail[r][0]
    L = i - tail[r][1]
    if s > maxSum or \
       (s == maxSum and  L < minLen):
      maxSum = s
      minLen = L

print( maxSum, minLen, timeit.default_timer() - t0 )


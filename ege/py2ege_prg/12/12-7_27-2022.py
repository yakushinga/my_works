"""
(Демо-2022) Файл input.txt содержит последовательность натуральных чисел. В первой строке
файла записано число N – количество элементов последовательности; каждая из
следующих N строк содержит по одному натуральному числу. Рассматриваются все
её непрерывные подпоследовательности, такие что сумма элементов каждой из них
кратна K = 43. Найдите среди них подпоследовательность с максимальной суммой,
определите её длину. Если таких подпоследовательностей найдено несколько, в
ответе укажите количество элементов самой короткой из них.
(Ответ: 185)
"""
with open("i/input_7.txt") as F:
  N = int( F.readline() )
  data = [ int(s) for s in F ]

K = 43

import timeit

t0 = timeit.default_timer()

maxSum, minLen = 0, float('inf')
for i in range(N):
  for j in range(i,N):
     s = sum( data[i:j+1] )
     if s % K == 0:
       if s > maxSum or \
         (s == maxSum and  j-i+1 < minLen):
         maxSum = s
         minLen = j - i + 1

print( maxSum, minLen, timeit.default_timer() - t0 )

print('---------------------------------')

t0 = timeit.default_timer()

maxSum, minLen = 0, float('inf')
for i in range(N):
  s = 0
  for j in range(i,N):
    s += data[j]
    if s % K == 0:
      if s > maxSum or \
        (s == maxSum and  j-i+1 < minLen):
        maxSum = s
        minLen = j - i + 1

print( maxSum, minLen, timeit.default_timer() - t0 )



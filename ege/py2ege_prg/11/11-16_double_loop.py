"""
Текстовый файл input.txt состоит не более чем из 10^6  заглавных латинских
букв. Определите в этом файле максимальное количество идущих подряд символов,
среди которых подстрока CAT встречается не более 20 раз.

Ответ: 2165
"""
import timeit

s = open('i/input_16.txt').readline()
maxCAT = 20

def valid( subs ):
  return subs.count('CAT') <= maxCAT

t0 = timeit.default_timer()
N = len(s)
maxLen = 0
for L in range(N):
  for R in range(L+maxLen+1, N+1):
    if valid( s[L:R] ):
      maxLen = max( R - L, maxLen )
    else: break

print( maxLen, timeit.default_timer()-t0 )

print('---------------------------------------------')

t0 = timeit.default_timer()
N = len(s)
maxLen = 0
for L in range(N):
  for R in range(L+maxLen+1, N+1):
    if valid( s[L:R] ):
      if R - L > maxLen:
        pos, maxLen = L, R - L
    else: break

print( maxLen, pos, "->", pos+maxLen-1, timeit.default_timer()-t0 )


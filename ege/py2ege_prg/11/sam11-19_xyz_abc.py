"""
Текстовый файл data11-19.txt состоит не более чем из 10^6 символов и
содержит только заглавные буквы латинского алфавита. Определите максимальное
количество идущих подряд символов, среди которых буквы X, Y и Z встречаются
ровно по пять раз, а буквы A, B и C не встречаются совсем.
Ответ: 77
"""
import timeit

s = open('data/data11-19.txt').readline()

def valid( subs ):
  return [ subs.count(c) for c in "XYZABC" ] ==  [5, 5, 5, 0, 0, 0]

def cantBeValid( subs ):
  return subs.count('A')+subs.count('B')+subs.count('C') > 0

t0 = timeit.default_timer()
N = len(s)
maxLen = 0
for L in range(N):
  for R in range(L+maxLen+1, N+1):
    if valid( s[L:R] ):
      if R - L > maxLen:
        maxLen = R - L
        pos = L
    elif cantBeValid( s[L:R] ):
      break

print( maxLen, timeit.default_timer()-t0 )
best = s[pos:pos+maxLen]
print( *[best.count(c) for c in "XYZABC"]  )

"""
Текстовый файл input.txt состоит не более чем из 10^6 символов T, U, V, W,
X, Y и Z. Определите в прилагаемом файле максимальное количество идущих подряд
символов, среди которых символ T встречается ровно 100 раз.

Ответ: 123
"""
import timeit
s = open("i/input_13.txt").readline()

s = s.split('T')
lenS = [ len(p) for p in s ]

t0 = timeit.default_timer()

K = 100
maxLen = 0
for i in range(len(lenS)-K-1):
  L = sum( lenS[i:i+K+1] )
  maxLen = max( L, maxLen )

print( maxLen + K, timeit.default_timer() - t0 )

print('------------------------------------------')

t0 = timeit.default_timer()
maxLen = L = sum( lenS[:K+1] )
for i in range(1, len(lenS)-K-1):
  L = L - lenS[i-1] + lenS[i+K]
  maxLen = max( L, maxLen )

print( maxLen + K, timeit.default_timer() - t0 )

print('------------------------------------------')

s = open("i/input_13.txt").readline()

s = 'T' + s + 'T'

t0 = timeit.default_timer()

posT = []
for i, c in enumerate(s):
  if c == 'T': posT.append(i)

#posT = [-1] + posT + [len(s)]

maxLen = 0
for i in range(len(posT)-K-1):
  maxLen = max( posT[i+K+1] - posT[i] - 1, maxLen )

print( maxLen, timeit.default_timer() - t0 )

print('------------------------------------------')

s = open("i/input_13.txt").readline()

def valid( countT: int ) -> bool:
  return countT == 100
def tooLong( countT: int ) -> bool:
  return countT > 100

countT = 0
maxLen = 0
L = 0
for R in range(len(s)):
  countT += (s[R] == 'T')
  while tooLong( countT ):
    countT -= (s[L] == 'T')
    L += 1
  if valid( countT ):
    maxLen = max( R-L+1, maxLen )

print( maxLen, timeit.default_timer()-t0 )

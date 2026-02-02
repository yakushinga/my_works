"""
Текстовый файл input.txt состоит не более чем из 10^6 символов T, U, V, W,
X, Y и Z. Определите в прилагаемом файле МИНИМАЛЬНОЕ количество идущих подряд
символов, среди которых символ T встречается ровно 100 раз.

Ответ: 102
"""
import timeit
s0 = open("i/input_13.txt").readline()
K = 100

#s0 = "T.........T...T..T.T......T"
#K = 3

s = s0
s = s.split('T')
lenS = [ len(p) for p in s ]

t0 = timeit.default_timer()

minLen = float("inf")
for i in range(len(lenS)-K+1):
  L = sum( lenS[i:i+K-1] )
  minLen = min( L, minLen )

print( minLen + K, timeit.default_timer() - t0 )

print('------------------------------------------')

t0 = timeit.default_timer()
minLen = L = sum( lenS[:K-1] )
for i in range(1, len(lenS)-K+1):
  L = L - lenS[i-1] + lenS[i+K-2]
  minLen = min( L, minLen )

print( minLen + K, timeit.default_timer() - t0 )

print('------------------------------------------')

s = s0

s = 'T' + s + 'T'

t0 = timeit.default_timer()

posT = []
for i, c in enumerate(s):
  if c == 'T': posT.append(i)

#posT = [-1] + posT + [len(s)]

minLen = float("inf")
for i in range(len(posT)-K+1):
  minLen = min( posT[i+K-1] - posT[i] + 1, minLen )

print( minLen, timeit.default_timer() - t0 )

print('------------------------------------------')

s = s0

def valid( countT ):
  return countT == K
def tooLong( c, countT ):
  return countT > K or \
         (countT == K and c != 'T')

countT = 0
minLen = float("inf")
L = 0
for R in range(len(s)):
  countT += (s[R] == 'T')
  while tooLong( s[L], countT ):
    countT -= (s[L] == 'T')
    L += 1
  if valid( countT ):
    minLen = min( R-L+1, minLen )

print( minLen, timeit.default_timer()-t0 )

"""
Текстовый файл input.txt состоит не более чем из 10^6  заглавных латинских
букв. Определите в прилагаемом файле максимальное количество идущих подряд
символов, среди которых символ T встречается не более 20 раз, а
символ E – не более 15 раз.

Ответ: 625
"""
import timeit
s = open('i/input_15.txt').readline()
maxT = 20
maxE = 15

#s = "AAATAAATAAEATAAATAAATAAATAAEATAAATAAATEAAATAAATAAAT"
#maxT = 3
#maxE = 2


def valid( countT, countE ):
  return countT <= maxT and countE <= maxE

t0 = timeit.default_timer()
N = len(s)
maxLen = 0
for L in range(N):
  countT = countE = 0
  for R in range(L, N):
    if s[R] == 'T': countT += 1
    if s[R] == 'E': countE += 1
    if not valid( countT, countE ): break
    maxLen = max( R - L + 1, maxLen )

print( maxLen, timeit.default_timer()-t0 )

print('----------------------------------')

t0 = timeit.default_timer()
N = len(s)
maxLen = 0
for L in range(N):
  countT = countE = 0
  for R in range(L, N):
    if s[R] == 'T': countT += 1
    if s[R] == 'E': countE += 1
    if not (countT <= maxT and countE <= maxE): break
    maxLen = max( R - L + 1, maxLen )

print( maxLen, timeit.default_timer()-t0 )

print('----------------------------------')

t0 = timeit.default_timer()

countT = countE = 0
maxLen = 0
L = 0
for R in range(len(s)):
  if s[R] == 'T': countT += 1
  if s[R] == 'E': countE += 1
  while not valid( countT, countE ):
    if s[L] == 'T': countT -= 1
    if s[L] == 'E': countE -= 1
    L += 1
  if R - L + 1 > maxLen:
    maxLen = R - L + 1
    #print( maxLen, s[L:R+1], s[L:R+1].count('T'),  s[L:R+1].count('E') )
  #maxLen = max( R - L + 1, maxLen )

print( maxLen, timeit.default_timer()-t0 )

print('----------------------------------')

t0 = timeit.default_timer()

countT = countE = 0
maxLen = 0
L = 0
for R in range(len(s)):
  if s[R] == 'T': countT += 1
  if s[R] == 'E': countE += 1
  while not (countT <= maxT and countE <= maxE):
    if s[L] == 'T': countT -= 1
    if s[L] == 'E': countE -= 1
    L += 1
  if R - L + 1 > maxLen:
    maxLen = R - L + 1
    #print( maxLen, s[L:R+1], s[L:R+1].count('T'),  s[L:R+1].count('E') )
  #maxLen = max( R - L + 1, maxLen )

print( maxLen, timeit.default_timer()-t0 )

print('----------------------------------')

t0 = timeit.default_timer()

N = len(s)
countT, countE = [0]*(N+1), [0]*(N+1)
for i in range(1,N+1):
  countT[i] = countT[i-1] + (s[i-1] == 'T')
  countE[i] = countE[i-1] + (s[i-1] == 'E')

def valid():
  return (countT[R]-countT[L] <= 20) and \
         (countE[R]-countE[L] <= 15)

maxLen = 0
L = 0
for R in range(1,N+1):
  while not valid():
    L += 1
  maxLen = max( R-L, maxLen )

print( maxLen, timeit.default_timer()-t0 )


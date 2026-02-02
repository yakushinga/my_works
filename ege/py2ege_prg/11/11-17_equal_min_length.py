"""
Текстовый файл input.txt состоит не более чем из 10^6  заглавных латинских
букв. Определите в этом файле МИНИМАЛЬНОЕ количество идущих подряд символов,
среди которых подстрока CAT встречается ровно 20 раз, а слово DOG - ровно 30 раз.

Ответ: 803
----------------------------------------------------------------
!!! Время работы каждой из двух частей программы - 5-7 минут !!!
----------------------------------------------------------------
"""
import timeit
s = open("i/input_16.txt").readline()

nCAT = 20
nDOG = 30

#s = 'CATCATDOGDOGDOG'
#nCAT, nDOG = 2, 3

def valid( subs ):
  return subs.count("CAT") == nCAT and \
         subs.count("DOG") == nDOG

len0 = nCAT*len("CAT") + nDOG*len("DOG")

t0 = timeit.default_timer()
N = len(s)
minLen = 1000
for L in range(N):
  for R in range( L+len0, min(L+minLen,N+1) ):
    if valid( s[L:R] ):
      minLen = min( R-L, minLen )
      break

print( minLen, timeit.default_timer()-t0 )

t0 = timeit.default_timer()
N = len(s)
minLen = 1000
for L in range(N):
  for R in range( min(L+minLen,N)-1, L+len0-1, -1):
    if valid( s[L:R] ):
      minLen = min( R-L, minLen )

print( minLen, timeit.default_timer()-t0 )


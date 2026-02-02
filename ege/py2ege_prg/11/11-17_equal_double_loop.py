"""
Текстовый файл input.txt состоит не более чем из 10^6  заглавных латинских
букв. Определите в этом файле максимальное количество идущих подряд символов,
среди которых подстрока CAT встречается ровно 20 раз, а слово DOG - ровно 30 раз.

Ответ: 2028
"""
import timeit
s = open("i/input_16.txt").readline()

nCAT = 20
nDOG = 30

def valid( subs ):
  return subs.count("CAT") == nCAT and \
         subs.count("DOG") == nDOG
def cantBeValid( subs ):
  return subs.count("CAT") > nCAT or \
         subs.count("DOG") > nDOG

t0 = timeit.default_timer()
N = len(s)
maxLen = 0
for L in range(N):
  for R in range(L+maxLen+1, N):
    if valid( s[L:R] ):
      if R-L > maxLen:
        maxLen = R - L
        pos = L
    elif cantBeValid( s[L:R] ):
      break

print( maxLen, pos, timeit.default_timer()-t0 )

sMax = s[pos:pos+maxLen]
print( "CAT:", sMax.count("CAT"), "DOG:", sMax.count("DOG") )



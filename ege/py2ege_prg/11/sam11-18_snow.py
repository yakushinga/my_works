"""
Текстовый файл data11-18.txt состоит не более чем из 10^6 заглавных латинских букв.
Определите в этом файле максимальную длину подстроки, которая заканчивается на
букву F и в которой слово SNOW встречается ровно 160 раз.
Ответ: 5359
"""
import timeit

s = open('data/data11-18.txt').readline()

maxSNOW = 160

def valid( subs ):
  return subs.count('SNOW') <= maxSNOW and subs[-1] == 'F'

t0 = timeit.default_timer()
N = len(s)
maxLen = 0
for L in range(N):
  for R in range(L+maxLen+1, N+1):
    if valid( s[L:R] ):
      if R-L > maxLen:
        maxLen = R - L
        pos = L
    else: break

print( maxLen, timeit.default_timer()-t0 )
print( s[pos:pos+maxLen].count('SNOW') )

"""
Текстовый файл input.txt состоит не более чем из 10^6 символов и содержит только
десятичные цифры и заглавные латинские буквы. Найдите в этом файле последовательность
наибольшей длины идущих подряд символов, представляющих собой 12-ричную запись
максимального нечётного числа. Если таких последовательностей несколько, выберите
последовательность с наименьшим числовым значением. В  ответе запишите индекс
первого символа (первой значащей цифры), с которого начинается запись этого
числа в файле. Нумерация символов в файле начинается с нуля.

Ответ: 765537
"""
import timeit
s0 = open('i/input_18.txt').readline()

s = s0

def isNum12( subs ):
  return subs[0] != '0' and \
         all( c in '0123456789AB' for c in subs )
def valid( subs ):
  return subs[-1] in '13579B'

t0 = timeit.default_timer()

N = len(s)
maxLen, minValue = 1, 12
for L in range(N):
  for R in range(L+maxLen, N+1):
    if isNum12( s[L:R] ):
      if valid( s[L:R] ):
        v = int(s[L:R], 12)
        if R-L > maxLen:
          print( R-L, s[L:R], v)
          pos, maxLen, minValue = L, R - L, v
        elif R-L == maxLen:
          print( R-L, s[L:R], v)
          if v < minValue:
            pos, maxLen, minValue = L, R - L, v
    else:
      break

print( pos, maxLen, s[pos:pos+maxLen], minValue, timeit.default_timer()-t0 )

print('-----------------------------------------')

s = s0
t0 = timeit.default_timer()

N = len(s)
maxLen, minValue = 1, 12
for L in range(N):
  for R in range(L+maxLen, N+1):
    if isNum12( s[L:R] ):
      if valid( s[L:R] ):
        v = int(s[L:R], 12)
        if R-L > maxLen or \
           R-L == maxLen and v < minValue:
          #pos, maxLen, minValue = L, R - L, v
          pos = L
          maxLen = R - L
          minValue = v
    else:
      break

print( pos, maxLen, s[pos:pos+maxLen], minValue, timeit.default_timer()-t0 )

print('-----------------------------------------')

s = s0
t0 = timeit.default_timer()

N = len(s)
best = 'C'
for L in range(N):
  for R in range(L+len(best), N+1):
    if isNum12( s[L:R] ):
      if valid( s[L:R] ):
        if R-L > len(best) or \
           R-L == len(best) and s[L:R] < best:
           best = s[L:R]
    else:
      break

print( s.find(best), len(best), best, int(best, 12), timeit.default_timer()-t0 )

print('-----------------------------------------')

s = s0
t0 = timeit.default_timer()

N = len(s)
results = []
for L in range(N):
  for R in range(L+1, N+1):
    if isNum12( s[L:R] ):
      if valid( s[L:R] ):
        results.append( s[L:R] )
    else:
      break

best = max( results, key= lambda x: (len(x), -int(x,12)) )

print( s.find(best), len(best), best, int(best, 12), timeit.default_timer()-t0 )

print('-----------------------------------------')

from re import findall

s = s0

t0 = timeit.default_timer()
num12 = r'[1-9AB][0-9AB]*[13579B]'
pattern = fr'(?=({num12}))'
parts = findall( pattern, s )
best = max( parts, key=lambda p: (len(p), -int(p,12))  )
print( s.find(best), len(best), best, int(best, 12), timeit.default_timer()-t0 )

print('-----------------------------------------')

from re import findall

s = s0

def int12( s ):
  return int(s, 12)

t0 = timeit.default_timer()
pattern = r'[1-9AB][0-9AB]*[13579B]'
parts = findall( pattern, s )
maxLen = max( len(p) for p in parts  )
pMaxLen = [ p for p in parts if len(p) == maxLen ]
#best = min( pMaxLen, key=int12 )
best = min( pMaxLen )
print( s.find(best), maxLen, best, int12(best), timeit.default_timer()-t0 )


"""
Текстовый файл data11-20.txt состоит не более чем из 10^6 символов
и содержит только десятичные цифры и заглавные буквы латинского алфавита. Определите
в этом файле последовательность идущих подряд символов, представляющих собой
16-ричную запись максимального числа, кратного четырём. В ответе запишите индекс
(номер) первого символа (первой значащей цифры), с которого начинается запись
этого числа в прилагаемом файле. Нумерация символов в текстовом файле начинается
с нуля.
Ответ: 13270
"""
import timeit

s = open('data/data11-20.txt').readline()

def isNum16( subs ):
  return subs[0] != '0' and \
         all( c in '0123456789ABCDEF' for c in subs )
def valid( subs ):
  return subs[-1] in '048C'

t0 = timeit.default_timer()

N = len(s)
maxLen, maxValue = 1, -1
for L in range(N):
  for R in range(L+maxLen, N+1):
    if isNum16( s[L:R] ):
      if valid( s[L:R] ):
        v = int(s[L:R], 16)
        if v > maxValue:
          pos = L
          maxLen = R - L
          maxValue = v
    else:
      break

print( pos, maxLen, s[pos:pos+maxLen], timeit.default_timer()-t0 )

print( '----------------------------' )

from re import findall

t0 = timeit.default_timer()

num16 = r'[1-9A-F][0-9A-F]*[048C]'
pattern = fr'(?=({num16}))'
parts = findall( pattern, s )
sMax = max( parts, key=lambda x: int(x,16)  )

print( s.find(sMax), len(sMax), sMax, timeit.default_timer()-t0)

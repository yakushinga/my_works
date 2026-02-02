"""
(Демо-2023) Текстовый файл input.txt состоит не более чем из 10^6 символов
A, C, D, F и O. Определите максимальное количество идущих подряд
пар символов вида «согласная + гласная».
"""
s = open("i/input_11.txt").readline()

"""
for pair in ["CA","DA","FA","CO","DO","FO"]:
  s = s.replace( pair, '*')

for sog in "CDF":
  for glas in "AO":
    s = s.replace( sog+glas, '*')

from itertools import product
for sog, glas in product("CDF", "AO"):
    s = s.replace( sog+glas, '*')
"""
s = s.replace('D','C').replace('F','C') \
     .replace('O','A').replace("CA",'*')

L = 1
while L*'*' in s:
  L += 1

print( L - 1 )

#----------------------------------------

q = '*'
while q in s:
  q += '*'

print( len(q) - 1 )
#----------------------------------------

maxLen = L = 0
for c in s:
  if c == '*':
    L += 1
    maxLen = max( L, maxLen )
  else:
    L = 0

print( maxLen )

#----------------------------------------

L = [0]*len(s)
for i, c in enumerate(s):
  if c == '*':
    L[i] = L[i-1] + 1
  else:
    L[i] = 0

print( max(L) )


#----------------------------------------
import re

s = open("i/input_11.txt").readline()

parts = re.findall( "(?:[CDF][AO])+", s )
sMax = max( parts, key=len )
print( len(sMax) // 2 )


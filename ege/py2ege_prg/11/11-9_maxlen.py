"""
Текстовый файл input.txt состоит не более чем из 10^6 символов X, Y, Z.
Определите максимальное количество идущих подряд символов X.
"""
s = open("i/input_9.txt").readline()

L = 1
while L*'X' in s:
  L += 1

print( L - 1 )

#----------------------------------------

q = 'X'
while q in s:
  q += 'X'

print( len(q) - 1 )
#----------------------------------------

maxLen = L = 0
for c in s:
  if c == 'X':
    L += 1
    maxLen = max( L, maxLen )
  else:
    L = 0

print( maxLen )

#----------------------------------------

L = [0]*len(s)
for i, c in enumerate(s):
  if c == 'X':
    L[i] = L[i-1] + 1
  else:
    L[i] = 0

print( max(L) )

#----------------------------------------
#s = s.replace('Y', ' ')
#s = s.replace('Z', ' ')

#s = s.replace('Y', ' ').replace('Z', ' ')

for c in 'YZ':
  s = s.replace(c, ' ')

print( max( len(p) for p in s.split() ) )

s = s.split()
L = [ len(p) for p in s ]
print( max(L) )


#----------------------------------------
import re

s = open("i/input_9.txt").readline()

parts = re.findall( "X+", s )
sMax = max( parts, key=len )
print( len(sMax) )

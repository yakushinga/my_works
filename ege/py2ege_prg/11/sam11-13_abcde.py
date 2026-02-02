"""
Текстовый файл data11-9.txt состоит не более чем из 10^6 заглавных латинских
букв. Определите максимальное количество идущих подряд символов, среди есть
только буквы A, B, C, D и E.
(Ответ: 9)
"""
s = open('i/data11-9.txt').readline()

maxLen = L = 0
for c in s:
  if c in 'ABCDE':
    L += 1
    maxLen = max( L, maxLen )
  else:
    L = 0

print( maxLen )

#-----------------------------------------------

import string

for c in 'BCDE':
  s = s.replace( c, 'A' )
for c in string.ascii_uppercase:
  if c not in 'ABCDE':
    s = s.replace( c, ' ' )

print(  max( len(p) for p in s.split() ) )

"""
Текстовый файл data11-11.txt состоит не более чем из 10^6 заглавных латинских
букв. Определите минимальную длину подстроки, в которой
символ Z встречается не менее 50 раз.
(Ответ: 890)
"""
s = open('i/data11-11.txt').readline()

N = 50

Zpos = []
minLen = 10**10
for i, c in enumerate(s):
  if c == 'Z':
    Zpos.append( i )
    if len(Zpos) >= N:
      L = i - Zpos[-N] + 1
      minLen = min( L, minLen )

print( minLen )

#-----------------------------------------
# Автор: А. Кабанов

s = s.split('Z')
minLen = 10**10
for i in range(len(s)-N-1):
  c = 'Z' + 'Z'.join(s[i+1:i+N]) + 'Z'
  minLen = min( len(c), minLen )

print( minLen )


"""
Текстовый файл data11-10.txt состоит не более чем из 10^6 заглавных латинских
букв. Определите максимальное коли-чество идущих подряд символов, среди
которых нет сочетания NO.
(Ответ: 3349)
"""
s = open('i/data11-10.txt').readline()

prev, L, maxLen = "_", 0, 0
for c in s:
  if prev + c == 'NO':
    L = 1
  else:
    L += 1
    maxLen = max( L, maxLen )
  prev = c

print( maxLen )

#-----------------------------------------------

maxLen = L = 0
for cur, nxt in zip(s, s[1:]):
  if cur + nxt == 'NO':
    L = 1
  else:
    L += 1
    maxLen = max(L, maxLen)

print( maxLen )

#-----------------------------------------------

while 'NO' in s:
  s = s.replace('NO', 'N O')

print(  max( len(p) for p in s.split() ) )

"""
Текстовый файл  data10-1.txt состоит не более чем из 10^6 символов X, Y и Z.
Определите максимальное количество идущих подряд одинаковых символов в этом файле.
(Ответ: 15)
"""
s = open("data/data10-1.txt").read()

maxLen = L = 0
prev = ''
for c in s:
  if c == prev:
    L += 1
    maxLen = max( L, maxLen )
  else:
    L = 1
  prev = c

print( maxLen )

#---------------------------------

s = open("data/data10-1.txt").read()

maxLen = 0
for c in 'XYZ':
  xx = c
  while xx in s:
    xx += c
  maxLen = max( maxLen, len(xx)-1 )

print( maxLen )

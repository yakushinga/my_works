"""
(Демо-2021) Текстовый файл input.txt состоит не более чем из 10^6 символов
X, Y и Z. Определите максимальное количество идущих подряд символов,
среди которых каждые два соседних различны.
"""
s = open("i/input_10.txt").readline()

maxLen = L = 1
for i in range(1, len(s)):
  if s[i] != s[i-1]:
    L += 1
    maxLen = max( L, maxLen )
  else:
    L = 1

print( maxLen )

#----------------------------------------

maxLen = L = 1
prev = ''
for c in s:
  if prev:
    if c != prev:
      L += 1
      maxLen = max( L, maxLen )
    else:
      L = 1
  prev = c

print( maxLen )

#----------------------------------------
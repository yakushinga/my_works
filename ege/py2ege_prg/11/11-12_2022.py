"""
Текстовый файл input.txt состоит не более чем из 10^6  символов P, Q, R и S.
Определите максимальное количество идущих подряд символов, среди которых
нет идущих подряд символов P.
"""
s = open('i/input_12.txt').readline()

s = s.replace('PP', 'P P') \
     .replace('PP', 'P P')
s = s.split()

print(  max( len(p) for p in s ) )


#-----------------------------------------------

s = open('i/input_12.txt').readline()
while 'PP' in s:
  s = s.replace('PP', 'P P')

print(  max( len(p) for p in s.split() ) )

#-----------------------------------------------

s = open('i/input_12.txt').readline()
prev, L, maxLen = "_", 0, 0
for c in s:
  if prev == c == 'P':
    L = 1
  else:
    L += 1
    maxLen = max( L, maxLen )
  prev = c

print( maxLen )

#-----------------------------------------------

s = open('i/input_12.txt').readline()
maxLen = L = 0
for prev, c in zip(s, s[1:]):
  if prev+c == 'PP':
    L = 1
  else:
    L += 1
    maxLen = max(L, maxLen)

print( maxLen )


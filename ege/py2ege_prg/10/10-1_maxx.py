"""
Текстовый файл input.txt состоит не более чем из 10^6 символов X, Y и Z.
Определите количество символов X в этом файле.
"""
s = open("i/input_1.txt").read()

countX = 0
for i in range(len(s)):
  if s[i] == 'X':
    countX += 1

print( countX )

#---------------------------------

s = open("i/input_1.txt").read()

countX = 0
for c in s:
  if c == 'X':
    countX += 1

print( countX )

#---------------------------------

s = open("i/input_1.txt").read()

countX = 0
for c in s:
  countX += (c == 'X')

print( countX )

#---------------------------------

s = open("i/input_1.txt").read()

print( sum( (c == 'X') for c in s ) )

print( s.count('X') )
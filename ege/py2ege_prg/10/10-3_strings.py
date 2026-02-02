"""
Текстовый файл input.txt состоит не более чем из 10^6 латинских букв. Текст
разбит на строки разной длины. Найдите строку, в которой буква X встречается
чаще всего. Если таких строк несколько, нужно взять ту, которая встретилась
в файле раньше. Определите букву, которая встречается в этой строке чаще
всего. Если таких букв несколько, выведите ту, которая стоит после остальных в
алфавите.
(Ответ: B 6)
"""
maxX = 0
sMax = ""
for s in open("i/input_3.txt") :
  countX = s.count('X')
  if countX > maxX:
    maxX = countX
    sMax = s

print( sMax, maxX )

import string
maxCount = 0
#for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
for c in string.ascii_uppercase:
  count = sMax.count( c )
  if count >= maxCount:
    maxCount = count
    cMax = c

print( cMax, maxCount )



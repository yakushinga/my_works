"""
Текстовый файл data10-3.txt состоит не более чем из 10^6 латинских букв. Текст
разбит на строки разной длины. Найдите строку, в которой буква X встречается
реже всего. Если таких строк несколько, нужно взять ту, которая встретилась
в файле позже. Определите пару соседних букв, которая встречается в этой строке
чаще всего. Если таких пар букв несколько, выведите ту, которая стоит после
остальных в алфавите.
(Ответ: ZX)
"""
minX = 10**10
for s in open("data/data10-3.txt") :
  countX = s.count('X')
  if countX <= minX:
    minX = countX
    sMin = s

print( sMin, minX )

s = sMin

maxCount = 0
for i in range(len(s)-1):
  count = sMin.count( s[i:i+2] )
  if count > maxCount:
    maxCount = count
    maxPair = { s[i:i+2] }
  elif count == maxCount:
    maxPair.add( s[i:i+2] )

maxPair = sorted( maxPair, reverse = True )

print( maxPair[0] )



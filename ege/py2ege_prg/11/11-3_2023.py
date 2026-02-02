"""
Для кодирования некоторой последовательности, состоя-щей из букв А, К, Л, О,
C, Т решили использовать неравномерный двоичный код, для которого выполняется
условие Фано. Для букв А и К использовали соответственно кодовые слова 10, 111.
Какое количество двоичных знаков потребуется для кодирования слова КОЛОКОЛ,
если известно, что оно закодировано минимально возможным количеством двоичных
знаков?
"""
from itertools import product

known = "10 111".split()

allCodes = []
for L in range(1,5):
  allCodes.extend( [ s for code in product('01', repeat=L)
                       if (s:=''.join(code)) not in known ] )

def fano( codes ):
  for a in codes:
    for b in codes:
      if a != b and a.startswith(b):
        return False
  return True

def fano( codes ):
  return all( not a.startswith(b)
              for a in codes for b in codes
              if a != b )

freeCodes = []
for code in allCodes:
  if fano( [code] + freeCodes + known ):
    freeCodes.append( code )

print( freeCodes )

def addCodes( code, maxLen ):
   return [] if len(code) > maxLen else \
          [code] + addCodes(code+'0', maxLen)  \
                 + addCodes(code+'1', maxLen)

def addCodes( code, maxLen ):
   if len(code) > maxLen: return []
   return [code] + addCodes(code+'0', maxLen)  \
                 + addCodes(code+'1', maxLen)

for code in freeCodes[:]:
  #freeCodes.extend( addCodes(code, 4) )
  freeCodes.extend( addCodes(code+'0', 4) )
  freeCodes.extend( addCodes(code+'1', 4) )

from itertools import permutations
minLen = 1000
for codes in permutations(freeCodes, 4):
   if fano( known + list(codes) ):
      L = 2*3 + 2*len(codes[0]) + 3*len(codes[1])
      if L < minLen:
        minLen = L
        print( codes, L )

from itertools import permutations

print( min( 2*3 + 2*len(codes[0]) + 3*len(codes[1])
            for codes in permutations(freeCodes, 4)
            if fano( known + list(codes) )  ) )

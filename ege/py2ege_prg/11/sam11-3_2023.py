"""
По каналу связи передаются сообщения, содержащие только буквы из набора:
А, З, К, Н, Ч. Для передачи используется двоичный код, удовлетворяющий
условию Фано. Кодовые слова для некоторых букв известны: Н – 1111, З – 110.
Для трёх оставшихся букв А, К и Ч кодовые слова неизвестны. Какое количество
двоичных знаков потребуется для кодирования слова КАЗАЧКА, если известно, что
оно закодировано минимально возможным количеством двоичных знаков?
(Ответ: 14)
"""
from itertools import product

known = "1111 110".split()

allCodes = []
for L in range(1,5):
  allCodes.extend( [ s for code in product('01', repeat=L)
                       if (s:=''.join(code)) not in known ] )

def fano( codes ):
  for a in codes:
    for b in codes:
      if a != b and a.startswith(b): # or b.startswith(a)):
        return False
  return True

def fano( codes ):
  return all( not a.startswith(b) #or b.startswith(a))
              for a in codes for b in codes
              if a != b )

freeCodes = []
for code in allCodes:
  if fano( [code] + freeCodes + known ):
    freeCodes.append( code )

print( freeCodes )

def addCodes( code, maxLen = 4 ):
   return [] if len(code) > maxLen else \
          [code] + addCodes(code+'0', maxLen)  \
                 + addCodes(code+'1', maxLen)

for code in freeCodes[:]:
  freeCodes.extend( addCodes(code+'0') )
  freeCodes.extend( addCodes(code+'1') )

from itertools import product
minLen = 100
for codes in product(freeCodes, repeat=3):
   if len(set(codes)) == 3 and \
      fano( known + list(codes) ):
      L = 3 + 3*len(codes[0]) + 2*len(codes[1]) + len(codes[2])
      if L < minLen:
        minLen = L
        print( codes, L )


"""
(Демо-2022) Для кодирования некоторой последовательности, состоящей из букв
Л, М, Н, П, Р, решили использовать неравномерный двоичный код, удовлетворяющий
условию Фано. Для букв Л, М, Н использовали соответственно кодовые слова
00, 01, 11. Для двух оставшихся букв П и Р кодовые слова неизвестны. Укажите
кратчайшее возможное кодовое слово для буквы П, при котором код будет
удовлетворять условию Фано. Если таких кодов несколько, укажите код с
наименьшим числовым значением.
(Ответ: 100)
"""
from itertools import product

known = "00 01 11".split()

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

def aAll( codes ):
  return all( not a.startswith(b) # or b.startswith(a))
              for a in codes for b in codes
              if a != b )

freeCodes = []
for code in allCodes:
  if aAll( [code] + freeCodes + known ):
    freeCodes.append( code )

if len(freeCodes) == 1:
  print( freeCodes[0] + '0' )
else:
  print( freeCodes[0] )



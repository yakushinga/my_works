"""
(Демо-2024) По каналу связи передаются сообщения, содержащие только восемь
букв: А, Б, В, Г, Д, Е, Ж и З. Для передачи используется двоичный код,
удовлетворяющий условию Фано. Кодовые слова для некоторых букв известны:
А – 000, Б – 001, В – 0101, Г – 0100, Д – 011, Е – 101. Какое наименьшее
количество двоичных знаков потребуется для кодирования двух оставшихся букв?
В ответе запишите суммарную длину кодовых слов для букв: Ж, З.
(Ответ: 5)
"""
from itertools import product

known = "000 001 0101 0100 011 101".split()

allCodes = []
for L in range(1,5):
  allCodes.extend( [ s for code in product('01', repeat=L)
                       if (s:=''.join(code)) not in known ] )

def fano( codes ):
  for a in codes:
    for b in codes:
      if a != b and a.startswith(b): #or b.startswith(a)):
        return False
  return True

def fano( codes ):
  return all( not a.startswith(b) # or b.startswith(a))
              for a in codes for b in codes
              if a != b )

freeCodes = []
for code in allCodes:
  if fano( [code] + freeCodes + known ):
    freeCodes.append( code )

print( freeCodes )

if len(freeCodes) == 1:
  print( 2*len(freeCodes[0]) + 2 )
else:
  print( sum( len(c) for c in freeCodes[:2] ) )



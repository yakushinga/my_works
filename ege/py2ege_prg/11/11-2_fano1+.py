"""
По каналу связи передаются только буквы русского алфавита, закодированные
неравномерным двоичным кодом, для которого выполняется условие Фано.
Кодовые слова для некоторых букв известны: А – 00, Б – 01, В – 110, Г – 101,
Д – 100. Укажите возможный код минимальной длины для буквы Я. Если таких
кодов несколько, укажите тот из них, который имеет максимальное числовое значение.
"""
from itertools import product

known = "00 01 110 101 100".split()

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


"""
По каналу связи передаются сообщения, содержащие только буквы А, Б, В и Г. Для
передачи используется двоичный код, для которого выполняется условие Фано.
Кодовые слова для некоторых букв известны: А – 1, Б – 010, В – 000. Укажите
кратчайшее кодовое слово для буквы Г, при котором код будет допускать
однозначное декодирование. Если таких кодов несколько, укажите код с
наименьшим числовым значением.
"""
known = "1 010 000".split()
known = [ '1', '010', '000' ]

from itertools import product
allCodes = []
for L in range(1,5):
  allCodes.extend( [ s for code in product('01', repeat=L)
                       if (s:=''.join(code)) not in known ] )

allCodes = []
for L in range(1,5):
  for code in product('01', repeat=L):
    s = ''.join( code )
    if s not in known:
      allCodes.append( s )

allCodes = [ s for L in range(1,5)
                 for code in product('01', repeat=L)
                   if (s:=''.join(code)) not in known ]

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

for code in allCodes:
  if fano( [code] + known ):
    print( code )

print('----------------------------------')

print( [ code for code in allCodes
              if fano( [code] + known) ][0] )


"""
Демо-2025
Текстовый файл состоит из цифр 0, 6, 7, 8, 9 и знаков «–» и «*». Определите
максимальное количество символов в непрерывной последовательности, которая является
корректным арифметическим выражением с целыми неотрицательными числами.

Ответ: 140
"""
from timeit import default_timer

s0 = open('i/input_14.txt').readline()

#s0 = '1---1234'
#s0 = '1-000000000000000000001234'
#s0 = '00088690-000*88*123-60960'
#s0 = '*2--*006*00000*1*20-4*05'
#s0 = '*2--*0000*1*20-4*05'
s0 = '123*'

#---------------------------------------------------------
# Решение с помощью замен
#---------------------------------------------------------
t0 = default_timer()
s = s0

s = ' ' + s + ' '

for d in '6789':
  s = s.replace( d, '1' )

s = s.replace( '-', '*' )

s = s.replace( '**', ' ' )
s = s.replace( ' *', ' ' )
s = s.replace( '* ', ' ' )

s = s.replace('*00', '*0 0')
s = s.replace('*01', '*0 1')

while ' 00' in s:
  s = s.replace(' 00', ' 0')

s = s.replace( ' 01', ' 0 1')

sMax = max( s.split(), key=len )

print( len(sMax), default_timer()-t0, sMax )

print( '---------------------------' )

#---------------------------------------------------------
# Решение однократным проходом по строке O(N)
#---------------------------------------------------------

t0 = default_timer()
s = s0

prev2 = prev = ''
sub = ''
maxLen = 0
for c in s:
  if c in '-*' and \
     (sub == '' or prev in '-*'):
    sub = prev = c = ''
  elif prev2 in '-*' and prev == '0' and c in '0123456789':
    sub = c
    prev = ''
  else:
    sub += c
  if c not in '-*':
    if len(sub) > maxLen:
      sMax = sub
    maxLen = max( len(sub), maxLen )
  prev2, prev = prev, c

print( maxLen, default_timer()-t0, sMax )

print( '---------------------------' )

#---------------------------------------------------------
# Решение путем замен и обработки блоков
#---------------------------------------------------------

s = s0
t0 = default_timer()
s = s.replace('-', '*').split('*')

sMax, maxLen = '', 0
sub = ""
for chunk in s:
  if not chunk:
    sub = ""
  elif chunk[0] != '0' or chunk == '0':
    sub += chunk + '*'
  else: # тут chunk[0] == '0'
    sub += '0'
    if len(sub) > maxLen:
      #  print( len(sub), sub )
      sMax = sub
    maxLen = max( len(sub), maxLen )
    chunk = chunk.lstrip('0')
    sub = chunk+'*' if chunk else '0*'
  if len(sub)-1 > maxLen:
    #  print( len(sub)-1, sub[:-1] )
    sMax = sub[:-1]
  maxLen = max( len(sub)-1, maxLen )

print( maxLen, default_timer()-t0, sMax )

print( '---------------------------' )

#---------------------------------------------------------
# Решение с помощью регулярных выражений
#---------------------------------------------------------

from re import findall
s = s0
t0 = default_timer()
number = r"(?:[1-9]\d*|0)"
pattern = fr"{number}(?:[-*]{number})*"
parts = findall( pattern, s )
sMax = max( parts, key=len )

print( len(sMax), default_timer()-t0, sMax )

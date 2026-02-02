"""
ЕГЭ-2024 (b) Выражения, равные нулю
Текстовый файл содержит только десятичные цифры, а также знаки «+» и «*».
Определите максимальное количество символов в непрерывной последовательности, являющейся
корректным арифметическим выражением с целыми неотрицательными числами (без знака),
значение которого равно нулю. В этом выражении никакие два знака арифметических
операций не стоят рядом, порядок действий определяется по правилам математики.
В записи чисел отсутствуют незначащие (ведущие) нули. В ответе укажите количество
символов в найденном выражении.

Ответ: 126
"""

from timeit import default_timer

s0 = open('i/input_20.txt').readline()

#s0 = '0+++++0*1+2+3+0*2'
#s0 = '1234++*0*12+11210*99*0*198*77+10*8'
#s0 = '10*2*00000000003*0*4'
#s0 = '100000000001+0*255'
#s0 = '100000000001+255'
#s0 = '00000000001'

def isZero( expr ):
  if any( expr.startswith(x) for x in ['+', '*', '00', '01']) or \
     any( expr.endswith(x) for x in '+*') or \
     any( x in expr
         for x in ['**', '++', '-*', '*-', '*00', '*01', '+00', '+01'] ):
    return False
  return eval(expr) == 0

#---------------------------------------------------------
# Решение с помощью регулярных выражений
# Автор: Е. Джобс
#---------------------------------------------------------

s = s0

from re import findall

t0 = default_timer()

number = r'(?:[1-9]\d*|0)'
product = fr'(?:(?:{number}\*)*0(?:\*{number})*)'
pattern = fr'{product}(?:\+{product})*'
parts = findall( pattern, s )
sMax = sorted( parts, key=len, reverse=True )[0]

print( len(sMax), sMax )
print( default_timer()-t0 )

print( '----------------------' )

#---------------------------------------------------------
# Самое медленное решение
#---------------------------------------------------------

s = s0

if len(s) < 100:
  t0 = default_timer()
  for d in '23456789':
    s = s.replace( d, '1' )

  sMax, maxLen = '', 0
  L = len(s)
  for i in range(L):
    for j in range(i+1, L+1):
      if isZero(s[i:j]):
        if j - i > maxLen:
          sMax = s[i:j]
          maxLen = j - i

  print( maxLen, sMax )
  print( default_timer()-t0 )

  print( '----------------------' )

#---------------------------------------------------------
# Тоже медленное решение, но лучше
#---------------------------------------------------------

s = s0

if len(s) < 1000:
  t0 = default_timer()

  for d in '23456789':
    s = s.replace( d, '1' )

  for wrong in ['++','+*','*+','**']:
    s = s.replace( wrong, ' ')

  sMax, maxLen = '', 0
  for part in s.split():
    L = len(part)
    for i in range(L):
      for j in range(i+1, L+1):
        if isZero(part[i:j]):
          if j - i > maxLen:
            sMax = part[i:j]
            maxLen = j - i

  print( maxLen, sMax )
  print( default_timer()-t0 )

  print( '----------------------' )

#---------------------------------------------------------
# Решение однократным проходом по строке O(N)
# Конечный автомат
#---------------------------------------------------------

s = s0

t0 = default_timer()

def check( expr ):
  global maxLen, sMax
  sZero = []
  for t in expr.split('+'):
    if '*0' in t or t.startswith('0'):
      sZero.append( t )
    elif '0*' in t:
      k = t.find( '0*' )
      sZero = [ t[k:] ]
    elif t.endswith('0'):
      sZero = [ t[-1]  ]
    else:
      sZero = []
    curLen = len( '+'.join(sZero) )
    if curLen > maxLen:
      sMax = sZero
      # print( curLen-1, sZero )
      maxLen = max( curLen, maxLen )

digits = '0123456789'
if '0' in s:
  sMax, maxLen = '0', 0
else:
  sMax, maxLen = '', 0
state = 0 # wait digit
sub = ''
for c in s:
  if state == 0:
    if c in digits:
      sub += c
      check( sub )
      if c == '0':
        state = 2 # wait operation
      else:
        state = 1 # wait digit or operation
    else:
      sub = ''
  elif state == 1:
    if c in digits:
      sub += c
      check( sub )
    else:
      sub += c
      state = 0
  else:
    if c in '+*':
      sub += c
      state = 0
    else:
      sub = c
      check( sub )

print( maxLen, sMax )
print( default_timer()-t0 )

print( '---------------------------' )

#---------------------------------------------------------
# Медленное решение
# Автор: Л. Шастин
#---------------------------------------------------------

s = s0

t0 = default_timer()

for d in '23456789':
  s = s.replace( d, '1' )

for wrong in ['++','+*','*+','**']:
  s = s.replace( wrong, ' ')

s = ' ' + s
s = s.replace( '*00', '*0 0' )
s = s.replace( '*01', '*0 1' )
s = s.replace( '+00', '+0 0' )
s = s.replace( '+01', '+0 1' )
while ' 00' in s:
  s = s.replace( ' 00', ' 0' )
s = s.replace( ' 01', ' 0 1' )

sMax, maxLen = '', 0
if '0' in s:
  sMax, maxLen = '0', 1
for part in s.split():
  L = len(part)
  if L > maxLen:
    for i in range(L):
        # if all( not part[i:].startswith(x) for x in ["+", "*", "00", "01"] ):
        for j in range(i+maxLen+1,L+1):
          #if part[j-1] not in '+*' and eval(part[i:j]) == 0:
          if isZero(part[i:j]):
            sMax = part[i:j]
            #print( len(part[i:j]), part[i:j] )
            maxLen = j-i

print( maxLen, sMax )
print( default_timer()-t0 )

print( '----------------------' )

#---------------------------------------------------------
# Быстрое решение
# Автор: Л. Шастин
#---------------------------------------------------------

s = s0

t0 = default_timer()

for wrong in ['++','+*','*+','**']:
  s = s.replace( wrong, ' ')

s = s.replace('*00', '*0 0')
s = s.replace('*01', '*0 1')
s = s.replace('*00', '*0 0')
s = s.replace('*01', '*0 1')

s = ' ' + s
while ' 00' in s:
  s = s.replace(' 00', ' 0')
s = s.replace(' 01', ' 0 1')

if '0' in s:
  sMax, maxLen = '0', 1
else:
  sMax, maxLen = '', 0

s = [ x.strip('+*') for x in s.split() ]

for part in s:
  terms = part.split('+')
  sZero = []
  for t in terms:
    if '*0' in t or t.startswith('0'):
      sZero.append( t )
    elif '0*' in t:
      k = t.find( '0*' )
      sZero = [ t[k:] ]
    elif t.endswith('0'):
      sZero = [ t[-1]  ]
    else:
      sZero = []
    curLen = len( '+'.join(sZero) )
    if curLen > maxLen:
      sMax = sZero
      # print( curLen-1, sZero )
    maxLen = max( curLen, maxLen )

print( maxLen, sMax )
print( default_timer()-t0 )

print( '----------------------' )



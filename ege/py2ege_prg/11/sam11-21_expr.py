"""
Текстовый файл data11-21.txt состоит не более чем из 10^6 символов и содержит
только цифры шестнадцатеричной системы счисления, а также знаки «+» и «*» (сложения
и умножения). Определите максимальное количество символов в непрерывной последовательности,
которая начинается символами AFD, за которыми следует правильное арифметическое
выражение с целыми неотрицательными числами (без знака), записанными в десятичной
системе счисления. В этом выражении никакие два знака арифметических операций
не стоят рядом, в записи чисел отсутствуют незначащие (ведущие) нули. В ответе
укажите количество символов в найденном выражении.
Ответ: 72
"""
import timeit

s = open('data/data11-21.txt').readline()

def valid( subs ):
  if not subs.startswith("AFD"): return False
  subs = subs[3:]
  if len(subs) == 0 or subs[0] in "+*": return False
  subs = '*' + subs.replace( '+', '*' )
  return "**" not in subs and \
         all( "*0"+c not in subs for c in "0123456789")

t0 = timeit.default_timer()
N = len(s)
maxLen = 0
for L in range(N):
  for R in range(L+maxLen+1, N+1):
    if valid( s[L:R] ):
      if s[R-1] not in "+*" and R - L > maxLen:
        maxLen = R - L
        pos = L
    elif R - L > 3:
      break

print( maxLen, s[pos:pos+maxLen], timeit.default_timer()-t0 )

print( '---------------------------------------------' )

from re import findall

t0 = timeit.default_timer()

from re import findall
number = r'(?:[1-9]\d*|0)'
pattern = fr'(AFD{number}(?:[+*]{number})*)'
parts = findall( pattern, s )
sMax = max( parts, key=len )

print( len(sMax), sMax, timeit.default_timer()-t0 )

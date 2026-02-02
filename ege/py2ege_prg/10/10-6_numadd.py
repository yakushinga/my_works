"""
В первой строке текстового файла input.txt записаны два натуральных числа
N (1 ≤ N ≤ 10000) и K (1 ≤ K ≤ 1000).  В следующих N строках записаны целые
числа, по модулю не превышающие 10 000. Найдите число, делящееся на K, которое
встречается в файле чаще всего. Если таких чисел несколько, запишите в
ответе все эти числа.
"""
with open("i/input_6.txt") as F:
  N, K = map( int, F.readline().split() )
  count = {}
  for _ in range(N):
    n = int( F.readline() )
    if n % K == 0:
      count[n] = count.get(n, 0) + 1

maxCount = max( count.values() )
nMax = [ n for n in count
           if count[n] == maxCount ]

print( *nMax )

#----------------------------

with open("i/input_6.txt") as F:
  N, K = map( int, F.readline().split() )
  data = []
#  for s in F:
#    if n % K == 0:
#      data.append( int(s) )
  for _ in range(N):
    n = int(F.readline())
    if n % K == 0:
      data.append( n )

maxCount = 0
for n in set(data):
  count = data.count(n)
  if count > maxCount:
    maxCount = count
    nMax = [n]
  elif count == maxCount:
    nMax.append( n )

print( *nMax )

#----------------------------

#with open("i/input_6.txt") as F:
#  N, K, *data = map( int, F.read().split() )

N, K, *data = map( int, open("i/input_6.txt").read().split() )

data = [ n for n in data if n % K == 0 ]

maxCount = 0
for n in set(data):
  count = data.count(n)
  if count > maxCount:
    maxCount = count
    nMax = [n]
  elif count == maxCount:
    nMax.append( n )

print( *nMax )

#----------------------------

with open("i/input_6.txt") as F:
  N, K, *data = map( int, F.read().split() )

data = [ n for n in data if n % K == 0 ]

from collections import Counter
count = Counter( data )
print( count.most_common() )

maxCount = max( count.values() )
nMax = [ n for n in count
           if count[n] == maxCount ]
print( *nMax )

#----------------------------


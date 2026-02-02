"""
В текстовом файле input.txt содержится последова-тельность натуральных чисел,
каждое из которых не превышает 100 000. Определите количество троек элементов
последовательности, в которых ровно два из трёх элементов являются трёхзначными
числами, а сумма элементов тройки не больше максимального элемента
последовательности, оканчивающегося на 13. Гарантируется, что в
последовательности есть хотя бы одно число, оканчивающееся на 13. В ответе
запишите количество найденных троек чисел, затем максимальную из сумм элементов
таких троек. В данной задаче под тройкой подразумевается три идущих подряд
элемента последовательности.
(Ответ: 959 97471)
"""
with open('i/input_1.txt') as F:
  max13 = 0
  for s in F:
    n = int(s)
    if n % 100 == 13:
      max13 = max( n, max13 )
  print( max13 )

def valid( a ):
  count = 0
  for x in a:
    if 100 <= x <= 999:
        count += 1
  if count == 2 and sum(a) <= max13:
    return True
  else:
    return False

def valid( a ):
  digits3 = sum( 1 for x in a if 100 <= x <= 999 )
  if digits3 == 2 and sum(a) <= max13:
    return True
  else:
    return False

def valid( a ):
  digits3 = sum( 1 for x in a if 100 <= x <= 999 )
  return digits3 == 2 and sum(a) <= max13

count = maxSum = 0
with open('i/input_1.txt') as F:
  n2 = int(F.readline())
  n1 = int(F.readline())
  for s in F:
    n = int(s)
    if valid( [n, n1, n2] ):
      count += 1
      maxSum = max( n+n1+n2, maxSum )
    n2, n1 = n1, n

print( count, maxSum )

print('-------------------------------')

with open('i/input_1.txt') as F:
  #data = [ int(s) for s in F ]
  data = []
  for s in F:
    data.append( int(s) )

#max13 = max( x for x in data if x % 100 == 13 )

max13 = 0
for x in data:
  if x % 100 == 13:
    max13 = max( x, max13 )

print( max13 )

count = maxSum = 0
for i in range(len(data)-2):
  if valid( data[i:i+3] ):
    count += 1
    maxSum = max( sum(data[i:i+3]), maxSum )

print( count, maxSum )

print('-------------------------------')

data = [int(s) for s in open('i/input_1.txt') ]

max13 = max( x for x in data if x % 100 == 13 )
print( max13 )

results = []
for triple in zip(data, data[1:], data[2:]):
  if valid( triple ):
    results.append( sum(triple) )

print( len(results), max(results) )
















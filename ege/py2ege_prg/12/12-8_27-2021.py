"""
Файл input.txt содержит набор данных, состоящий из пар натуральных чисел. В
первой строке файла записано натуральное число N – количество пар чисел.
Каждая из следующих N строк содержит очередную пару: два натуральных числа,
разделённые пробелами. Необходимо выбрать из каж-дой пары ровно одно число так,
чтобы сумма всех выбранных чисел не делилась на 3 и при этом была максимально
возможной. Гарантируется, что искомую сумму получить можно. Программа должна
напечатать максимально возможную сумму, соответствующую условиям задачи.
(Ответ: 127127)
"""
F = open("i/input_8.txt")
N = int( F.readline() )

B = 3
dMin = float('inf')
sMax = 0
for s in F:
  a, b = map( int, s.split() )
  sMax += max( a, b )
  d = abs( a-b )
  if d % B != 0:
    dMin = min( d, dMin )

F.close()

if sMax % B != 0:
  print( sMax )
else:
  print( sMax - dMin )


print( '----------------------------------' )

with open("i/input_8.txt") as F:
  N = int( F.readline() )
  data = []
  for s in F:
    a, b = map( int, s.split() )
    data.append( (a, b) )

B = 3
dMin = float('inf')
sMax = 0
for a, b in data:
  sMax += max( a, b )
  d = abs( a-b )
  if d % B != 0:
    dMin = min( d, dMin )

if sMax % B != 0:
  print( sMax )
else:
  print( sMax - dMin )

if sMax % B != 0:
  print( sMax )
else:
  print( sMax - dMin )

print( sMax if sMax % B != 0 else sMax - dMin)

print( '----------------------------------' )

F = open("i/input_8.txt")
N = int( F.readline() )

def get():
  return list( map( int, F.readline().split() ) )

sums = get()
for _ in range(N-1):
  pair = get()
  sNext = [0]*B
  for a in sums:
    for b in pair:
      s = a + b
      sNext[s%B] = max( s, sNext[s%B] )
  sums = [ s for s in sNext if s > 0 ]
  #cmb = [ a+b for a in sums for b in pair ]
  #sums = [ max( x for x in cmb if x % B == r  )
  #         for r in range(B) ]

F.close()

print( max( sums[1:] ) )

print( '----------------------------------' )

F = open("i/input_8.txt")
N = int( F.readline() )

def get():
  return list( map( int, F.readline().split() ) )

sums = get()
for _ in range(N-1):
  pair = get()
  sums = [ a+b for a in sums for b in pair ]
  sums = [ max( x for x in sums if x % B == r  )
           for r in range(B)
           if any( x % B == r for x in sums ) ]

F.close()

print( max( x for x in sums if x % B > 0 ) )




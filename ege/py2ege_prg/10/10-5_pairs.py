"""
В файле input.txt содержится последовательность целых чисел. Элементы
последовательности могут принимать це-лые значения от –10 000 до 10 000
включительно. Определите количество пар последовательности, в которых только
одно число оканчивается на 3, и максимальную из сумм квадратов элементов таких
пар. В данной задаче под парой подразуме-вается два идущих подряд
элемента последовательности.
"""
def valid( a, b ):
  a, b = abs(a), abs(b)
  return (a % 10 == 3) and (b % 10 != 3) or \
         (a % 10 != 3) and (b % 10 == 3)

count, maxSqr = 0, 0
with open("i/input_5.txt") as F:
  prev = int( F.readline() )
  for s in F:
    n = int( s )
    if valid( prev, n ):
       count += 1
       maxSqr = max( prev**2 + n**2, maxSqr )
    prev = n

print( count, maxSqr )

#-----------------------------------

def valid( a, b ):
  return (abs(a) % 10 == 3) != (abs(b) % 10 == 3)
def valid( a, b ):
  return (abs(a) % 10 == 3) ^ (abs(b) % 10 == 3)

count, maxSqr = 0, 0
with open("i/input_5.txt") as F:
  prev = int( F.readline() )
  for s in F:
    n = int( s )
    if valid( prev, n ):
       count += 1
       maxSqr = max( prev**2 + n**2, maxSqr )
    prev = n

print( count, maxSqr )

#-----------------------------------

results = []
with open("i/input_5.txt") as F:
  prev = int( F.readline() )
  for s in F:
    n = int( s )
    if (abs(prev) % 10 == 3) != (abs(n) % 10 == 3):
       results.append( prev**2 + n**2 )
    prev = n

print( len(results), max(results) )

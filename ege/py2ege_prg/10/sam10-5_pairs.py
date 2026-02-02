"""
В файле data10-5.txt содержится последовательность целых чисел. Элементы
последовательности могут принимать целые значения от –10 000 до 10 000
включительно. Определите ко-личество пар элементов последовательности, в
которых оба числа заканчиваются на нечётную цифру, и минимальную из сумм
элементов таких пар. В данной задаче под парой подразумевается два идущих
подряд элемента последовательности.
(Ответ: 1194, –19292)
"""
def valid( a, b ):
  def val( x ):
    last = abs(x) % 10
    return last % 2 == 1
  return val(a) and val(b)

count, minSum = 0, 0
with open("data/data10-5.txt") as F:
  prev = int( F.readline() )
  for s in F:
    n = int( s )
    if valid( prev, n ):
       count += 1
       minSum = min( prev + n, minSum )
    prev = n

print( count, minSum )

#-----------------------------------

def valid( a, b ):
  return abs(a) % 10 in [1, 3, 5, 7, 9] and \
         abs(b) % 10 in [1, 3, 5, 7, 9]

results = []
with open("data/data10-5.txt") as F:
  prev = int( F.readline() )
  for s in F:
    n = int( s )
    if valid( prev, n ):
       results.append( prev + n )
    prev = n

print( len(results), min(results) )

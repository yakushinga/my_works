"""
В текстовом файле input.txt содержится последовательность целых чисел, каждое
из которых по модулю не превышает 100 000. Определите количество троек, для
которых выполняются следующие условия:
– в тройке есть четырёхзначные числа, но не все числа четырёхзначные;
– в тройке больше чисел, кратных 13, чем чисел, кратных 7;
– каждый элемент тройки больше среднего арифметического всех элементов
последовательности, запись которых заканчивается на 151. (Гарантируется, что
в последовательности есть хотя бы один элемент, запись которого заканчивается на 151.)
В ответе запишите количество найденных троек, затем – минимальную из сумм
элементов таких троек. В данной задаче под тройкой подразумевается три идущих
подряд элемента последовательности.
(Ответ: 44 37313)
"""
data = [ int(s) for s in open('i/input_2.txt') ]

last151 = [ x for x in data if abs(x) % 1000 == 151 ]
avg151 = sum(last151) / len(last151)

def valid( a ):
  dig4 = sum( 1 for x in a if 1000 <= abs(x) <= 9999 )
  last3 = sum( 1 for x in a if abs(x) % 10 == 3 )
  last7 = sum( 1 for x in a if abs(x) % 10 == 7 )
  return 1 <= dig4 <= 2 and last3 > last7 and \
         all( x > avg151 for x in a )

count, sMin = 0, float('inf')
for i in range(len(data)-2):
  if valid( data[i:i+3] ):
    count += 1
    sMin = min( sum(data[i:i+3]), sMin )

print( count, sMin )

#--------------------------------------------------------

results = []
for i in range(len(data)-2):
  triple = data[i:i+3]
  if valid( triple ):
    results.append( sum(triple) )

print( len(results), min(results) )

#--------------------------------------------------------

results = []
for i in range(len(data)-2):
  tri = data[i:i+3]
  dig4 = sum( 1 for x in tri if 1000 <= abs(x) <= 9999 )
  last3 = sum( 1 for x in tri if abs(x) % 10 == 3 )
  last7 = sum( 1 for x in tri if abs(x) % 10 == 7 )
  if 1<= dig4 <= 2 and last3 > last7 and \
     all( x > avg151 for x in tri ) :
    results.append( sum(tri) )

print( len(results), min(results) )













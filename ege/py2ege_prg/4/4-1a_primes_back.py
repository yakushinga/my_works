"""
Среди чисел, больших, чем 10000000, найдите пять минимальных простых чисел.
Вывести найденные числа в порядке УБЫВАНИЯ.
(Ответ:
10000139
10000121
10000103
10000079
10000019 )
"""
import timeit
def isPrime( n ):
  return all( n % d != 0
              for d in range(2,round(n**0.5)+1) )

t0 = timeit.default_timer()

count = 0
n = 10000000
results = []
while count < 5:
  if isPrime( n ):
    results.append( n )
    count += 1
  n += 1

for n in results[::-1]:
  print( n )

print( timeit.default_timer() - t0 )


"""
Среди чисел, больших, чем 10000000, найдите пять минимальных
натуральных чисел, у которых больше 200 делителей. Выведите эти числа в порядке
возрастания, справа от каждого числа выведите количество его делителей.
(Ответ:
10000080
10001376
10001880
10003500
10006920
)
"""
import timeit

def divisors( n ):
  q = round( n**0.5 )
  divs = []
  for d in range(1,q+1):
    if n % d == 0:
      divs.append( d )
      if n//d != d:
        divs.append( n//d )
  return sorted(divs)

t0 = timeit.default_timer()

count = 0
n = 10_000_001
while count < 5:
  divs = divisors(n)
  if len(divs) > 200:
    print( n, len(divs) )
    count += 1
  n += 1

print( timeit.default_timer() - t0 )

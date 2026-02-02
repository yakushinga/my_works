"""
Среди чисел, не превышающих 20000000, найдите пять максимальных натуральных
чисел, у которых больше 150 делителей. Выведите эти числа в порядке возрастания,
справа от каждого числа выведите количество его делителей.
(Ответ:
19998160 160
19998720 288
19999440 160
19999650 192
19999980 384
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
n = 20_000_000
results = []
while len(results) < 5:
  divs = divisors(n)
  if len(divs) > 150:
    results.append( (n, len(divs)) )
  n -= 1

for n, nDivs in results[::-1]:
  print( n, nDivs )

print( timeit.default_timer() - t0 )

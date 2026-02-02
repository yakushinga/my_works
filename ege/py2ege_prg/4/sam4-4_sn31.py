"""
Пусть S(n) – сумма двух наибольших нетривиальных делите-лей числа n (не считая
единицы и самого числа). Если у числа n меньше двух таких делителей, то S(n)
считается равным 0. Найдите 5 наименьших натуральных чисел, превышающих
20 000 000, для которых 0 < S(n) < 10 000 и S(n) кратно 31. В ответе запишите
значения S(n) в порядке возрастания, справа от каждого их них запишите
соответствующее число n.
(Ответ:
9052 19987651
9114 19991849
9300 19991771
9486 19999649
9796 19986403
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
  if len(divs) >= 4:
    S = divs[-2] + divs[-3]
    if S < 10000 and S % 31 == 0:
      results.append( (S, n) )
  n -= 1

for S, n in sorted(results):
  print( S, n )

print( timeit.default_timer() - t0 )

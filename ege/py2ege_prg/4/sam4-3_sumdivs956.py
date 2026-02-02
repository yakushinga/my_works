"""
Найдите 5 наибольших натуральных чисел, не превышающих 10 000 000, для которых
сумма всех делителей оканчивается на 956. В ответе для каждого найденного
числа запишите сначала значение суммы делителей, а затем – наибольший делитель,
не равный самому числу.
(Ответ:
10021956 21881
14998956 4999651
19840956 4999264
14437956 3331833
10763956 768853
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
n = 10_000_000
count = 0
while count < 5:
  divs = divisors(n)
  s = sum(divs)
  if s % 1000 == 956:
    print( s, divs[-2] )
    count += 1
  n -= 1

print( timeit.default_timer() - t0 )

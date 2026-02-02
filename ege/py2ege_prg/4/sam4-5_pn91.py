"""
Обозначим через P(N) – произведение 5 наименьших различных нетривиальных
делителей натурального числа N (не считая единицы и самого числа). Если у
числа N меньше 5 таких делителей, то P(N) считается равным нулю. Найдите 5
наименьших натуральных чисел, превышающих 5 000 000, для которых P(N)
оканчивается на 91 и не превышает N. В ответе для каждого найденного числа
запишите сначала значение P(N), а затем – наибольший делитель, вошедший в
произведение P(N).
(Ответ:
242991 29
260091 39
1933191 41
3483891 81
3483891 81
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
n = 500_000_001
results = []
while len(results) < 5:
  divs = divisors(n)
  if len(divs) >= 7:
    P = divs[1]*divs[2]*divs[3]*divs[4]*divs[5]
    if P <= n and P % 100 == 91:
      results.append( (P, divs[5]) )
  n += 1

for P, dMax in sorted(results):
  print( P, dMax )

print( timeit.default_timer() - t0 )

"""
Среди всех пятизначных чисел найдите числа, для которых сумма всех
нетривиальных делителей – простое число. Выведите на экран количество таких чисел.
(Ответ: 7349)
"""
def divisors( n ):
  q = round( n**0.5 )
  divs = set()
  for d in range(1,q+1):
    if n % d == 0:
      divs |= { d, n//d }
  return sorted(divs)

def isPrime( n ):
  return all( n % d != 0
              for d in range(2,round(n**0.5)+1) )

count = 0
for n in range(10**4, 10**5):
  divs = divisors( n )
  s = sum(divs[1:-1])
  if s > 0 and isPrime(s):
    # print( n, s )
    count += 1

print( count )

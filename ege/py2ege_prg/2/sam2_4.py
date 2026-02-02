"""
(Е. Джобс) Найдите все числа, принадлежащие отрезку [33333; 55555], которые
кратны сумме своих простых делителей. В качестве ответа приведите числа,
для которых сумма простых делителей больше 250, – сначала найденное число,
затем сумму его простых делителей. Само число в качестве делителя не учитывается.
(Ответ: 38086 278, 44998 302, 53332 268)
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

for n in range(33333, 55555+1):
  divs = divisors( n )
  sumDivs = sum( d for d in divs[1:-1] if isPrime(d) )
  if sumDivs > 0 and n % sumDivs == 0 and sumDivs > 250:
    print( n, sumDivs )

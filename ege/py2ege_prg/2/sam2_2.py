"""
Среди всех пятизначных чисел найдите числа, которые имеют наибольшее
количество нетривиальных делителей. Выведите на экран сами числа в порядке
убывания, а справа от каждого числа – сумму его нетривиальных делителей.
(Ответ: 98280 304919, 83160 262439)
"""
def divisors( n ):
  q = round( n**0.5 )
  divs = set()
  for d in range(1,q+1):
    if n % d == 0:
      divs |= { d, n//d }
  return sorted(divs)

nDivs = 0
for n in range(10**4, 10**5):
  divs = divisors( n )
  k = len(divs[1:-1])
  sDivs = sum(divs[1:-1])
  if k > nDivs:
    nDivs = k
    ans = [(n, sDivs)]
  elif k == nDivs:
    ans.append( (n, sDivs) )

for n, sDivs in ans[::-1]:
  print( n, sDivs )

def sum_n( n ):
  s = 0
  for i in range(1, n+1):
    s += i
  return s

mem = {}
def sum_n( n ):
  if n in mem:
    return mem[n]
  s = 0
  for i in range(1, n+1):
    s += i
  mem[n] = s
  return s

import timeit

t0 = timeit.default_timer()
N = 1_000_000
for i in range(N):
  s = sum_n(1000)
print( s )
print( timeit.default_timer() - t0 )
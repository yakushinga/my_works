import timeit
import string
from random import choice
N = 1_000_000
s = ''
for _ in range(N):
  s += choice(string.ascii_uppercase)

N = 100
start = timeit.default_timer()
for i in range(N):
  count = 0
  for c in s:
    if c == 'X':
      count += 1
dt1 = timeit.default_timer() - start
print( count, dt1 )

start = timeit.default_timer()
for i in range(N):
  count = s.count('X')
dt2 = timeit.default_timer() - start
print( count, dt2 )

print( dt1/dt2)

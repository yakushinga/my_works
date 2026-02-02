import timeit

t0 = timeit.default_timer()
def F( n ):
  fn1, fn2 = 1, 1
  for i in range(3,n+1):
    fn1, fn2 = fn1 + 2*fn2, fn1
  return fn1

for i in range(1000):
  F100 = F(100) % 10**6
print( F100, timeit.default_timer() - t0 )

print('---------------------------------')

t0 = timeit.default_timer()
D = 10**6
def F( n ):
  fn1, fn2 = 1, 1
  for i in range(3,n+1):
    fn1, fn2 = (fn1 + 2*fn2) % D , fn1
  return fn1

for i in range(1000):
  F100 = F(100) % 10**6

print( F100, timeit.default_timer() - t0 )

"""
Сколько существует чисел, шестнадцатеричная запись которых состоит из четырёх
различных цифр, причём никакие две чётные или две нечётные цифры
не стоят рядом?
"""
import timeit

def valid( w ):
  if w[0] == '0': return False
  if len(w) != len(set(w)): return False
  even = '02468ACE'
  for i in range(len(w)-1):
    if (w[i] in even) == (w[i+1] in even):
      return False
  return True

from itertools import product
t0 = timeit.default_timer()
count = 0
for w in product('0123456789ABCDEF', repeat=4):
  if valid( w ):
    count += 1

print( count, timeit.default_timer() - t0 )

#---------------------------------------------

def valid( w ):
  if w[0] == '0': return False
#  if len(w) != len(set(w)): return False
  even = '02468ACE'
  for i in range(len(w)-1):
    if (w[i] in even) == (w[i+1] in even):
      return False
  return True

from itertools import permutations
t0 = timeit.default_timer()
count = 0
for w in permutations('0123456789ABCDEF', 4):
  if valid( w ):
    count += 1
print( count, timeit.default_timer() - t0 )

#---------------------------------------------

from itertools import permutations
print( len( [ w for w in permutations('0123456789ABCDEF', 4)
                if valid( w ) ] )  )

#---------------------------------------------

from itertools import permutations
print( sum( valid( w )
            for w in permutations('0123456789ABCDEF', 4) )  )

#---------------------------------------------

def valid( w ):
  if w[0] == '0': return False
  if len(w) != len(set(w)): return False
  for i in range(1, len(w)):
    if ord(w[i-1]) % 2 == ord(w[i]) % 2:
      return False
  return True

from itertools import permutations
count = 0
for w in product('0123456789BCDEFG', repeat=4):
#for w in permutations('0123456789BCDEFG', 4):
  if valid( w ):
    count += 1

print( count )

